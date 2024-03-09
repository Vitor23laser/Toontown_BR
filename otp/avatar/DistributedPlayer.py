# File: D (Python 2.4)

from pandac.PandaModules import *
from libotp import WhisperPopup
from libotp import CFQuicktalker, CFPageButton, CFQuitButton, CFSpeech, CFThought, CFTimeout
from otp.chat import ChatGarbler
import string
from direct.task import Task
from otp.otpbase import OTPLocalizer
from otp.speedchat import SCDecoders
from direct.showbase import PythonUtil
from otp.avatar import DistributedAvatar
import time
from otp.avatar import Avatar, PlayerBase
from otp.chat import TalkAssistant
from otp.otpbase import OTPGlobals
if base.config.GetBool('want-chatfilter-hacks', 0):
    from otp.switchboard import badwordpy
    import os
    badwordpy.init(os.environ.get('OTP') + '\\src\\switchboard\\', '')


class DistributedPlayer(DistributedAvatar.DistributedAvatar, PlayerBase.PlayerBase):
    TeleportFailureTimeout = 60.0
    chatGarbler = ChatGarbler.ChatGarbler()
    
    def __init__(self, cr):
        
        try:
            pass
        except:
            self.DistributedPlayer_initialized = 1
            DistributedAvatar.DistributedAvatar.__init__(self, cr)
            PlayerBase.PlayerBase.__init__(self)
            self._DistributedPlayer__teleportAvailable = 0
            self.inventory = None
            self.experience = None
            self.friendsList = []
            self.oldFriendsList = None
            self.timeFriendsListChanged = None
            self.ignoreList = []
            self.lastFailedTeleportMessage = { }
            self._districtWeAreGeneratedOn = None
            self.DISLname = ''
            self.DISLid = 0
            self.autoRun = 0
            self.whiteListEnabled = base.config.GetBool('whitelist-chat-enabled', 1)


    
    def disable(self):
        DistributedAvatar.DistributedAvatar.disable(self)

    
    def delete(self):
        
        try:
            pass
        except:
            self.DistributedPlayer_deleted = 1
            del self.experience
            if self.inventory:
                self.inventory.unload()
            
            del self.inventory
            DistributedAvatar.DistributedAvatar.delete(self)


    
    def generate(self):
        DistributedAvatar.DistributedAvatar.generate(self)

    
    def setLocation(self, parentId, zoneId, teleport = 0):
        DistributedAvatar.DistributedAvatar.setLocation(self, parentId, zoneId, teleport)
        if not parentId in (0, None) and zoneId in (0, None):
            if not self.cr._isValidPlayerLocation(parentId, zoneId):
                self.cr.disableDoId(self.doId)
                self.cr.deleteObject(self.doId)
            
        

    
    def isGeneratedOnDistrict(self, districtId = None):
        if districtId is None:
            return self._districtWeAreGeneratedOn is not None
        else:
            return self._districtWeAreGeneratedOn == districtId

    
    def getArrivedOnDistrictEvent(self, districtId = None):
        if districtId is None:
            return 'arrivedOnDistrict'
        else:
            return 'arrivedOnDistrict-%s' % districtId

    
    def arrivedOnDistrict(self, districtId):
        curFrameTime = globalClock.getFrameTime()
        if hasattr(self, 'frameTimeWeArrivedOnDistrict') and curFrameTime == self.frameTimeWeArrivedOnDistrict:
            if districtId == 0 and self._districtWeAreGeneratedOn:
                self.notify.warning('ignoring arrivedOnDistrict 0, since arrivedOnDistrict %d occured on the same frame' % self._districtWeAreGeneratedOn)
                return None
            
        
        self._districtWeAreGeneratedOn = districtId
        self.frameTimeWeArrivedOnDistrict = globalClock.getFrameTime()
        messenger.send(self.getArrivedOnDistrictEvent(districtId))
        messenger.send(self.getArrivedOnDistrictEvent())

    
    def setLeftDistrict(self):
        self._districtWeAreGeneratedOn = None

    
    def hasParentingRules(self):
        if self is localAvatar:
            return True
        

    
    def setAccountName(self, accountName):
        self.accountName = accountName

    
    def setSystemMessage(self, aboutId, chatString, whisperType = WhisperPopup.WTSystem):
        self.displayWhisper(aboutId, chatString, whisperType)

    
    def displayWhisper(self, fromId, chatString, whisperType):
        print 'Whisper type %s from %s: %s' % (whisperType, fromId, chatString)

    
    def displayWhisperPlayer(self, playerId, chatString, whisperType):
        print 'WhisperPlayer type %s from %s: %s' % (whisperType, playerId, chatString)

    
    def whisperSCTo(self, msgIndex, sendToId, toPlayer):
        if toPlayer:
            base.cr.playerFriendsManager.sendSCWhisper(sendToId, msgIndex)
        else:
            messenger.send('wakeup')
            self.sendUpdate('setWhisperSCFrom', [
                self.doId,
                msgIndex], sendToId)

    
    def setWhisperSCFrom(self, fromId, msgIndex):
        handle = base.cr.identifyAvatar(fromId)
        if handle == None:
            return None
        
        if base.cr.avatarFriendsManager.checkIgnored(fromId):
            self.d_setWhisperIgnored(fromId)
            return None
        
        if fromId in self.ignoreList:
            self.d_setWhisperIgnored(fromId)
            return None
        
        chatString = SCDecoders.decodeSCStaticTextMsg(msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTQuickTalker)
            base.talkAssistant.receiveAvatarWhisperSpeedChat(TalkAssistant.SPEEDCHAT_NORMAL, msgIndex, fromId)
        

    
    def whisperSCCustomTo(self, msgIndex, sendToId, toPlayer):
        if toPlayer:
            base.cr.playerFriendsManager.sendSCCustomWhisper(sendToId, msgIndex)
            return None
        
        messenger.send('wakeup')
        self.sendUpdate('setWhisperSCCustomFrom', [
            self.doId,
            msgIndex], sendToId)

    
    def _isValidWhisperSource(self, source):
        return True

    
    def setWhisperSCCustomFrom(self, fromId, msgIndex):
        handle = base.cr.identifyAvatar(fromId)
        if handle == None:
            return None
        
        if not self._isValidWhisperSource(handle):
            self.notify.warning('displayWhisper from non-toon %s' % fromId)
            return None
        
        if base.cr.avatarFriendsManager.checkIgnored(fromId):
            self.d_setWhisperIgnored(fromId)
            return None
        
        if fromId in self.ignoreList:
            self.d_setWhisperIgnored(fromId)
            return None
        
        chatString = SCDecoders.decodeSCCustomMsg(msgIndex)
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTQuickTalker)
            base.talkAssistant.receiveAvatarWhisperSpeedChat(TalkAssistant.SPEEDCHAT_CUSTOM, msgIndex, fromId)
        

    
    def whisperSCEmoteTo(self, emoteId, sendToId, toPlayer):
        print 'whisperSCEmoteTo %s %s %s' % (emoteId, sendToId, toPlayer)
        if toPlayer:
            base.cr.playerFriendsManager.sendSCEmoteWhisper(sendToId, emoteId)
            return None
        
        messenger.send('wakeup')
        self.sendUpdate('setWhisperSCEmoteFrom', [
            self.doId,
            emoteId], sendToId)

    
    def setWhisperSCEmoteFrom(self, fromId, emoteId):
        handle = base.cr.identifyAvatar(fromId)
        if handle == None:
            return None
        
        if base.cr.avatarFriendsManager.checkIgnored(fromId):
            self.d_setWhisperIgnored(fromId)
            return None
        
        chatString = SCDecoders.decodeSCEmoteWhisperMsg(emoteId, handle.getName())
        if chatString:
            self.displayWhisper(fromId, chatString, WhisperPopup.WTEmote)
            base.talkAssistant.receiveAvatarWhisperSpeedChat(TalkAssistant.SPEEDCHAT_EMOTE, emoteId, fromId)
        

    
    def d_setWhisperIgnored(self, sendToId):
        pass

    
    def setChatAbsolute(self, chatString, chatFlags, dialogue = None, interrupt = 1, quiet = 0):
        DistributedAvatar.DistributedAvatar.setChatAbsolute(self, chatString, chatFlags, dialogue, interrupt)
        if not quiet:
            pass
        1

    
    def b_setChat(self, chatString, chatFlags):
        if self.cr.wantMagicWords and len(chatString) > 0 and chatString[0] == '~':
            messenger.send('magicWord', [
                chatString])
        elif base.config.GetBool('want-chatfilter-hacks', 0):
            if base.config.GetBool('want-chatfilter-drop-offending', 0):
                if badwordpy.test(chatString):
                    return None
                
            else:
                chatString = badwordpy.scrub(chatString)
        
        messenger.send('wakeup')
        self.setChatAbsolute(chatString, chatFlags)
        self.d_setChat(chatString, chatFlags)

    
    def d_setChat(self, chatString, chatFlags):
        self.sendUpdate('setChat', [
            chatString,
            chatFlags,
            0])

    
    def setTalk(self, fromAV, fromAC, avatarName, chat, mods, flags):
        (newText, scrubbed) = self.scrubTalk(chat, mods)
        self.displayTalk(newText)
        if base.talkAssistant.isThought(newText):
            newText = base.talkAssistant.removeThoughtPrefix(newText)
            base.talkAssistant.receiveThought(fromAV, avatarName, fromAC, None, newText, scrubbed)
        else:
            base.talkAssistant.receiveOpenTalk(fromAV, avatarName, fromAC, None, newText, scrubbed)

    
    def setTalkWhisper(self, fromAV, fromAC, avatarName, chat, mods, flags):
        (newText, scrubbed) = self.scrubTalk(chat, mods)
        self.displayTalkWhisper(fromAV, avatarName, chat, mods)
        base.talkAssistant.receiveWhisperTalk(fromAV, avatarName, fromAC, None, self.doId, self.getName(), newText, scrubbed)

    
    def displayTalkWhisper(self, fromId, avatarName, chatString, mods):
        print 'TalkWhisper from %s: %s' % (fromId, chatString)

    
    def scrubTalk(self, chat, mods):
        return chat

    
    def setChat(self, chatString, chatFlags, DISLid):
        self.notify.error('Should call setTalk')
        chatString = base.talkAssistant.whiteListFilterMessage(chatString)
        if base.cr.avatarFriendsManager.checkIgnored(self.doId):
            return None
        
        if base.localAvatar.garbleChat and not self.isUnderstandable():
            chatString = self.chatGarbler.garble(self, chatString)
        
        chatFlags &= ~(CFQuicktalker | CFPageButton | CFQuitButton)
        if chatFlags & CFThought:
            chatFlags &= ~(CFSpeech | CFTimeout)
        else:
            chatFlags |= CFSpeech | CFTimeout
        self.setChatAbsolute(chatString, chatFlags)

    
    def b_setSC(self, msgIndex):
        self.setSC(msgIndex)
        self.d_setSC(msgIndex)

    
    def d_setSC(self, msgIndex):
        messenger.send('wakeup')
        self.sendUpdate('setSC', [
            msgIndex])

    
    def setSC(self, msgIndex):
        if base.cr.avatarFriendsManager.checkIgnored(self.doId):
            return None
        
        if self.doId in base.localAvatar.ignoreList:
            return None
        
        chatString = SCDecoders.decodeSCStaticTextMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout, quiet = 1)
        
        base.talkAssistant.receiveOpenSpeedChat(TalkAssistant.SPEEDCHAT_NORMAL, msgIndex, self.doId)

    
    def b_setSCCustom(self, msgIndex):
        self.setSCCustom(msgIndex)
        self.d_setSCCustom(msgIndex)

    
    def d_setSCCustom(self, msgIndex):
        messenger.send('wakeup')
        self.sendUpdate('setSCCustom', [
            msgIndex])

    
    def setSCCustom(self, msgIndex):
        if base.cr.avatarFriendsManager.checkIgnored(self.doId):
            return None
        
        if self.doId in base.localAvatar.ignoreList:
            return None
        
        chatString = SCDecoders.decodeSCCustomMsg(msgIndex)
        if chatString:
            self.setChatAbsolute(chatString, CFSpeech | CFQuicktalker | CFTimeout)
        
        base.talkAssistant.receiveOpenSpeedChat(TalkAssistant.SPEEDCHAT_CUSTOM, msgIndex, self.doId)

    
    def b_setSCEmote(self, emoteId):
        self.b_setEmoteState(emoteId, animMultiplier = self.animMultiplier)

    
    def d_friendsNotify(self, avId, status):
        self.sendUpdate('friendsNotify', [
            avId,
            status])

    
    def friendsNotify(self, avId, status):
        avatar = base.cr.identifyFriend(avId)
        if avatar != None:
            if status == 1:
                self.setSystemMessage(avId, OTPLocalizer.WhisperNoLongerFriend % avatar.getName())
            elif status == 2:
                self.setSystemMessage(avId, OTPLocalizer.WhisperNowSpecialFriend % avatar.getName())
            
        

    
    def d_teleportQuery(self, requesterId, sendToId = None):
        self.sendUpdate('teleportQuery', [
            requesterId], sendToId)

    
    def teleportQuery(self, requesterId):
        avatar = base.cr.playerFriendsManager.identifyFriend(requesterId)
        if avatar != None:
            if base.cr.avatarFriendsManager.checkIgnored(requesterId):
                self.d_teleportResponse(self.doId, 2, 0, 0, 0, sendToId = requesterId)
                return None
            
            if requesterId in self.ignoreList:
                self.d_teleportResponse(self.doId, 2, 0, 0, 0, sendToId = requesterId)
                return None
            
            if hasattr(base, 'distributedParty'):
                if base.distributedParty.partyInfo.isPrivate:
                    if requesterId not in base.distributedParty.inviteeIds:
                        self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId = requesterId)
                        return None
                    
                
                if base.distributedParty.isPartyEnding:
                    self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId = requesterId)
                    return None
                
            
            if self._DistributedPlayer__teleportAvailable and not (self.ghostMode) and base.config.GetBool('can-be-teleported-to', 1):
                self.setSystemMessage(requesterId, OTPLocalizer.WhisperComingToVisit % avatar.getName())
                messenger.send('teleportQuery', [
                    avatar,
                    self])
                return None
            
            if self.failedTeleportMessageOk(requesterId):
                self.setSystemMessage(requesterId, OTPLocalizer.WhisperFailedVisit % avatar.getName())
            
        
        self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId = requesterId)

    
    def failedTeleportMessageOk(self, fromId):
        now = globalClock.getFrameTime()
        lastTime = self.lastFailedTeleportMessage.get(fromId, None)
        if lastTime != None:
            elapsed = now - lastTime
            if elapsed < self.TeleportFailureTimeout:
                return 0
            
        
        self.lastFailedTeleportMessage[fromId] = now
        return 1

    
    def d_teleportResponse(self, avId, available, shardId, hoodId, zoneId, sendToId = None):
        self.sendUpdate('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId], sendToId)

    
    def teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        messenger.send('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId])

    
    def d_teleportGiveup(self, requesterId, sendToId = None):
        self.sendUpdate('teleportGiveup', [
            requesterId], sendToId)

    
    def teleportGiveup(self, requesterId):
        avatar = base.cr.identifyAvatar(requesterId)
        if not self._isValidWhisperSource(avatar):
            self.notify.warning('teleportGiveup from non-toon %s' % requesterId)
            return None
        
        if avatar != None:
            self.setSystemMessage(requesterId, OTPLocalizer.WhisperGiveupVisit % avatar.getName())
        

    
    def b_teleportGreeting(self, avId):
        self.d_teleportGreeting(avId)
        self.teleportGreeting(avId)

    
    def d_teleportGreeting(self, avId):
        self.sendUpdate('teleportGreeting', [
            avId])

    
    def teleportGreeting(self, avId):
        avatar = base.cr.getDo(avId)
        if isinstance(avatar, Avatar.Avatar):
            self.setChatAbsolute(OTPLocalizer.TeleportGreeting % avatar.getName(), CFSpeech | CFTimeout)
        elif avatar is not None:
            self.notify.warning('got teleportGreeting from %s referencing non-toon %s' % (self.doId, avId))
        

    
    def setTeleportAvailable(self, available):
        self._DistributedPlayer__teleportAvailable = available

    
    def getTeleportAvailable(self):
        return self._DistributedPlayer__teleportAvailable

    
    def getFriendsList(self):
        return self.friendsList

    
    def setFriendsList(self, friendsList):
        self.oldFriendsList = self.friendsList
        self.friendsList = friendsList
        self.timeFriendsListChanged = globalClock.getFrameTime()
        messenger.send('friendsListChanged')
        Avatar.reconsiderAllUnderstandable()

    
    def setDISLname(self, name):
        self.DISLname = name

    
    def setDISLid(self, id):
        self.DISLid = id

    
    def setAutoRun(self, value):
        self.autoRun = value

    
    def getAutoRun(self):
        return self.autoRun


