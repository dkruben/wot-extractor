# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/customization_confirm_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/customization_confirm_dialog_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_dog_tag import DtDogTag

class CustomizationConfirmDialogModel(ViewModel):
    __slots__ = ('onClose', 'onDiscard', 'onConfirm')

    def __init__(self, properties=1, commands=3):
        super(CustomizationConfirmDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def equippedDogTag(self):
        return self._getViewModel(0)

    @staticmethod
    def getEquippedDogTagType():
        return DtDogTag

    def _initialize(self):
        super(CustomizationConfirmDialogModel, self)._initialize()
        self._addViewModelProperty('equippedDogTag', DtDogTag())
        self.onClose = self._addCommand('onClose')
        self.onDiscard = self._addCommand('onDiscard')
        self.onConfirm = self._addCommand('onConfirm')
