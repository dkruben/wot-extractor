# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/mono_dialog_template_button_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/dialogs/mono_dialog_template_button_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ButtonType(Enum):
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    CUSTOM = 'custom'


class MonoDialogTemplateButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MonoDialogTemplateButtonModel, self).__init__(properties=properties, commands=commands)

    def getAction(self):
        return self._getString(0)

    def setAction(self, value):
        self._setString(0, value)

    def getLabel(self):
        return self._getResource(1)

    def setLabel(self, value):
        self._setResource(1, value)

    def getSoundTarget(self):
        return self._getString(2)

    def setSoundTarget(self, value):
        self._setString(2, value)

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)

    def getType(self):
        return ButtonType(self._getString(4))

    def setType(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(MonoDialogTemplateButtonModel, self)._initialize()
        self._addStringProperty('action', '')
        self._addResourceProperty('label', R.invalid())
        self._addStringProperty('soundTarget', '')
        self._addBoolProperty('isDisabled', False)
        self._addStringProperty('type')
