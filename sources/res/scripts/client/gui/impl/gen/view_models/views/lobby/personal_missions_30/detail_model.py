# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/detail_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/detail_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class DetailStatus(Enum):
    DONE = 'done'
    IN_PROGRESS = 'inProgress'
    NOT_RECEIVED = 'notReceived'
    DEFAULT = 'default'


class DetailModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DetailModel, self).__init__(properties=properties, commands=commands)

    def getStatus(self):
        return DetailStatus(self._getString(0))

    def setStatus(self, value):
        self._setString(0, value.value)

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)

    def getEarnedPoint(self):
        return self._getNumber(2)

    def setEarnedPoint(self, value):
        self._setNumber(2, value)

    def getHasAssemblingVideo(self):
        return self._getBool(3)

    def setHasAssemblingVideo(self, value):
        self._setBool(3, value)

    def getMaxPoint(self):
        return self._getNumber(4)

    def setMaxPoint(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(DetailModel, self)._initialize()
        self._addStringProperty('status')
        self._addStringProperty('id', '')
        self._addNumberProperty('earnedPoint', 0)
        self._addBoolProperty('hasAssemblingVideo', False)
        self._addNumberProperty('maxPoint', 0)
