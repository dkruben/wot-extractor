# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/new_operation_banner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/new_operation_banner.py
from enum import Enum
from frameworks.wulf import ViewModel

class BannerState(Enum):
    DEFAULT = 'default'
    COMPLETED_WITH_HONOR = 'completedWithHonor'
    COMPLETED = 'completed'


class NewOperationBanner(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NewOperationBanner, self).__init__(properties=properties, commands=commands)

    def getOperationId(self):
        return self._getNumber(0)

    def setOperationId(self, value):
        self._setNumber(0, value)

    def getBannerState(self):
        return BannerState(self._getString(1))

    def setBannerState(self, value):
        self._setString(1, value.value)

    def getFirstTimeEntrance(self):
        return self._getBool(2)

    def setFirstTimeEntrance(self, value):
        self._setBool(2, value)

    def getEnabled(self):
        return self._getBool(3)

    def setEnabled(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(NewOperationBanner, self)._initialize()
        self._addNumberProperty('operationId', 0)
        self._addStringProperty('bannerState', BannerState.DEFAULT.value)
        self._addBoolProperty('firstTimeEntrance', True)
        self._addBoolProperty('enabled', True)
