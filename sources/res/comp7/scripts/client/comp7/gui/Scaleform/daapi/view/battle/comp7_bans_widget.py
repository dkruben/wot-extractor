# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/battle/comp7_bans_widget.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/battle/comp7_bans_widget.py
from __future__ import absolute_import
import logging
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID
from comp7.gui.impl.battle.vehicle_ban.ban_widget import BanWidgetView
from constants import ARENA_PERIOD
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)

class Comp7BansWidget(InjectComponentAdaptor):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _onPopulate(self):
        vehicleBanCtrl = self.__sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.COMP7_VEHICLE_BAN_CTRL)
        if vehicleBanCtrl is None or not vehicleBanCtrl.isVehicleBanEnabled:
            return
        if self.__sessionProvider.arenaVisitor.getArenaPeriod() == ARENA_PERIOD.BATTLE:
            return
        else:
            self._createInjectView()
            return

    def _makeInjectView(self):
        return BanWidgetView()
