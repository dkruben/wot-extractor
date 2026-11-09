# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/router_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/common/router_model.py
from frameworks.wulf import ViewModel

class RouterModel(ViewModel):
    __slots__ = ('navigateTo', 'navigateBack')

    def __init__(self, properties=2, commands=2):
        super(RouterModel, self).__init__(properties=properties, commands=commands)

    def getRoute(self):
        return self._getString(0)

    def setRoute(self, value):
        self._setString(0, value)

    def getParams(self):
        return self._getString(1)

    def setParams(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(RouterModel, self)._initialize()
        self._addStringProperty('route', '')
        self._addStringProperty('params', '')
        self.navigateTo = self._addCommand('navigateTo')
        self.navigateBack = self._addCommand('navigateBack')
