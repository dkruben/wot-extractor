# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_card_types.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/mode_selector/mode_selector_card_types.py
from frameworks.wulf import ViewModel

class ModeSelectorCardTypes(ViewModel):
    __slots__ = ()
    DEFAULT = 0
    RANDOM = 1
    RANKED = 2
    MAPBOX = 3
    EPIC_BATTLE = 4
    BATTLE_ROYALE = 5
    FUN_RANDOM = 6

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorCardTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ModeSelectorCardTypes, self)._initialize()
