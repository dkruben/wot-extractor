# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/restore_tankman_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/dialogs/restore_tankman_dialog_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class RestoreTankmanDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=2):
        super(RestoreTankmanDialogModel, self).__init__(properties=properties, commands=commands)

    @property
    def tankman(self):
        return self._getViewModel(6)

    @staticmethod
    def getTankmanType():
        return TankmanModel

    def _initialize(self):
        super(RestoreTankmanDialogModel, self)._initialize()
        self._addViewModelProperty('tankman', TankmanModel())
