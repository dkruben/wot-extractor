# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/full_screen_param_dialog_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.dialogs.dialog_template_param_view_model import DialogTemplateParamViewModel as DialogTemplateParamViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
_logger: Any

class FullScreenParamDialogView(FullScreenDialogBaseView):
    __slots__: tuple
    VIEW_MODEL = DialogTemplateParamViewModel
    __type: Any
    __params: Any
    __additionalData: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getAdditionalData(self):
        ...
    def _actionHandler(self, args):
        ...
    def _closeHandler(self, _=None):
        ...
