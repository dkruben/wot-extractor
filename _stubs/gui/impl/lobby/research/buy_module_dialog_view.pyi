# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/research/buy_module_dialog_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.format_resource_string_arg_model import FormatResourceStringArgModel as FormatResourceStringArgModel
from gui.impl.gen.view_models.views.lobby.research.buy_module_dialog_view_model import BuyModuleDialogViewModel as BuyModuleDialogViewModel, MountDisabledReason as MountDisabledReason, ModuleType as ModuleType
from gui.impl.gen.view_models.views.lobby.research.sold_module_info_tooltip_model import SoldModuleInfoTooltipModel as SoldModuleInfoTooltipModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView as FullScreenDialogView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES as FITTING_TYPES
from gui.shared.gui_items.items_actions.actions import BuyAndInstallWithOptionalSellItemAction as BuyModuleAction
from gui.shared.items_parameters.params_cache import g_paramsCache as g_paramsCache
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.impl.gen.view_models.views.lobby.research.insufficient_credits_tooltip_model import InsufficientCreditsTooltipModel as InsufficientCreditsTooltipModel
_logger: Any

class BuyModuleDialogView(FullScreenDialogView):
    __slots__: tuple
    lobbyContext: Any
    _module: Any
    _previousModule: Any
    _returnedData: Any
    _currency: Any
    _mountDisabledReason: Any
    _isAutoSellEnabled: Any
    def __init__(self, module, previousModule, currency, mountDisabledReason):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _mayInstall(self):
        ...
    def _setItemPrices(self, model):
        ...
    def _setItemType(self, model):
        ...
    def _setTitleArgs(self, arrModel, frmtArgs):
        ...
    def _setTitleBody(self, model):
        ...
    def _setTitle(self, model):
        ...
    def _setMountDisabledReason(self, model):
        ...
    def _setBaseParams(self, model):
        ...
    # decorador original: @args2params(...)
    def _onAcceptClicked(self, sellPreviousModule):
        ...
    def _getAdditionalData(self):
        ...
