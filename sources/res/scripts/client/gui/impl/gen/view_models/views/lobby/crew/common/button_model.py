# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/button_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/button_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ButtonType(Enum):
    CREWOPERATIONS = 'crewOperations'
    CREWBOOKS = 'crewBooks'
    ACCELERATEDTRAINING = 'acceleratedTraining'
    WOTPLUS = 'wotPlus'


class ButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ButtonModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return ButtonType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(ButtonModel, self)._initialize()
        self._addStringProperty('type')
