# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/tooltips/critical_damage_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/tooltips/critical_damage_tooltip_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.critical_damage_group_model import CriticalDamageGroupModel

class CriticalDamageTooltipModel(ViewModel):
    __slots__ = ()
    CRITICAL_DAMAGE = 'criticalDamage'

    def __init__(self, properties=2, commands=0):
        super(CriticalDamageTooltipModel, self).__init__(properties=properties, commands=commands)

    def getParamType(self):
        return self._getString(0)

    def setParamType(self, value):
        self._setString(0, value)

    def getDetails(self):
        return self._getArray(1)

    def setDetails(self, value):
        self._setArray(1, value)

    @staticmethod
    def getDetailsType():
        return CriticalDamageGroupModel

    def _initialize(self):
        super(CriticalDamageTooltipModel, self)._initialize()
        self._addStringProperty('paramType', '')
        self._addArrayProperty('details', Array())
