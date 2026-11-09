# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/message_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/message_model.py
from frameworks.wulf import ViewModel

class MessageModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MessageModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getOrder(self):
        return self._getNumber(2)

    def setOrder(self, value):
        self._setNumber(2, value)

    def getViewed(self):
        return self._getBool(3)

    def setViewed(self, value):
        self._setBool(3, value)

    def getSelected(self):
        return self._getBool(4)

    def setSelected(self, value):
        self._setBool(4, value)

    def getSystem(self):
        return self._getBool(5)

    def setSystem(self, value):
        self._setBool(5, value)

    def getPrebattle(self):
        return self._getBool(6)

    def setPrebattle(self, value):
        self._setBool(6, value)

    def getTooltipId(self):
        return self._getString(7)

    def setTooltipId(self, value):
        self._setString(7, value)

    def _initialize(self):
        super(MessageModel, self)._initialize()
        self._addNumberProperty('id', 0)
        self._addStringProperty('name', '')
        self._addNumberProperty('order', 0)
        self._addBoolProperty('viewed', False)
        self._addBoolProperty('selected', False)
        self._addBoolProperty('system', False)
        self._addBoolProperty('prebattle', False)
        self._addStringProperty('tooltipId', '')
