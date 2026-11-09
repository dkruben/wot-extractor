# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/server_info_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/server_info_model.py
from enum import Enum, IntEnum
from frameworks.wulf import ViewModel

class PingStatus(IntEnum):
    REQUESTED = 0
    HIGH = 1
    NORM = 2
    LOW = 3


class ColorBlindMode(Enum):
    DISABLED = 'disabled'
    PROTANOPIA = 'protanopia'


class ServerInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ServerInfoModel, self).__init__(properties=properties, commands=commands)

    def getServerName(self):
        return self._getString(0)

    def setServerName(self, value):
        self._setString(0, value)

    def getStatus(self):
        return PingStatus(self._getNumber(1))

    def setStatus(self, value):
        self._setNumber(1, value.value)

    def getColorBlind(self):
        return ColorBlindMode(self._getString(2))

    def setColorBlind(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(ServerInfoModel, self)._initialize()
        self._addStringProperty('serverName', '')
        self._addNumberProperty('status')
        self._addStringProperty('colorBlind')
