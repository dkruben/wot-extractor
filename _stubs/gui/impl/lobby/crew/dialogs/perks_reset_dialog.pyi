# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/perks_reset_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
import SoundGroups as SoundGroups
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY
from gui import SystemMessages as SystemMessages
from gui.customization.shared import getPurchaseGoldForCredits as getPurchaseGoldForCredits, getPurchaseMoneyState as getPurchaseMoneyState, MoneyForPurchase as MoneyForPurchase
from gui.impl import backport as backport
from gui.impl.auxiliary.tankman_operations import packSkills as packSkills, packBaseTankman as packBaseTankman
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent as SimpleTextContent
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle as SimpleTextTitle
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as DefaultDialogPlaceHolders
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.lobby.crew.dialogs.perks_reset_dialog_model import PerksResetDialogModel as PerksResetDialogModel
from gui.impl.lobby.crew.crew_helpers.model_setters import ifWGMAvailableButtonUpdate as ifWGMAvailableButtonUpdate
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.impl.lobby.crew.dialogs.price_cards_content.perks_reset_price_list import PerksResetPriceList as PerksResetPriceList
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.gui_items.processors.tankman import TankmanDropSkills as TankmanDropSkills
from gui.shared.utils import decorators as decorators
from gui.shop import showBuyGoldForCrew as showBuyGoldForCrew
from helpers import dependency as dependency
from items.tankmen import TankmanDescr as TankmanDescr
from messenger import MessengerEntry as MessengerEntry
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import getPerksResetGracePeriod as getPerksResetGracePeriod
from collections import namedtuple as namedtuple
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
_LOC = R.strings.dialogs.perksReset

class PerksResetDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    _itemsCache: Any
    VIEW_MODEL = PerksResetDialogModel
    _tankman: Any
    _isFreePerkReset: Any
    _isFreeByGold: Any
    _lastSoundEvent: Any
    _moneyBalance: Any
    _priceListContent: Any
    def __init__(self, tankmanId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initModel(self):
        ...
    def _finalize(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _onPriceChange(self, index=None):
        ...
    def _onConsumeWalletUpdate(self, *_):
        ...
    def _setResult(self, result):
        ...
    def _resetPerks(self):
        ...
    def _updateTankmenBefore(self):
        ...
    def _updateTankmanAfter(self, xpReuseFraction):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __processReset(self, tankman, dropSkillKey, freeDrop):
        ...
