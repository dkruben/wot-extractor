# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/alert_message_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/alert_message_model.py
from enum import Enum
from frameworks.wulf import Map, ViewModel

class AlertType(Enum):
    NONE = 'none'
    CEASEFIRECURRENTSERVER = 'ceasefireCurrentServer'
    CEASEFIREALLSERVERS = 'ceasefireAllServers'
    MODEISUNAVAILABLE = 'modeIsUnavailable'
    MODEISFINISHED = 'modeIsFinished'


class AlertMessageModel(ViewModel):
    __slots__ = ('onChangeServer', )

    def __init__(self, properties=2, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)

    def getAlertType(self):
        return AlertType(self._getString(0))

    def setAlertType(self, value):
        self._setString(0, value.value)

    def getBattleSchedule(self):
        return self._getMap(1)

    def setBattleSchedule(self, value):
        self._setMap(1, value)

    @staticmethod
    def getBattleScheduleType():
        return (unicode, unicode)

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty('alertType', AlertType.NONE.value)
        self._addMapProperty('battleSchedule', Map(unicode, unicode))
        self.onChangeServer = self._addCommand('onChangeServer')
