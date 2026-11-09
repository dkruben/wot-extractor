# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/sounds/halloween_sound_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/sounds/halloween_sound_controller.py
from __future__ import absolute_import
import BattleReplay, SoundGroups, WWISE
from constants import IS_CHINA, IS_CT
from gui.prb_control.entities.listener import IGlobalListener
from halloween.gui.sounds import playSound
from halloween.skeletons.halloween_sound_controller import IHalloweenSoundController
from halloween.skeletons.halloween_controller import IHalloweenController
from halloween.gui.sounds.sound_constants import SoundLanguage, HW_ENTER_EVENT, HW_EXIT_EVENT, HW_SOUND_REMAPPING, HW_RESET_HANGAR_MUSIC_EVENT
from helpers import dependency, getClientLanguage
from skeletons.gui.impl import IGuiLoader

class _StatusUpdateOperation(object):

    def execute(self):
        pass


class _StatusUpdateEvent(_StatusUpdateOperation):

    def __init__(self, event):
        self._event = event

    def execute(self):
        playSound(self._event)


class _StatusUpdateState(_StatusUpdateOperation):

    def __init__(self, group, value):
        self._group = group
        self._value = value

    def execute(self):
        WWISE.WW_setState(self._group, self._value)


_SOUNDS_WINDOW_STATUS_UPDATE = {}

def getEventVoiceoverLanguage():
    language = getClientLanguage()
    if language == SoundLanguage.LANGUAGE_UA:
        return SoundLanguage.VOICEOVER_UA
    if language == SoundLanguage.LANGUAGE_RU:
        return SoundLanguage.VOICEOVER_RU
    if IS_CHINA:
        return SoundLanguage.VOICEOVER_CN
    return SoundLanguage.VOICEOVER_EN


class HalloweenSoundController(IHalloweenSoundController, IGlobalListener):
    _guiLoader = dependency.descriptor(IGuiLoader)
    _hwController = dependency.descriptor(IHalloweenController)

    def __init__(self, *args, **kwargs):
        super(HalloweenSoundController, self).__init__(*args, **kwargs)
        self._hangarEnterEventPlayed = False

    def onAvatarBecomePlayer(self):
        if BattleReplay.g_replayCtrl.isPlaying:
            self.__setEventVoiceoverLanguage()

    def onLobbyInited(self, event):
        self._hangarEnterEventPlayed = False
        self.startGlobalListening()
        self._guiLoader.windowsManager.onWindowStatusChanged += self.__onWindowStatusChanged
        if self._hwController.isEventPrb():
            self._playEnter()

    def onAccountBecomePlayer(self):
        if IS_CT:
            WWISE.activateRemapping(HW_SOUND_REMAPPING)

    def onAccountBecomeNonPlayer(self):
        playSound(HW_RESET_HANGAR_MUSIC_EVENT)
        self.stopGlobalListening()
        self._guiLoader.windowsManager.onWindowStatusChanged -= self.__onWindowStatusChanged
        if IS_CT:
            WWISE.deactivateRemapping(HW_SOUND_REMAPPING)

    def onConnected(self):
        self.__setEventVoiceoverLanguage()

    def __setEventVoiceoverLanguage(self):
        language = getEventVoiceoverLanguage()
        SoundGroups.g_instance.setSwitch(SoundLanguage.VOICEOVER_LOCALIZATION_SWITCH, language)

    def onPrbEntitySwitched(self):
        if self._hwController.isEventPrb():
            self._playEnter()
        else:
            self._playExit()

    def playSoundEvent(self, audioEvent):
        playSound(audioEvent)

    def _playEnter(self):
        if not self._hangarEnterEventPlayed:
            self._hangarEnterEventPlayed = True
            playSound(HW_ENTER_EVENT)

    def _playExit(self):
        if self._hangarEnterEventPlayed:
            self._hangarEnterEventPlayed = False
            playSound(HW_EXIT_EVENT)

    def __onWindowStatusChanged(self, uniqueID, newStatus):
        window = self._guiLoader.windowsManager.getWindow(uniqueID)
        if not self._hwController.isEventPrb() or window is None or window.content is None:
            return
        content = window.content
        aliasOrLayoutID = getattr(content, 'alias') if hasattr(content, 'alias') else getattr(content, 'layoutID')
        sound = _SOUNDS_WINDOW_STATUS_UPDATE.get((aliasOrLayoutID, newStatus))
        if sound:
            sound.execute()
        return
