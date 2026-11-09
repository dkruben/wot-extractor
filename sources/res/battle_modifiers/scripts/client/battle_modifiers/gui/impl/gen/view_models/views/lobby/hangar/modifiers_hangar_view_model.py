# wot-extractor: codigo DESCOMPILADO de sources/res/battle_modifiers/scripts/client/battle_modifiers/gui/impl/gen/view_models/views/lobby/hangar/modifiers_hangar_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_modifiers/scripts/client/battle_modifiers/gui/impl/gen/view_models/views/lobby/hangar/modifiers_hangar_view_model.py
from frameworks.wulf import Array, ViewModel

class ModifiersHangarViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ModifiersHangarViewModel, self).__init__(properties=properties, commands=commands)

    def getModifiersDomains(self):
        return self._getArray(0)

    def setModifiersDomains(self, value):
        self._setArray(0, value)

    @staticmethod
    def getModifiersDomainsType():
        return unicode

    def _initialize(self):
        super(ModifiersHangarViewModel, self)._initialize()
        self._addArrayProperty('modifiersDomains', Array())
