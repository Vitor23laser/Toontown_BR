from panda3d.core import ClockObject

from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify.DirectNotifyGlobal import directNotify

from otp.distributed.PotentialAvatar import PotentialAvatar
from otp.uberdog.AccountDetailRecord import AccountDetailRecord

from otp.otpbase import OTPGlobals

from datetime import datetime

from libotp import WhisperPopup

import simplejson as json
import time, hmac

class ClientManager(DistributedObject):
    notify = directNotify.newCategory('ClientManager')
    notify.setInfo(True)

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

        self.systemMessageSfx = None

    # --- LOGIN LOGIC ---
    def performLogin(self, doneEvent):
        self.doneEvent = doneEvent

        token = base.cr.playToken
        base.cr.userName = token

        key = 'GXyYBRWZazyXWS2jpvqnFB7d54EUwUdB'
        digest_maker = hmac.new(key)
        digest_maker.update(token)
        clientKey = digest_maker.hexdigest()
            
        self.sendUpdate('login', [token, clientKey])

    def acceptLogin(self, timestamp, responseBlob):
        responseData = json.loads(responseBlob)

        now = time.time()

        returnCode = responseData.get('returnCode')
        respString = responseData.get('respString')

        errorString = self.getExtendedErrorMsg(respString)

        accountNumber = responseData.get('accountNumber')
        self.cr.DISLIdFromLogin = accountNumber

        accountDetailRecord = AccountDetailRecord()

        self.cr.accountDetailRecord = accountDetailRecord

        createFriendsWithChat = responseData.get('createFriendsWithChat')

        canChat = createFriendsWithChat == 'YES' or createFriendsWithChat == 'CODE'
        self.cr.secretChatAllowed = canChat

        if base.logPrivateInfo:
            self.notify.info("CREATE_FRIENDS_WITH_CHAT from game server login: %s %s" % (createFriendsWithChat, canChat))

        chatCodeCreationRule = responseData.get('chatCodeCreationRule')

        if base.logPrivateInfo:
            self.notify.info("Chat code creation rule = %s" % chatCodeCreationRule)

        self.cr.chatChatCodeCreationRule = chatCodeCreationRule
        self.cr.secretChatNeedsParentPassword = chatCodeCreationRule == 'PARENT'

        serverTime = responseData.get('serverTime')

        self.cr.serverTimeUponLogin = serverTime
        self.cr.clientTimeUponLogin = now
        self.cr.globalClockRealTimeUponLogin = globalClock.getRealTime()

        if hasattr(self.cr, 'toontownTimeManager'):
            self.cr.toontownTimeManager.updateLoginTimes(serverTime, now, self.cr.globalClockRealTimeUponLogin)

        serverDelta = serverTime - now
        self.cr.setServerDelta(serverDelta)
        self.notify.setServerDelta(serverDelta, 28800)

        access = responseData.get('access')
        isPaid = access == 'FULL'
        self.cr.parentPasswordSet = isPaid
        self.cr.setIsPaid(isPaid)

        if isPaid:
            launcher.setPaidUserLoggedIn()

        if base.logPrivateInfo:
            self.notify.info("Paid from game server login: %s" % isPaid)

        WhiteListResponse = responseData.get('WhiteListResponse')

        if WhiteListResponse == 'YES':
            self.cr.whiteListChatEnabled = 1
        else:
            self.cr.whiteListChatEnabled = 0

        lastLoggedInStr = responseData.get('lastLoggedInStr')
        self.cr.lastLoggedIn = datetime.now()

        if hasattr(self.cr, 'toontownTimeManager'):
            self.cr.lastLoggedIn = self.cr.toontownTimeManager.convertStrToToontownTime(lastLoggedInStr)

        accountDaysFromServer = responseData.get('accountDays')

        if accountDaysFromServer is not None:
            self.cr.accountDays = self.parseAccountDays(accountDaysFromServer)
        else:
            self.cr.accountDays = 100000
        toonAccountType = responseData.get('toonAccountType')

        if toonAccountType == 'WITH_PARENT_ACCOUNT':
            self.cr.withParentAccount = True
        elif toonAccountType == 'NO_PARENT_ACCOUNT':
            self.cr.withParentAccount = False
        else:
            self.notify.error('unknown toon account type %s' % toonAccountType)
        if base.logPrivateInfo:
            self.notify.info("toonAccountType=%s" % toonAccountType)

        self.userName = responseData.get('userName')
        self.cr.userName = self.userName
        self.notify.info('Login response return code %s' % returnCode)

        if returnCode == 0:
            self.__handleLoginSuccess(timestamp)
        elif returnCode == -13:
            self.notify.info('Period Time Expired')
            messenger.send(self.doneEvent, [{'mode': 'reject'}])
        else:
            self.notify.info('Login failed: %s' % errorString)
            messenger.send(self.doneEvent, [{'mode': 'reject'}])

    def __handleLoginSuccess(self, timestamp):
        self.cr.logAccountInfo()
        launcher.setGoUserName(self.userName)
        launcher.setLastLogin(self.userName)
        launcher.setUserLoggedIn()

        if self.cr.loginInterface.freeTimeExpires == -1:
            launcher.setPaidUserLoggedIn()

        if self.cr.loginInterface.needToSetParentPassword():
            messenger.send(self.doneEvent, [{'mode': 'getChatPassword'}])
        else:
            messenger.send(self.doneEvent, [{'mode': 'success', 'timestamp': timestamp}])

    def getExtendedErrorMsg(self, errorString):
        prefix = 'Bad DC Version Compare'

        if len(errorString) < len(prefix):
            return errorString

        if errorString[:len(prefix)] == prefix:
            return '%s%s' % (errorString, ', address=%s' % self.cr.getServerAddress())

        return errorString

    def parseAccountDays(self, accountDays):
        result = 100000

        if accountDays >= 0:
            result = accountDays
        else:
            self.notify.warning('account days is negative %s' % accountDays)

        self.notify.debug('result=%s' % result)
        return result

    def receiveAccountDays(self, accountDays):
        base.cr.accountDays = accountDays

    # --- AVATARS LIST ---
    def requestAvatars(self):
        self.sendUpdate('requestAvatars')

    def setAvatars(self, avatars):
        avList = []
        for avNum, avName, avDNA, avPosition, nameState in avatars:
            nameOpen = int(nameState == 1)
            names = [avName, '', '', '']
            if nameState == 2: # PENDING
                names[1] = avName
            elif nameState == 3: # APPROVED
                names[2] = avName
            elif nameState == 4: # REJECTED
                names[3] = avName
            avList.append(PotentialAvatar(avNum, names, avDNA, avPosition, nameOpen))

        self.cr.handleAvatarsList(avList)

    # --- AVATAR CREATION/DELETION ---
    def sendCreateAvatar(self, avDNA, _, index):
        self.sendUpdate('createAvatar', [avDNA.makeNetString(), index])

    def createAvatarResp(self, avId):
        messenger.send('nameShopCreateAvatarDone', [avId])

    def sendDeleteAvatar(self, avId):
        self.sendUpdate('deleteAvatar', [avId])

    # No deleteAvatarResp; it just sends a setAvatars when the deed is done.

    def sendSetNameTyped(self, avId, name, callback):
        self._callback = callback
        self.sendUpdate('setNameTyped', [avId, name])

    def setNameTypedResp(self, avId, status):
        self._callback(avId, status)

    def sendSetNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4, callback):
        self._callback = callback
        self.sendUpdate('setNamePattern', [avId, p1, f1, p2, f2, p3, f3, p4, f4])

    def setNamePatternResp(self, avId, status):
        self._callback(avId, status)

    def sendAcknowledgeAvatarName(self, avId, callback):
        self._callback = callback
        self.sendUpdate('acknowledgeAvatarName', [avId])

    def acknowledgeAvatarNameResp(self):
        self._callback()

    # --- AVATAR CHOICE ---
    def sendChooseAvatar(self, avId):
        self.sendUpdate('chooseAvatar', [avId])

    def systemMessage(self, message):
        whisper = WhisperPopup(message, OTPGlobals.getInterfaceFont(), WTSystem)
        whisper.manage(base.marginManager)

        if self.systemMessageSfx is None:
            self.systemMessageSfx = base.loader.loadSfx('phase_3/audio/sfx/clock03.mp3')

        base.playSfx(self.systemMessageSfx)
