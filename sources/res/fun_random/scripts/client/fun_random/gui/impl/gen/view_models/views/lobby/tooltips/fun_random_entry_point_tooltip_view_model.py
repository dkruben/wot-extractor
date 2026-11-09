# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/tooltips/fun_random_entry_point_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/tooltips/fun_random_entry_point_tooltip_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import ModePerformanceModel

class FunRandomEntryPointTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FunRandomEntryPointTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def performance(self):
        return self._getViewModel(0)

    @staticmethod
    def getPerformanceType():
        return ModePerformanceModel

    def getAssetsPointer(self):
        return self._getString(1)

    def setAssetsPointer(self, value):
        self._setString(1, value)

    def getModeState(self):
        return self._getString(2)

    def setModeState(self, value):
        self._setString(2, value)

    def getStartTime(self):
        return self._getNumber(3)

    def setStartTime(self, value):
        self._setNumber(3, value)

    def getLeftTime(self):
        return self._getNumber(4)

    def setLeftTime(self, value):
        self._setNumber(4, value)

    def getEndTime(self):
        return self._getNumber(5)

    def setEndTime(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(FunRandomEntryPointTooltipViewModel, self)._initialize()
        self._addViewModelProperty('performance', ModePerformanceModel())
        self._addStringProperty('assetsPointer', 'undefined')
        self._addStringProperty('modeState', '')
        self._addNumberProperty('startTime', 0)
        self._addNumberProperty('leftTime', 0)
        self._addNumberProperty('endTime', 0)
