# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/compare_step_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/compare_step_model.py
from gui.impl.gen.view_models.views.lobby.post_progression.base_step_model import BaseStepModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_modification_model import CompareModificationModel

class CompareStepModel(BaseStepModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CompareStepModel, self).__init__(properties=properties, commands=commands)

    @property
    def modification(self):
        return self._getViewModel(2)

    @staticmethod
    def getModificationType():
        return CompareModificationModel

    def getIsInstalled(self):
        return self._getBool(3)

    def setIsInstalled(self, value):
        self._setBool(3, value)

    def getLevel(self):
        return self._getNumber(4)

    def setLevel(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(CompareStepModel, self)._initialize()
        self._addViewModelProperty('modification', CompareModificationModel())
        self._addBoolProperty('isInstalled', False)
        self._addNumberProperty('level', 0)
