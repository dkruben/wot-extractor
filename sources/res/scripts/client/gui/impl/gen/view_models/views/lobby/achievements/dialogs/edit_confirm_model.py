# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/dialogs/edit_confirm_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/dialogs/edit_confirm_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class DialogType(Enum):
    AUTO_SELECT_ENABLED = 'autoSelectEnabled'
    AUTO_SELECT_DISABLED = 'autoSelectDisabled'
    ERROR = 'error'


class EditConfirmModel(ViewModel):
    __slots__ = ('onAccept', 'onCancel', 'onClose')

    def __init__(self, properties=1, commands=3):
        super(EditConfirmModel, self).__init__(properties=properties, commands=commands)

    def getDialogType(self):
        return DialogType(self._getString(0))

    def setDialogType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(EditConfirmModel, self)._initialize()
        self._addStringProperty('dialogType')
        self.onAccept = self._addCommand('onAccept')
        self.onCancel = self._addCommand('onCancel')
        self.onClose = self._addCommand('onClose')
