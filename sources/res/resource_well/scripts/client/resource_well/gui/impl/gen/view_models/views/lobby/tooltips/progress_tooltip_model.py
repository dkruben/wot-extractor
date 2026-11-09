# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/tooltips/progress_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/tooltips/progress_tooltip_model.py
from frameworks.wulf import ViewModel

class ProgressTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ProgressTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCurrentProgress(self):
        return self._getReal(0)

    def setCurrentProgress(self, value):
        self._setReal(0, value)

    def getProgressDiff(self):
        return self._getReal(1)

    def setProgressDiff(self, value):
        self._setReal(1, value)

    def getNeedShowDiff(self):
        return self._getBool(2)

    def setNeedShowDiff(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(ProgressTooltipModel, self)._initialize()
        self._addRealProperty('currentProgress', 0.0)
        self._addRealProperty('progressDiff', 0.0)
        self._addBoolProperty('needShowDiff', False)
