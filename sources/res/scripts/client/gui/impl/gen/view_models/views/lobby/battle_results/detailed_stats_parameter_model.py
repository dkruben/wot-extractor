# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/detailed_stats_parameter_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/detailed_stats_parameter_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import SimpleStatsParameterModel

class DetailedStatsParameterModel(SimpleStatsParameterModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DetailedStatsParameterModel, self).__init__(properties=properties, commands=commands)

    def getDetails(self):
        return self._getArray(4)

    def setDetails(self, value):
        self._setArray(4, value)

    @staticmethod
    def getDetailsType():
        return SimpleStatsParameterModel

    def _initialize(self):
        super(DetailedStatsParameterModel, self)._initialize()
        self._addArrayProperty('details', Array())
