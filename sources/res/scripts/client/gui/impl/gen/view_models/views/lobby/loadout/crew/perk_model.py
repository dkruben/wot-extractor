# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/perk_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/perk_model.py
from frameworks.wulf import ViewModel

class PerkModel(ViewModel):
    __slots__ = ()
    NEW_STATE = 'new'
    FREE_STATE = 'free'
    LEARNING_STATE = 'learning'
    LEARNED_STATE = 'learned'
    IRRELEVANT_STATE = 'irrelevant'

    def __init__(self, properties=2, commands=0):
        super(PerkModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getState(self):
        return self._getString(1)

    def setState(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(PerkModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('state', '')
