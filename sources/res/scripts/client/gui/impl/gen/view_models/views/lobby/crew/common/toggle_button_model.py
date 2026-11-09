# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/toggle_button_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/toggle_button_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.crew.common.button_model import ButtonModel

class ToggleState(Enum):
    ON = 'on'
    OFF = 'off'
    DISABLED = 'disabled'
    HIDDEN = 'hidden'


class ToggleButtonModel(ButtonModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ToggleButtonModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return ToggleState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(ToggleButtonModel, self)._initialize()
        self._addStringProperty('state')
        self._addBoolProperty('isDisabled', False)
