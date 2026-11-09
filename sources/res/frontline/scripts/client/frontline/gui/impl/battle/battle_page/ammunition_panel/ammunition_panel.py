# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/battle/battle_page/ammunition_panel/ammunition_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/battle/battle_page/ammunition_panel/ammunition_panel.py
from __future__ import absolute_import
from frontline.gui.impl.battle.battle_page.ammunition_panel.groups_controller import FLRespawnAmmunitionGroupsController
from gui.impl.common.ammunition_panel.base import BaseAmmunitionPanel

class FLRespawnAmmunitionPanel(BaseAmmunitionPanel):

    def _createAmmunitionGroupsController(self, vehicle):
        return FLRespawnAmmunitionGroupsController(vehicle, ctx=self._ctx)
