# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/battle/battle_page/ammunition_panel/ammunition_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/battle/battle_page/ammunition_panel/ammunition_panel.py
from __future__ import absolute_import
from gui.impl.battle.battle_page.ammunition_panel.groups_controller import PrebattleAmmunitionGroupsController
from gui.impl.common.ammunition_panel.base import BaseAmmunitionPanel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants

class PrebattleAmmunitionPanel(BaseAmmunitionPanel):

    def _createAmmunitionGroupsController(self, vehicle):
        return PrebattleAmmunitionGroupsController(vehicle, ctx=self._ctx)

    def onNextShellChanged(self, intCD):
        self._controller.onNextShellChanged(intCD)
        self.updateSection(TankSetupConstants.SHELLS)

    def onCurrentShellChanged(self, intCD):
        self._controller.onCurrentShellChanged(intCD)
        self.updateSection(TankSetupConstants.SHELLS)
