# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_panel_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/prebattle_ammunition_panel_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_ammunition_items_group import PrebattleAmmunitionItemsGroup
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_model import AmmunitionPanelModel

class PrebattleAmmunitionPanelModel(AmmunitionPanelModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=6):
        super(PrebattleAmmunitionPanelModel, self).__init__(properties=properties, commands=commands)

    def getSectionGroups(self):
        return self._getArray(6)

    def setSectionGroups(self, value):
        self._setArray(6, value)

    @staticmethod
    def getSectionGroupsType():
        return PrebattleAmmunitionItemsGroup

    def _initialize(self):
        super(PrebattleAmmunitionPanelModel, self)._initialize()
        self._addArrayProperty('sectionGroups', Array())
