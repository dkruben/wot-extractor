# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/manual/manual_view_base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/manual/manual_view_base.py
from __future__ import absolute_import
import logging
from gui.Scaleform.framework.entities.View import View
from helpers import dependency
from skeletons.gui.game_control import IManualController
from skeletons.gui.lobby_context import ILobbyContext
from gui.sounds.filters import States, StatesGroup
from sound_gui_manager import CommonSoundSpaceSettings
_logger = logging.getLogger(__name__)

class ManualViewBase(View):
    lobbyContext = dependency.descriptor(ILobbyContext)
    manualController = dependency.descriptor(IManualController)
    SOUND_SPACE = 'manual'
    SOUND_STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_MENU_GUIDE = 'STATE_hangar_place_menu_guide'
    STATE_PLACE_GARAGE = 'STATE_hangar_place_garage'
    BC_HANGAR_MUSIC_GUIDE_ENTER_SOUND_ID = 'bc_hangar_music_guide_enter'
    BC_HANGAR_MUSIC_GUIDE_EXIT_SOUND_ID = 'bc_hangar_music_guide_exit'
    _COMMON_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUND_SPACE, entranceStates={SOUND_STATE_PLACE: STATE_PLACE_MENU_GUIDE, (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_OFF)}, exitStates={SOUND_STATE_PLACE: STATE_PLACE_GARAGE}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=BC_HANGAR_MUSIC_GUIDE_ENTER_SOUND_ID, exitEvent=BC_HANGAR_MUSIC_GUIDE_EXIT_SOUND_ID)

    def __init__(self, ctx=None):
        super(ManualViewBase, self).__init__()
        self._ctx = ctx
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        self.chaptersUIData = self.manualController.getChaptersUIData()

    def closeView(self):
        raise NotImplementedError

    def _close(self):
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        self.destroy()

    def __onServerSettingChanged(self, diff):
        if 'isManualEnabled' in diff:
            if not bool(diff['isManualEnabled']):
                self.closeView()
