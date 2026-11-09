# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/death_cam_ui.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/death_cam_ui.py
from __future__ import absolute_import
import logging
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.battle.death_cam.death_cam_hud_view import DeathCamHudView
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext
_logger = logging.getLogger(__name__)

class DeathCamUI(InjectComponentAdaptor):
    __slots__ = ('__isArenaLoaded', '__isEnabledByServer')
    lobbyContext = dependency.descriptor(ILobbyContext)
    settingsCore = dependency.descriptor(ISettingsCore)

    def _onPopulate(self):
        self._updateInjectedViewState()

    def _makeInjectView(self):
        return DeathCamHudView()

    def __onSettingsChanged(self, diff):
        self._updateInjectedViewState()

    def _updateInjectedViewState(self):
        self._createInjectView()
