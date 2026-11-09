# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/header_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/header_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ModeStatus(Enum):
    ALERT = 'alert'
    BATTLESELECTOR = 'battleSelector'


class HeaderModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(HeaderModel, self).__init__(properties=properties, commands=commands)

    def getModeStatus(self):
        return ModeStatus(self._getString(0))

    def setModeStatus(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(HeaderModel, self)._initialize()
        self._addStringProperty('modeStatus', ModeStatus.BATTLESELECTOR.value)
