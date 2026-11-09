# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/shared/hud_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/shared/hud_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class HudDisplay(Enum):
    ALL = 'all'
    NONE = 'none'


class HudViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(HudViewModel, self).__init__(properties=properties, commands=commands)

    def getDisplay(self):
        return HudDisplay(self._getString(0))

    def setDisplay(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(HudViewModel, self)._initialize()
        self._addStringProperty('display', HudDisplay.ALL.value)
