# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/common/anomaly_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/common/anomaly_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class AnomalyType(Enum):
    REGULAR = 'regular'
    EPIC = 'epic'
    INDIVIDUAL = 'individual'
    SECRET = 'secret'


class AnomalyState(Enum):
    UNKNOWN = 'unknown'
    KNOWN = 'known'
    AVAILABLE = 'available'
    ACQUIRED = 'acquired'
    NEW = 'new'


class AnomalyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AnomalyModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getType(self):
        return AnomalyType(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)

    def getState(self):
        return AnomalyState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(AnomalyModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('type')
        self._addStringProperty('state')
