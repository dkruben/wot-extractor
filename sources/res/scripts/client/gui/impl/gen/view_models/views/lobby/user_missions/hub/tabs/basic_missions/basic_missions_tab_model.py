# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/basic_missions_tab_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/basic_missions_tab_model.py
from frameworks.wulf import ViewModel

class BasicMissionsTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BasicMissionsTabModel, self).__init__(properties=properties, commands=commands)

    def getIsDailySectionAvailable(self):
        return self._getBool(0)

    def setIsDailySectionAvailable(self, value):
        self._setBool(0, value)

    def getIsWeeklySectionAvailable(self):
        return self._getBool(1)

    def setIsWeeklySectionAvailable(self, value):
        self._setBool(1, value)

    def getIsPMSectionAvailable(self):
        return self._getBool(2)

    def setIsPMSectionAvailable(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(BasicMissionsTabModel, self)._initialize()
        self._addBoolProperty('isDailySectionAvailable', False)
        self._addBoolProperty('isWeeklySectionAvailable', False)
        self._addBoolProperty('isPMSectionAvailable', False)
