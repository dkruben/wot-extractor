# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/alert_message_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/alert_message_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    NONE = 'none'
    NOVEHICLES = 'noVehicles'
    CEASEFIREAVAILABLE = 'ceasefireAvailable'
    CEASEFIREUNAVAILABLE = 'ceasefireUnavailable'
    MODEOFFLINE = 'modeOffline'


class AlertMessageModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=1, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty('state')
        self.onClick = self._addCommand('onClick')
