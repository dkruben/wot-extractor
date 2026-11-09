# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/tooltips/fixed_rewards_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/tooltips/fixed_rewards_tooltip_model.py
from frameworks.wulf import Array, ViewModel
from open_bundle.gui.impl.gen.view_models.views.lobby.tooltips.step_model import StepModel

class FixedRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FixedRewardsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getBundleType(self):
        return self._getString(0)

    def setBundleType(self, value):
        self._setString(0, value)

    def getSteps(self):
        return self._getArray(1)

    def setSteps(self, value):
        self._setArray(1, value)

    @staticmethod
    def getStepsType():
        return StepModel

    def _initialize(self):
        super(FixedRewardsTooltipModel, self)._initialize()
        self._addStringProperty('bundleType', '')
        self._addArrayProperty('steps', Array())
