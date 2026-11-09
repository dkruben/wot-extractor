# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/panel/ammunition/section_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/loadout/panel/ammunition/section_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.slot_model import SlotModel

class SectionState(Enum):
    DEFAULT = 'default'
    WARNING = 'warning'


class SectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SectionModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getSlots(self):
        return self._getArray(1)

    def setSlots(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSlotsType():
        return SlotModel

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)

    def getState(self):
        return SectionState(self._getString(3))

    def setState(self, value):
        self._setString(3, value.value)

    def _initialize(self):
        super(SectionModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addArrayProperty('slots', Array())
        self._addStringProperty('type', '')
        self._addStringProperty('state')
