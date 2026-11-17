# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/enlarge_barracks_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet as IconSet
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as Placeholder
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.dialogs.template_settings.default_dialog_template_settings import DisplayFlags as DisplayFlags
from gui.impl.gen.view_models.views.lobby.crew.dialogs.enlarge_barracks_dialog_model import EnlargeBarracksDialogModel as EnlargeBarracksDialogModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import getBethsSlotsCount as getBethsSlotsCount
from gui.impl.lobby.crew.tooltips.bunks_confirm_discount_tooltip import BunksConfirmDiscountTooltip as BunksConfirmDiscountTooltip
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.money import Currency as Currency
from gui.shop import showBuyGoldForBerth as showBuyGoldForBerth
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class EnlargeBarracksDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = EnlargeBarracksDialogModel
    itemsCache: Any
    __STEPPER_MAX_VALUE = 160
    __countPacksBerths: Any
    __berthPrice: Any
    __berthsInPack: Any
    __defaultBerthPrice: Any
    __isDiscount: Any
    __pricePacksBerths: Any
    def __init__(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _enlargeBarracks(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getCallbacks(self):
        ...
    def _onGoldUpdate(self, *_):
        ...
    def _setResult(self, result):
        ...
    def _updateViewMode(self, freeBunksCount, allBunksCount):
        ...
    def __prepareBerthInfo(self):
        ...
    # decorador original: @args2params(...)
    def __onBunksCountChange(self, selectedCount):
        ...
    def __onCacheResync(self, reason, _):
        ...
    def __isEnoughMoney(self):
        ...
