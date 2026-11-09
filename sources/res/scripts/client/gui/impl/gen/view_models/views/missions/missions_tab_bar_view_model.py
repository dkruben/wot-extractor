# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/missions/missions_tab_bar_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/missions/missions_tab_bar_view_model.py
from frameworks.wulf import Array, ViewModel

class MissionsTabBarViewModel(ViewModel):
    __slots__ = ('onTabSelectionChanged', )

    def __init__(self, properties=3, commands=1):
        super(MissionsTabBarViewModel, self).__init__(properties=properties, commands=commands)

    def getViews(self):
        return self._getArray(0)

    def setViews(self, value):
        self._setArray(0, value)

    def getCurrentView(self):
        return self._getString(1)

    def setCurrentView(self, value):
        self._setString(1, value)

    def getStartIndex(self):
        return self._getNumber(2)

    def setStartIndex(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(MissionsTabBarViewModel, self)._initialize()
        self._addArrayProperty('views', Array())
        self._addStringProperty('currentView', '')
        self._addNumberProperty('startIndex', 0)
        self.onTabSelectionChanged = self._addCommand('onTabSelectionChanged')
