# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/param_value_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/sub_views/param_value_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class MechanicState(Enum):
    DEFAULT = ''
    ON = 'on'
    OFF = 'off'


class ParamValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ParamValueModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)

    def getMechanic(self):
        return self._getString(1)

    def setMechanic(self, value):
        self._setString(1, value)

    def getState(self):
        return MechanicState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(ParamValueModel, self)._initialize()
        self._addStringProperty('value', '')
        self._addStringProperty('mechanic', '')
        self._addStringProperty('state')
