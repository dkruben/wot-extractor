# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/panel/ammunition/specialization.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/loadout/panel/ammunition/specialization.py
from frameworks.wulf import ViewModel

class Specialization(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(Specialization, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getEditable(self):
        return self._getBool(1)

    def setEditable(self, value):
        self._setBool(1, value)

    def getActive(self):
        return self._getBool(2)

    def setActive(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(Specialization, self)._initialize()
        self._addStringProperty('type', 'none')
        self._addBoolProperty('editable', False)
        self._addBoolProperty('active', False)
