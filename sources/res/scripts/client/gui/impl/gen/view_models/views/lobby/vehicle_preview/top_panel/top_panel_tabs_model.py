# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/top_panel/top_panel_tabs_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/top_panel/top_panel_tabs_model.py
from enum import IntEnum
from frameworks.wulf import Array, ViewModel

class TabID(IntEnum):
    NONE = 0
    VEHICLE = 1
    STYLE = 2
    BASE_VEHICLE = 3
    PERSONAL_NUMBER_VEHICLE = 4


class TopPanelTabsModel(ViewModel):
    __slots__ = ('onTabChanged', )

    def __init__(self, properties=3, commands=1):
        super(TopPanelTabsModel, self).__init__(properties=properties, commands=commands)

    def getTabIDs(self):
        return self._getArray(0)

    def setTabIDs(self, value):
        self._setArray(0, value)

    @staticmethod
    def getTabIDsType():
        return TabID

    def getTabCustomNames(self):
        return self._getArray(1)

    def setTabCustomNames(self, value):
        self._setArray(1, value)

    @staticmethod
    def getTabCustomNamesType():
        return unicode

    def getCurrentTabID(self):
        return TabID(self._getNumber(2))

    def setCurrentTabID(self, value):
        self._setNumber(2, value.value)

    def _initialize(self):
        super(TopPanelTabsModel, self)._initialize()
        self._addArrayProperty('tabIDs', Array())
        self._addArrayProperty('tabCustomNames', Array())
        self._addNumberProperty('currentTabID')
        self.onTabChanged = self._addCommand('onTabChanged')
