# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tournaments/team_logos_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tournaments/team_logos_model.py
from frameworks.wulf import ViewModel

class TeamLogosModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TeamLogosModel, self).__init__(properties=properties, commands=commands)

    def getX48(self):
        return self._getString(0)

    def setX48(self, value):
        self._setString(0, value)

    def getX86(self):
        return self._getString(1)

    def setX86(self, value):
        self._setString(1, value)

    def getX260(self):
        return self._getString(2)

    def setX260(self, value):
        self._setString(2, value)

    def getX522(self):
        return self._getString(3)

    def setX522(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(TeamLogosModel, self)._initialize()
        self._addStringProperty('x48', '')
        self._addStringProperty('x86', '')
        self._addStringProperty('x260', '')
        self._addStringProperty('x522', '')
