# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/detailed_personal_efficiency_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/detailed_personal_efficiency_item_model.py
from frameworks.wulf import ViewModel

class DetailedPersonalEfficiencyItemModel(ViewModel):
    __slots__ = ()
    FORT_RUSH_SCORE = 'fortRushScore'
    KILLED = 'targetKills'
    SPOTTED = 'spotted'
    DAMAGE_DEALT = 'damageDealt'
    PIERCINGS = 'piercings'
    DAMAGE_ASSISTED = 'damageAssisted'
    CRITICAL_DAMAGE = 'critsCount'
    DAMAGE_BLOCKED_BY_ARMOR = 'damageBlockedByArmor'
    RICKOCHETS_RECEIVED = 'rickochetsReceived'
    NO_DAMAGE_DIRECT_HITS_RECIEVEVD = 'noDamageDirectHitsReceived'

    def __init__(self, properties=2, commands=0):
        super(DetailedPersonalEfficiencyItemModel, self).__init__(properties=properties, commands=commands)

    def getParamType(self):
        return self._getString(0)

    def setParamType(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(DetailedPersonalEfficiencyItemModel, self)._initialize()
        self._addStringProperty('paramType', '')
        self._addNumberProperty('value', 0)
