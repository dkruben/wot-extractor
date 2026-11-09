# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/battle_results/fun_stats_efficiency_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/battle_results/fun_stats_efficiency_model.py
from frameworks.wulf import Map, ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_stats_efficiency_param_model import FunStatsEfficiencyParamModel

class FunStatsEfficiencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FunStatsEfficiencyModel, self).__init__(properties=properties, commands=commands)

    def getParameters(self):
        return self._getMap(0)

    def setParameters(self, value):
        self._setMap(0, value)

    @staticmethod
    def getParametersType():
        return (unicode, FunStatsEfficiencyParamModel)

    def _initialize(self):
        super(FunStatsEfficiencyModel, self)._initialize()
        self._addMapProperty('parameters', Map(unicode, FunStatsEfficiencyParamModel))
