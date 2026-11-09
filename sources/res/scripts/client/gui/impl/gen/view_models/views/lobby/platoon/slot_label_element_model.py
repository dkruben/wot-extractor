# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/platoon/slot_label_element_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/platoon/slot_label_element_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class Types(Enum):
    IMAGE = 'image'
    TEXT = 'text'


class SlotLabelElementModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SlotLabelElementModel, self).__init__(properties=properties, commands=commands)

    def getContent(self):
        return self._getString(0)

    def setContent(self, value):
        self._setString(0, value)

    def getType(self):
        return Types(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)

    def getStyleJson(self):
        return self._getString(2)

    def setStyleJson(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(SlotLabelElementModel, self)._initialize()
        self._addStringProperty('content', '')
        self._addStringProperty('type')
        self._addStringProperty('styleJson', '')
