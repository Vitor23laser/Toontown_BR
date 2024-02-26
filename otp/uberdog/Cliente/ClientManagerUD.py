from panda3d.direct import DCPacker

from direct.fsm.FSM import FSM
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *

from otp.otpbase import OTPGlobals

from toontown.makeatoon.NameGenerator import NameGenerator
from toontown.toon.ToonDNA import ToonDNA
from toontown.toonbase import TTLocalizer

from datetime import datetime

import anydbm, hmac, time, json, os

blacklist = []

if blacklist:
    blacklist = json.dumps(blacklist)

def judgeName(name):
    if not name:
        return False
    if blacklist:
        for namePart in name.split(' '):
            namePart = namePart.lower()
            if len(namePart) < 1:
                return False
            for banned in blacklist.get(namePart[0], []):
                if banned in namePart:
                    return False
    return True

# --- ACCOUNT DATABASES ---
# These classes make up the available account databases for Toontown.
# DeveloperAccountDB is a special database that accepts a username.

class AccountDB:
    notify = directNotify.newCategory('AccountDB')

    def __init__(self, clientManager):
        self.clientManager = clientManager

        FOLDER_PATH = 'otpd/databases/otpdb'

        if not os.path.exists(FOLDER_PATH):
            os.makedirs(FOLDER_PATH)

        filename = simbase.config.GetString('account-bridge-filename', 'otpd/databases/account-bridge.db')
        self.dbm = anydbm.open(filename, 'c')

    def addNameRequest(self, avId, name):
        return 'Success'

    def getNameStatus(self, avId):
        return 'APPROVED'

    def removeNameRequest(self, avId):
        return 'Success'

    def lookup(self, username, callback):
        pass  # Inheritors should override this.

    def storeAccountID(self, userId, accountId, callback):
        self.dbm[str(userId)] = str(accountId)  # anydbm only allows strings.
        if getattr(self.dbm, 'sync', None):
            self.dbm.sync()
            callback(True)
        else:
            self.notify.warning('Unable to associate user %s with account %d!' % (userId, accountId))
            callback(False)

class AccountHandler(AccountDB):
    notify = directNotify.newCategory('AccountHandler')

    def lookup(self, username, callback):
        # Let's check if this user's ID is in your account database bridge:
        if str(username) not in self.dbm:

            # Nope. Let's associate them with a brand new Account object!
            response = {
                'success': True,
                'userId': username,
                'accountId': 0,
            }
            callback(response)
            return response

        else:

            # We have an account already, let's return what we've got:
            response = {
                'success': True,
                'userId': username,
                'accountId': int(self.dbm[str(username)]),
            }
            callback(response)
            return response

# --- FSMs ---
class OperationFSM(FSM):
    TARGET_CONNECTION = False

    def __init__(self, clientManager, target):
        self.clientManager = clientManager
        self.target = target

        FSM.__init__(self, self.__class__.__name__)

    def enterKill(self, reason = ''):
        if self.TARGET_CONNECTION:
            self.clientManager.killConnection(self.target, reason)
        else:
            self.clientManager.killAccount(self.target, reason)
        self.demand('Off')

    def enterOff(self):
        if self.TARGET_CONNECTION:
            del self.clientManager.connection2fsm[self.target]
        else:
            del self.clientManager.account2fsm[self.target]

class LoginAccountFSM(OperationFSM):
    notify = directNotify.newCategory('LoginAccountFSM')
    TARGET_CONNECTION = True

    def enterStart(self, token):
        self.token = token
        self.demand('QueryAccountDB')

    def enterQueryAccountDB(self):
        self.clientManager.accountDB.lookup(self.token, self.__handleLookup)

    def __handleLookup(self, result):
        if not result.get('success'):
            self.clientManager.air.writeServerEvent('tokenRejected', self.target, self.token)
            self.demand('Kill', result.get('reason', 'The account server rejected your token.'))
            return

        self.userId = result.get('userId', 0)
        self.accountId = result.get('accountId', 0)

        if self.accountId:
            self.demand('RetrieveAccount')
        else:
            self.demand('CreateAccount')

    def enterRetrieveAccount(self):
        self.clientManager.air.dbInterface.queryObject(self.clientManager.air.dbId, self.accountId, self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.clientManager.air.dclassesByName['AccountUD']:
            self.demand('Kill', 'Your account object was not found in the database!')
            return

        self.account = fields
        self.demand('SetAccount')

    def enterCreateAccount(self):
        self.account = {
            'ACCOUNT_AV_SET': [0] * 6,
            'pirateAvatars': [0],
            'HOUSE_ID_SET': [0],
            'ESTATE_ID': 0,
            'ACCOUNT_AV_SET_DEL': [],
            'CREATED': time.ctime(),
            'LAST_LOGIN': time.ctime(),
            'ACCOUNT_ID': str(self.userId)
        }
        self.clientManager.air.dbInterface.createObject(
            self.clientManager.air.dbId,
            self.clientManager.air.dclassesByName['AccountUD'],
            self.account,
            self.__handleCreate)

    def __handleCreate(self, accountId):
        if self.state != 'CreateAccount':
            self.notify.warning('Received a create account response outside of the CreateAccount state.')
            return

        if not accountId:
            self.notify.warning('Database failed to construct an account object!')
            self.demand('Kill', 'Your account object could not be created in the game database.')
            return

        self.accountId = accountId
        self.clientManager.air.writeServerEvent('accountCreated', accountId)
        self.demand('StoreAccountID')

    def enterStoreAccountID(self):
        self.clientManager.accountDB.storeAccountID(
            self.userId,
            self.accountId,
            self.__handleStored)

    def __handleStored(self, success = True):
        if not success:
            self.demand('Kill', 'The account server could not save your user ID!')
            return

        self.demand('SetAccount')

    def enterSetAccount(self):
        # If there's anybody on the account, kill them for redundant login:
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.clientManager.GetAccountConnectionChannel(self.accountId),
            self.clientManager.air.ourChannel,
            CLIENTAGENT_EJECT)
        datagram.addUint16(100)
        datagram.addString('This account has been logged in from elsewhere.')
        self.clientManager.air.send(datagram)

        # Next, add this connection to the account channel.
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.target,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_OPEN_CHANNEL)
        datagram.addChannel(self.clientManager.GetAccountConnectionChannel(self.accountId))
        self.clientManager.air.send(datagram)

        # Now set their sender channel to represent their account affiliation:
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.target,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_SET_CLIENT_ID)
        # Account ID in high 32 bits, 0 in low (no avatar):
        datagram.addChannel(self.accountId << 32)
        self.clientManager.air.send(datagram)

        # Un-sandbox them!
        self.clientManager.air.setClientState(self.target, 2)  # ESTABLISHED state.

        # Update the last login timestamp:
        self.clientManager.air.dbInterface.updateObject(
            self.clientManager.air.dbId,
            self.accountId,
            self.clientManager.air.dclassesByName['AccountUD'],
            {'LAST_LOGIN': time.ctime(),
             'ACCOUNT_ID': str(self.userId)})

        responseData = {
            'returnCode': 0,
            'respString': '',
            'accountNumber': self.target,
            'createFriendsWithChat': 'YES',
            'chatCodeCreationRule': 'YES',
            'access': 'FULL',
            'WhiteListResponse': 'YES',
            'lastLoggedInStr': self.getLastLoggedInStr(),
            'accountDays': self.getAccountDays(),
            'serverTime': int(time.time()),
            'toonAccountType': 'NO_PARENT_ACCOUNT',
            'userName': str(self.userId)
        }

        responseBlob = json.dumps(responseData)

        # We're done.
        self.clientManager.air.writeServerEvent('accountLogin', self.target, self.accountId, self.userId)
        self.clientManager.sendUpdateToChannel(self.target, 'acceptLogin', [int(time.time()), responseBlob])
        self.demand('Off')

    def getLastLoggedInStr(self):
        lastLoggedInStr = time.strftime('%Y-%m-%d %I:%M:%S')

        return lastLoggedInStr

    def getAccountCreationDate(self):
        accountCreationDate = self.account.get('CREATED', '')

        try:
            accountCreationDate = datetime.fromtimestamp(time.mktime(time.strptime(accountCreationDate)))
        except ValueError:
            accountCreationDate = ''

        return accountCreationDate

    def getAccountDays(self):
        accountCreationDate = self.getAccountCreationDate()
        accountDays = -1

        if accountCreationDate:
            now = datetime.fromtimestamp(time.mktime(time.strptime(time.ctime())))
            accountDays = abs((now - accountCreationDate).days)

        return accountDays

class CreateAvatarFSM(OperationFSM):
    notify = directNotify.newCategory('CreateAvatarFSM')

    def enterStart(self, dna, index):
        # Basic sanity-checking:
        if index >= 6:
            self.demand('Kill', 'Invalid index specified!')
            return

        if not ToonDNA().isValidNetString(dna):
            self.demand('Kill', 'Invalid DNA specified!')
            return

        self.index = index
        self.dna = dna

        # Okay, we're good to go, let's query their account.
        self.demand('RetrieveAccount')

    def enterRetrieveAccount(self):
        self.clientManager.air.dbInterface.queryObject(
            self.clientManager.air.dbId, self.target, self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.clientManager.air.dclassesByName['AccountUD']:
            self.demand('Kill', 'Your account object was not found in the database!')
            return

        self.account = fields

        self.avList = self.account['ACCOUNT_AV_SET']
        # Sanitize:
        self.avList = self.avList[:6]
        self.avList += [0] * (6-len(self.avList))

        # Make sure the index is open:
        if self.avList[self.index]:
            self.demand('Kill', 'This avatar slot is already taken by another avatar!')
            return

        # Okay, there's space. Let's create the avatar!
        self.demand('CreateAvatar')

    def enterCreateAvatar(self):
        dna = ToonDNA()
        dna.makeFromNetString(self.dna)
        colorString = TTLocalizer.NumToColor[dna.headColor]
        animalType = TTLocalizer.AnimalToSpecies[dna.getAnimal()]
        name = ' '.join((colorString, animalType))
        toonFields = {
            'setName': (name,),
            'WishNameState': ('OPEN',),
            'WishName': ('',),
            'setDNAString': (self.dna,),
            'setDISLid': (self.target,)
        }
        self.clientManager.air.dbInterface.createObject(
            self.clientManager.air.dbId,
            self.clientManager.air.dclassesByName['DistributedToonUD'],
            toonFields,
            self.__handleCreate)

    def __handleCreate(self, avId):
        if not avId:
            self.demand('Kill', 'Database failed to create the new avatar object!')
            return

        self.avId = avId
        self.demand('StoreAvatar')

    def enterStoreAvatar(self):
        # Associate the avatar with the account...
        self.avList[self.index] = self.avId
        self.clientManager.air.dbInterface.updateObject(
            self.clientManager.air.dbId,
            self.target,
            self.clientManager.air.dclassesByName['AccountUD'],
            {'ACCOUNT_AV_SET': self.avList},
            {'ACCOUNT_AV_SET': self.account['ACCOUNT_AV_SET']},
            self.__handleStoreAvatar)

    def __handleStoreAvatar(self, fields):
        if fields:
            self.demand('Kill', 'Database failed to associate the new avatar to your account!')
            return

        # Otherwise, we're done!
        self.clientManager.air.writeServerEvent('avatarCreated', self.avId, self.target, self.dna.encode('hex'), self.index)
        self.clientManager.sendUpdateToAccountId(self.target, 'createAvatarResp', [self.avId])
        self.demand('Off')

class AvatarOperationFSM(OperationFSM):
    POST_ACCOUNT_STATE = 'Off'  # This needs to be overridden.

    def enterRetrieveAccount(self):
        # Query the account:
        self.clientManager.air.dbInterface.queryObject(
            self.clientManager.air.dbId, self.target, self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.clientManager.air.dclassesByName['AccountUD']:
            self.demand('Kill', 'Your account object was not found in the database!')
            return

        self.account = fields

        self.avList = self.account['ACCOUNT_AV_SET']
        # Sanitize:
        self.avList = self.avList[:6]
        self.avList += [0] * (6-len(self.avList))

        self.demand(self.POST_ACCOUNT_STATE)

class GetAvatarsFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('GetAvatarsFSM')
    POST_ACCOUNT_STATE = 'QueryAvatars'

    def enterStart(self):
        self.demand('RetrieveAccount')

    def enterQueryAvatars(self):
        self.pendingAvatars = set()
        self.avatarFields = {}
        for avId in self.avList:
            if avId:
                self.pendingAvatars.add(avId)

                def response(dclass, fields, avId=avId):
                    if self.state != 'QueryAvatars':
                        return
                    if dclass != self.clientManager.air.dclassesByName['DistributedToonUD']:
                        self.demand('Kill', "One of the account's avatars is invalid!")
                        return
                    self.avatarFields[avId] = fields
                    self.pendingAvatars.remove(avId)
                    if not self.pendingAvatars:
                        self.demand('SendAvatars')

                self.clientManager.air.dbInterface.queryObject(
                    self.clientManager.air.dbId,
                    avId,
                    response)

        if not self.pendingAvatars:
            self.demand('SendAvatars')

    def enterSendAvatars(self):
        potentialAvs = []

        for avId, fields in self.avatarFields.items():
            index = self.avList.index(avId)
            wishNameState = fields.get('WishNameState', [''])[0]
            name = fields['setName'][0]
            nameState = 0

            if wishNameState == 'OPEN':
                nameState = 1
            elif wishNameState == 'PENDING':
                actualNameState = self.clientManager.accountDB.getNameStatus(avId)
                self.clientManager.air.dbInterface.updateObject(
                    self.clientManager.air.dbId,
                    avId,
                    self.clientManager.air.dclassesByName['DistributedToonUD'],
                    {'WishNameState': [actualNameState]}
                )
                if actualNameState == 'PENDING':
                    nameState = 2
                if actualNameState == 'APPROVED':
                    nameState = 3
                    name = fields['WishName'][0]
                elif actualNameState == 'REJECTED':
                    nameState = 4
            elif wishNameState == 'APPROVED':
                nameState = 3
            elif wishNameState == 'REJECTED':
                nameState = 4

            potentialAvs.append([avId, name, fields['setDNAString'][0], index, nameState])

        self.clientManager.sendUpdateToAccountId(self.target, 'setAvatars', [potentialAvs])
        self.demand('Off')

# This inherits from GetAvatarsFSM, because the delete operation ends in a
# setAvatars message being sent to the client.
class DeleteAvatarFSM(GetAvatarsFSM):
    notify = directNotify.newCategory('DeleteAvatarFSM')
    POST_ACCOUNT_STATE = 'ProcessDelete'

    def enterStart(self, avId):
        self.avId = avId
        GetAvatarsFSM.enterStart(self)

    def enterProcessDelete(self):
        if self.avId not in self.avList:
            self.demand('Kill', 'Tried to delete an avatar not in the account!')
            return

        index = self.avList.index(self.avId)
        self.avList[index] = 0

        avsDeleted = list(self.account.get('ACCOUNT_AV_SET_DEL', []))
        if len(avsDeleted) >= 100:
            avsDeleted.pop(0)
        avsDeleted.append([self.avId, int(time.time())])

        estateId = self.account.get('ESTATE_ID', 0)

        if estateId != 0:
            # This assumes that the house already exists, but it shouldn't
            # be a problem if it doesn't.
            self.clientManager.air.dbInterface.updateObject(
                self.clientManager.air.dbId,
                estateId,
                self.clientManager.air.dclassesByName['DistributedEstateAI'],
                {'setSlot%dToonId' % index: [0],
                 'setSlot%dItems' % index: [[]]}
            )

        self.clientManager.air.dbInterface.updateObject(
            self.clientManager.air.dbId,
            self.target,
            self.clientManager.air.dclassesByName['AccountUD'],
            {'ACCOUNT_AV_SET': self.avList,
             'ACCOUNT_AV_SET_DEL': avsDeleted},
            {'ACCOUNT_AV_SET': self.account['ACCOUNT_AV_SET'],
             'ACCOUNT_AV_SET_DEL': self.account['ACCOUNT_AV_SET_DEL']},
            self.__handleDelete)
        self.clientManager.accountDB.removeNameRequest(self.avId)

    def __handleDelete(self, fields):
        if fields:
            self.demand('Kill', 'Database failed to mark the avatar as deleted!')
            return

        self.clientManager.air.writeServerEvent('avatarDeleted', self.avId, self.target)
        self.demand('QueryAvatars')

class SetNameTypedFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('SetNameTypedFSM')
    POST_ACCOUNT_STATE = 'RetrieveAvatar'

    def enterStart(self, avId, name):
        self.avId = avId
        self.name = name

        if self.avId:
            self.demand('RetrieveAccount')
            return

        # Hmm, self.avId was 0. Okay, let's just cut to the judging:
        self.demand('JudgeName')

    def enterRetrieveAvatar(self):
        if self.avId and self.avId not in self.avList:
            self.demand('Kill', 'Tried to name an avatar not in the account!')
            return

        self.clientManager.air.dbInterface.queryObject(self.clientManager.air.dbId, self.avId,
                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.clientManager.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        if fields['WishNameState'][0] != 'OPEN':
            self.demand('Kill', 'Avatar is not in a namable state!')
            return

        self.demand('JudgeName')

    def enterJudgeName(self):
        # Let's see if the name is valid:
        status = judgeName(self.name)

        if self.avId and status:
            resp = self.clientManager.accountDB.addNameRequest(self.avId, self.name)
            if resp != 'Success':
                status = False
            else:
                self.clientManager.air.dbInterface.updateObject(
                    self.clientManager.air.dbId,
                    self.avId,
                    self.clientManager.air.dclassesByName['DistributedToonUD'],
                    {'WishNameState': ('PENDING',),
                     'WishName': (self.name,)})

        if self.avId:
            self.clientManager.air.writeServerEvent('avatarWishname', self.avId, self.name)

        self.clientManager.sendUpdateToAccountId(self.target, 'setNameTypedResp', [self.avId, status])
        self.demand('Off')

class SetNamePatternFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('SetNamePatternFSM')
    POST_ACCOUNT_STATE = 'RetrieveAvatar'

    def enterStart(self, avId, pattern):
        self.avId = avId
        self.pattern = pattern

        self.demand('RetrieveAccount')

    def enterRetrieveAvatar(self):
        if self.avId and self.avId not in self.avList:
            self.demand('Kill', 'Tried to name an avatar not in the account!')
            return

        self.clientManager.air.dbInterface.queryObject(self.clientManager.air.dbId, self.avId,
                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.clientManager.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        if fields['WishNameState'][0] != 'OPEN':
            self.demand('Kill', 'Avatar is not in a namable state!')
            return

        self.demand('SetName')

    def enterSetName(self):
        # Render the pattern into a string:
        parts = []
        for p, f in self.pattern:
            part = self.clientManager.nameGenerator.nameDictionary.get(p, ('', ''))[1]
            if f:
                part = part[:1].upper() + part[1:]
            else:
                part = part.lower()
            parts.append(part)

        parts[2] += parts.pop(3) # Merge 2&3 (the last name) as there should be no space.
        while '' in parts:
            parts.remove('')
        name = ' '.join(parts)

        self.clientManager.air.dbInterface.updateObject(
            self.clientManager.air.dbId,
            self.avId,
            self.clientManager.air.dclassesByName['DistributedToonUD'],
            {'WishNameState': ('',),
             'WishName': ('',),
             'setName': (name,)})

        self.clientManager.air.writeServerEvent('avatarNamed', self.avId, name)
        self.clientManager.sendUpdateToAccountId(self.target, 'setNamePatternResp', [self.avId, 1])
        self.demand('Off')

class AcknowledgeNameFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('AcknowledgeNameFSM')
    POST_ACCOUNT_STATE = 'GetTargetAvatar'

    def enterStart(self, avId):
        self.avId = avId
        self.demand('RetrieveAccount')

    def enterGetTargetAvatar(self):
        # Make sure the target avatar is part of the account:
        if self.avId not in self.avList:
            self.demand('Kill', 'Tried to acknowledge name on an avatar not in the account!')
            return

        self.clientManager.air.dbInterface.queryObject(self.clientManager.air.dbId, self.avId, self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.clientManager.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        # Process the WishNameState change.
        wishNameState = fields['WishNameState'][0]
        wishName = fields['WishName'][0]
        name = fields['setName'][0]

        if wishNameState == 'APPROVED':
            wishNameState = ''
            name = wishName
            wishName = ''
            self.clientManager.accountDB.removeNameRequest(self.avId)
        elif wishNameState == 'REJECTED':
            wishNameState = 'OPEN'
            wishName = ''
            self.clientManager.accountDB.removeNameRequest(self.avId)
        else:
            self.demand('Kill', "Tried to acknowledge name on an avatar in %s state!" % wishNameState)
            return

        # Push the change back through:
        self.clientManager.air.dbInterface.updateObject(
            self.clientManager.air.dbId,
            self.avId,
            self.clientManager.air.dclassesByName['DistributedToonUD'],
            {'WishNameState': (wishNameState,),
             'WishName': (wishName,),
             'setName': (name,)},
            {'WishNameState': fields['WishNameState'],
             'WishName': fields['WishName'],
             'setName': fields['setName']})

        self.clientManager.sendUpdateToAccountId(self.target, 'acknowledgeAvatarNameResp', [])
        self.demand('Off')

class LoadAvatarFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('LoadAvatarFSM')
    POST_ACCOUNT_STATE = 'GetTargetAvatar'

    def enterStart(self, avId):
        self.avId = avId
        self.demand('RetrieveAccount')

    def enterGetTargetAvatar(self):
        # Make sure the target avatar is part of the account:
        if self.avId not in self.avList:
            self.demand('Kill', 'Tried to play an avatar not in the account!')
            return

        self.clientManager.air.dbInterface.queryObject(self.clientManager.air.dbId, self.avId,
                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.clientManager.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        self.avatar = fields
        self.demand('SetAvatar')

    def generateAvatar(self):
        dclass = self.clientManager.air.dclassesByName['DistributedToonUD']
        requiredPacker = DCPacker()
        otherCount = 0
        otherPacker = DCPacker()

        for f in range(dclass.getNumInheritedFields()):
            field = dclass.getInheritedField(f)
            if field.isRequired():
                requiredPacker.beginPack(field)
                if field.getName() in self.avatar:
                    field.packArgs(requiredPacker, self.avatar[field.getName()])
                else:
                    requiredPacker.packDefaultValue()
                requiredPacker.endPack()
            elif field.isRam() and field.getName() in self.avatar:
                otherPacker.rawPackUint16(field.getNumber())
                otherPacker.beginPack(field)
                field.packArgs(otherPacker, self.avatar[field.getName()])
                otherPacker.endPack()
                otherCount += 1

        dg = PyDatagram()
        dg.addServerHeader(self.clientManager.air.serverId, self.clientManager.air.ourChannel, STATESERVER_CREATE_OBJECT_WITH_REQUIRED_OTHER)
        dg.addUint32(self.avId)
        dg.addUint32(0)
        dg.addUint32(0)
        dg.addUint16(dclass.getNumber())
        dg.appendData(requiredPacker.getString())
        dg.addUint16(otherCount)
        dg.appendData(otherPacker.getString())
        self.clientManager.air.send(dg)

    def enterSetAvatar(self):
        # Get the client channel.
        channel = self.clientManager.GetAccountConnectionChannel(self.target)

        # First, give them a POSTREMOVE to unload the avatar, just in case they
        # disconnect while we're working.
        datagramCleanup = PyDatagram()
        datagramCleanup.addServerHeader(
            self.avId,
            channel,
            STATESERVER_OBJECT_DELETE_RAM)
        datagramCleanup.addUint32(self.avId)
        datagram = PyDatagram()
        datagram.addServerHeader(
            channel,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_ADD_POST_REMOVE)
        datagram.addString(datagramCleanup.getMessage())
        self.clientManager.air.send(datagram)

        # We will now set the account's days since creation on the client.
        creationDate = self.getCreationDate()
        accountDays = -1

        if creationDate:
            now = datetime.fromtimestamp(time.mktime(time.strptime(time.ctime())))
            accountDays = abs((now - creationDate).days)

        if accountDays < 0:
            accountDays = 100000

        self.clientManager.sendUpdateToAccountId(self.target, 'receiveAccountDays', [accountDays])

        # Activate the avatar on the DBSS:
        self.clientManager.air.sendActivate(
            self.avId, 0, 0, self.clientManager.air.dclassesByName['DistributedToonUD'],
            {'setAccess': [OTPGlobals.AccessFull]})

       #  self.generateAvatar()

        # Next, add them to the avatar channel:
        datagram = PyDatagram()
        datagram.addServerHeader(
            channel,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_OPEN_CHANNEL)
        datagram.addChannel(self.clientManager.GetPuppetConnectionChannel(self.avId))
        self.clientManager.air.send(datagram)

        # We will now set the avatar as the client's session object.
        self.clientManager.air.clientAddSessionObject(channel, self.avId)

        # Now set their sender channel to represent their account affiliation:
        datagram = PyDatagram()
        datagram.addServerHeader(
            channel,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_SET_CLIENT_ID)
        datagram.addChannel(self.target << 32 | self.avId)
        self.clientManager.air.send(datagram)

        # We will now grant ownership.
        self.clientManager.air.setOwner(self.avId, channel)

        # Tell the friends manager that an avatar is coming online.
        friendsList = [x for x, y in self.avatar['setFriendsList'][0]]
        self.clientManager.air.toontownFriendsManager.comingOnline(self.avId, friendsList)

        # Now we'll assign a POST_REMOVE that will tell the friends manager
        # that an avatar has gone offline, in the event that they disconnect
        # unexpectedly.
        if self.clientManager.air.toontownFriendsManager:
            friendsManagerDclass = self.clientManager.air.toontownFriendsManager.dclass
            cleanupDatagram = friendsManagerDclass.aiFormatUpdate('goingOffline',
                                                                  self.clientManager.air.toontownFriendsManager.doId,
                                                                  self.clientManager.air.toontownFriendsManager.doId,
                                                                  self.clientManager.air.ourChannel, [self.avId])
        else:
            friendsManagerDoId = OtpDoGlobals.OTP_DO_ID_TOONTOWN_FRIENDS_MANAGER
            friendsManagerDclass = self.clientManager.air.dclassesByName['ToontownFriendsManagerUD']
            cleanupDatagram = friendsManagerDclass.aiFormatUpdate('goingOffline', friendsManagerDoId,
                                                                  friendsManagerDoId,
                                                                  self.clientManager.air.ourChannel, [self.avId])

        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.clientManager.air.ourChannel, CLIENTAGENT_ADD_POST_REMOVE)
        datagram.addString(cleanupDatagram.getMessage())
        self.clientManager.air.send(datagram)

        self.clientManager.air.writeServerEvent('avatarChosen', self.avId, self.target)
        self.demand('Off')

    def getCreationDate(self):
        # Based on game creation date:
        creationDate = self.account.get('CREATED', '')

        try:
            creationDate = datetime.fromtimestamp(time.mktime(time.strptime(creationDate)))
        except ValueError:
            creationDate = ''

        return creationDate

class UnloadAvatarFSM(OperationFSM):
    notify = directNotify.newCategory('UnloadAvatarFSM')

    def enterStart(self, avId):
        self.avId = avId

        # We don't even need to query the account, we know the avatar is being played!
        self.demand('UnloadAvatar')

    def enterUnloadAvatar(self):
        # Get the client channel.
        channel = self.clientManager.GetAccountConnectionChannel(self.target)

        # Tell the friends manager that we're logging off.
        self.clientManager.air.toontownFriendsManager.goingOffline(self.avId)

        # Clear off POSTREMOVE:
        datagram = PyDatagram()
        datagram.addServerHeader(
            channel,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_CLEAR_POST_REMOVES)
        self.clientManager.air.send(datagram)

        # Remove avatar channel:
        datagram = PyDatagram()
        datagram.addServerHeader(
            channel,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_CLOSE_CHANNEL)
        datagram.addChannel(self.clientManager.GetPuppetConnectionChannel(self.avId))
        self.clientManager.air.send(datagram)

        # Reset sender channel:
        datagram = PyDatagram()
        datagram.addServerHeader(
            channel,
            self.clientManager.air.ourChannel,
            CLIENTAGENT_SET_CLIENT_ID)
        datagram.addChannel(self.target << 32)
        self.clientManager.air.send(datagram)

        # Reset the session object.
        datagram = PyDatagram()
        datagram.addServerHeader(channel,
        self.clientManager.air.ourChannel,
        CLIENTAGENT_REMOVE_SESSION_OBJECT)
        datagram.addUint32(self.avId)
        self.clientManager.air.send(datagram)

        # Unload avatar object:
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.avId,
            channel,
            STATESERVER_OBJECT_DELETE_RAM)
        datagram.addUint32(self.avId)
        self.clientManager.air.send(datagram)

        # Done!
        self.clientManager.air.writeServerEvent('avatarUnload', self.avId)
        self.demand('Off')

# --- The actual UberDOG class itself. ---
class ClientManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('ClientManagerUD')

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

        # These keep track of the connection/account IDs currently undergoing an
        # operation on the ClientManager. This is to prevent (hacked) clients from firing up more
        # than one operation at a time, which could potentially lead to exploitation
        # of race conditions.
        self.connection2fsm = {}
        self.account2fsm = {}

        # For processing name patterns.
        self.nameGenerator = NameGenerator()

        # Temporary HMAC key:
        self.key = 'GXyYBRWZazyXWS2jpvqnFB7d54EUwUdB'

        # Instantiate our account DB interface:
        self.accountDB = AccountHandler(self)

    def killConnection(self, connId, reason):
        datagram = PyDatagram()
        datagram.addServerHeader(connId, self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(122)
        datagram.addString(reason)
        self.air.send(datagram)

    def killConnectionFSM(self, connId):
        fsm = self.connection2fsm.get(connId)

        if not fsm:
            self.notify.warning('Tried to kill connection %d for duplicate FSM, but none exists!' % connId)
            return

        self.killConnection(connId, 'An operation is already underway: ' + fsm.name)

    def killAccount(self, accountId, reason):
        self.killConnection(self.GetAccountConnectionChannel(accountId), reason)

    def killAccountFSM(self, accountId):
        fsm = self.account2fsm.get(accountId)
        if not fsm:

            self.notify.warning('Tried to kill account {0} for duplicate FSM, but none exists!'.format(accountId))
            return

        self.killAccount(accountId, 'An operation is already underway: ' + fsm.name)

    def runAccountFSM(self, fsmtype, *args):
        sender = self.air.getAccountIdFromSender()

        if not sender:
            self.killAccount(sender, 'Client is not logged in.')

        if sender in self.account2fsm:
            self.killAccountFSM(sender)
            return

        self.account2fsm[sender] = fsmtype(self, sender)
        self.account2fsm[sender].request('Start', *args)

    def login(self, cookie, authKey):
        self.notify.debug('Received login cookie %r from %d' % (cookie, self.air.getMsgSender()))

        sender = self.air.getMsgSender()

        # Time to check this login to see if its authentic
        digest_maker = hmac.new(self.key)
        digest_maker.update(cookie)
        serverKey = digest_maker.hexdigest()
        if serverKey == authKey:
            # This login is authentic!
            pass
        else:
            # This login is not authentic.
            self.killConnection(sender, ' ')

        if sender >> 32:
            self.killConnection(sender, 'Client is already logged in.')
            return

        if sender in self.connection2fsm:
            self.killConnectionFSM(sender)
            return

        self.connection2fsm[sender] = LoginAccountFSM(self, sender)
        self.connection2fsm[sender].request('Start', cookie)

    def requestAvatars(self):
        self.notify.debug('Received avatar list request from %d' % (self.air.getMsgSender()))
        self.runAccountFSM(GetAvatarsFSM)

    def createAvatar(self, dna, index):
        self.runAccountFSM(CreateAvatarFSM, dna, index)

    def deleteAvatar(self, avId):
        self.runAccountFSM(DeleteAvatarFSM, avId)

    def setNameTyped(self, avId, name):
        self.runAccountFSM(SetNameTypedFSM, avId, name)

    def setNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4):
        self.runAccountFSM(SetNamePatternFSM, avId, [(p1, f1), (p2, f2),
                                                     (p3, f3), (p4, f4)])

    def acknowledgeAvatarName(self, avId):
        self.runAccountFSM(AcknowledgeNameFSM, avId)

    def chooseAvatar(self, avId):
        currentAvId = self.air.getAvatarIdFromSender()
        accountId = self.air.getAccountIdFromSender()
        if currentAvId and avId:
            self.killAccount(accountId, 'A Toon is already chosen!')
            return
        elif not currentAvId and not avId:
            # This isn't really an error, the client is probably just making sure
            # none of its Toons are active.
            return

        if avId:
            self.runAccountFSM(LoadAvatarFSM, avId)
        else:
            self.runAccountFSM(UnloadAvatarFSM, currentAvId)
