# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/reset_stats_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.dialogs.dialog_template_button import MonoButtonTemplate as MonoButtonTemplate
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_view_model import MonoDialogTemplateViewModel as MonoDialogTemplateViewModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from gui.lootbox_system.base.common import getTextResource as getTextResource
CLOSE_DIALOG_ACTIONS: tuple

class ResetStatsDialog(FullScreenDialogBaseView):
    LAYOUT_ID: Any
    VIEW_MODEL = MonoDialogTemplateViewModel
    DEFAULT_DIMMER_ALPHA = 0.8
    __lootBoxes: Any
    _buttons: Any
    __eventName: Any
    _resourcesParams: Any
    def __init__(self, *args, **kwargs):
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
    def _dumpResourcesParams(self):
        ...
    def _setButtons(self):
        ...
    def _onAction(self, event):
        ...
    def _buildResourcesParams(self):
        ...
    def __onAvailabilityChanged(self):
        ...
    def __isEventAvailable(self):
        ...
