# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/info_page_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/info_page_model.py
from frameworks.wulf import ViewModel

class InfoPageModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(InfoPageModel, self).__init__(properties=properties, commands=commands)

    def getRerollInterval(self):
        return self._getNumber(0)

    def setRerollInterval(self, value):
        self._setNumber(0, value)

    def getIsWeeklySectionAvailable(self):
        return self._getBool(1)

    def setIsWeeklySectionAvailable(self, value):
        self._setBool(1, value)

    def getStandardBlockPlugin(self):
        return self._getString(2)

    def setStandardBlockPlugin(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(InfoPageModel, self)._initialize()
        self._addNumberProperty('rerollInterval', 0)
        self._addBoolProperty('isWeeklySectionAvailable', False)
        self._addStringProperty('standardBlockPlugin', '')
        self.onClose = self._addCommand('onClose')
