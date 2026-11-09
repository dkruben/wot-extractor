# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_grid_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_grid_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel

class PostProgressionGridModel(ViewModel):
    __slots__ = ('onMainStepActionClick', 'onMainStepSelectClick', 'onMultiStepActionClick',
                 'onMultiStepSelectClick', 'onPrebattleSwitchToggleClick')

    def __init__(self, properties=3, commands=5):
        super(PostProgressionGridModel, self).__init__(properties=properties, commands=commands)

    def getMainSelectedIdx(self):
        return self._getNumber(0)

    def setMainSelectedIdx(self, value):
        self._setNumber(0, value)

    def getMainSteps(self):
        return self._getArray(1)

    def setMainSteps(self, value):
        self._setArray(1, value)

    @staticmethod
    def getMainStepsType():
        return SingleStepModel

    def getMultiSteps(self):
        return self._getArray(2)

    def setMultiSteps(self, value):
        self._setArray(2, value)

    @staticmethod
    def getMultiStepsType():
        return MultiStepModel

    def _initialize(self):
        super(PostProgressionGridModel, self)._initialize()
        self._addNumberProperty('mainSelectedIdx', -1)
        self._addArrayProperty('mainSteps', Array())
        self._addArrayProperty('multiSteps', Array())
        self.onMainStepActionClick = self._addCommand('onMainStepActionClick')
        self.onMainStepSelectClick = self._addCommand('onMainStepSelectClick')
        self.onMultiStepActionClick = self._addCommand('onMultiStepActionClick')
        self.onMultiStepSelectClick = self._addCommand('onMultiStepSelectClick')
        self.onPrebattleSwitchToggleClick = self._addCommand('onPrebattleSwitchToggleClick')
