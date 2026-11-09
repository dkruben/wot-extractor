# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/setup_tabs_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/common/setup_tabs_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.setup_tab_model import SetupTabModel

class SetupTabsModel(ViewModel):
    __slots__ = ('onTabChanged', )

    def __init__(self, properties=2, commands=1):
        super(SetupTabsModel, self).__init__(properties=properties, commands=commands)

    def getTabs(self):
        return self._getArray(0)

    def setTabs(self, value):
        self._setArray(0, value)

    @staticmethod
    def getTabsType():
        return SetupTabModel

    def getSelectedTabName(self):
        return self._getString(1)

    def setSelectedTabName(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(SetupTabsModel, self)._initialize()
        self._addArrayProperty('tabs', Array())
        self._addStringProperty('selectedTabName', '')
        self.onTabChanged = self._addCommand('onTabChanged')
