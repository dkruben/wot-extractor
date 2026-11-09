# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/common/base_field_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/common/base_field_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BaseFieldModel(ViewModel):
    __slots__ = ('onChange', 'onLostFocus')

    def __init__(self, properties=4, commands=2):
        super(BaseFieldModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getResource(0)

    def setName(self, value):
        self._setResource(0, value)

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)

    def getErrorMessage(self):
        return self._getString(2)

    def setErrorMessage(self, value):
        self._setString(2, value)

    def getPlaceholder(self):
        return self._getString(3)

    def setPlaceholder(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(BaseFieldModel, self)._initialize()
        self._addResourceProperty('name', R.invalid())
        self._addStringProperty('value', '')
        self._addStringProperty('errorMessage', '')
        self._addStringProperty('placeholder', '')
        self.onChange = self._addCommand('onChange')
        self.onLostFocus = self._addCommand('onLostFocus')
