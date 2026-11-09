# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/wot_plus/base_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.dialogs.dialog_template_button import MonoButtonTemplate as MonoButtonTemplate
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_view_model import MonoDialogTemplateViewModel as MonoDialogTemplateViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
CLOSE_DIALOG_ACTIONS: tuple

class BaseDialog(FullScreenDialogBaseView):
    LAYOUT_ID: Any
    VIEW_MODEL = MonoDialogTemplateViewModel
    DEFAULT_DIMMER_ALPHA = 0.6
    BACKGROUND_IMAGE = None
    _contentParams: Any
    _resourcesParams: Any
    _buttons: Any
    def __init__(self, contentParams, resourcesParams, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _addButton(self, monoButton):
        ...
    def _buildButton(self, action, label, buttonType, isDisabled=False):
        ...
    def _dumpContentParams(self):
        ...
    def _dumpResourcesParams(self):
        ...
    def _setButtons(self):
        ...
    def _onAction(self, event):
        ...
