# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/battle_results/comp7_light_player_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/battle_results/comp7_light_player_model.py
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_stats_efficiency_model import Comp7LightStatsEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_player_model import RandomPlayerModel

class Comp7LightPlayerModel(RandomPlayerModel):
    __slots__ = ()
    NO_PLATOON_SQUAD_INDEX = 0
    SUPER_PLATOON_SQUAD_INDEX = -1

    def __init__(self, properties=14, commands=0):
        super(Comp7LightPlayerModel, self).__init__(properties=properties, commands=commands)

    @property
    def efficiencyValues(self):
        return self._getViewModel(13)

    @staticmethod
    def getEfficiencyValuesType():
        return Comp7LightStatsEfficiencyModel

    def _initialize(self):
        super(Comp7LightPlayerModel, self)._initialize()
        self._addViewModelProperty('efficiencyValues', Comp7LightStatsEfficiencyModel())
