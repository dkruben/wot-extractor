# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/fl_hangar_ammunition_groups_controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/presenters/fl_hangar_ammunition_groups_controller.py
from __future__ import absolute_import
from constants import PREBATTLE_TYPE, QUEUE_TYPE
from frontline.constants.common import FRONTLINE_GROUPS
from gui.impl.lobby.tank_setup.ammunition_panel.groups_controller import HangarAmmunitionGroupsController
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController

class FLHangarAmmunitionGroupsController(HangarAmmunitionGroupsController):
    __slots__ = ()
    __epicMetaGameCtrl = dependency.descriptor(IEpicBattleMetaGameController)

    def _getGroups(self):
        if self._vehicle is None:
            return []
        else:
            if self.prbDispatcher is not None and (self.prbDispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.EPIC) or self.prbDispatcher.getFunctionalState().isInUnit(PREBATTLE_TYPE.EPIC)) and self._vehicle.level in self.__epicMetaGameCtrl.getValidVehicleLevels():
                return FRONTLINE_GROUPS
            return super(FLHangarAmmunitionGroupsController, self)._getGroups()
