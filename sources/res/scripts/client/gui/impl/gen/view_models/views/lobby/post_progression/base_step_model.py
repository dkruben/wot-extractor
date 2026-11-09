# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/base_step_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/base_step_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ActionType(Enum):
    MODIFICATION = 'modification'
    PAIRMODIFICATION = 'pairModification'
    MODIFICATIONWITHFEATURE = 'modificationWithFeature'


class BaseStepModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BaseStepModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getActionType(self):
        return ActionType(self._getString(1))

    def setActionType(self, value):
        self._setString(1, value.value)

    def _initialize(self):
        super(BaseStepModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addStringProperty('actionType')
