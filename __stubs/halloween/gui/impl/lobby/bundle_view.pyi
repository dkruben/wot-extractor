# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/bundle_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.shared.money import Currency as Currency
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel as BonusItemViewModel
from halloween.gui.impl.lobby.hw_helpers.bonuses_formatters import HalloweenBonusesAwardsComposer as HalloweenBonusesAwardsComposer, getHWMetaAwardFormatter as getHWMetaAwardFormatter, getImgName as getImgName
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from halloween.gui.impl.lobby.tooltips.key_tooltip import KeyTooltipView as KeyTooltipView
from halloween.gui.impl.lobby.tooltips.vehicle_tooltip import VehicleTooltipView as VehicleTooltipView
from halloween.gui.shared.event_dispatcher import showHalloweenShopBundle as showHalloweenShopBundle
from halloween.gui.shop import showHWBuyGoldForBundle as showHWBuyGoldForBundle
from halloween.gui.sounds.sound_constants import BUNDLE_ENTER as BUNDLE_ENTER, BUNDLE_EXIT as BUNDLE_EXIT
from halloween.gui.game_control.halloween_artefacts_controller import getBonusPriority as getBonusPriority
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.skeletons.halloween_shop_controller import IHalloweenShopController as IHalloweenShopController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys, HWLogActions as HWLogActions
from halloween_common.halloween_constants import ArtefactsSettings as ArtefactsSettings
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen import R as R
from halloween.gui.impl.lobby.base_view import BaseView as BaseView
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from halloween.gui.impl.gen.view_models.views.lobby.bundle_view_model import BundleViewModel as BundleViewModel, WindowType as WindowType, TitleStates as TitleStates
from halloween.gui.impl.gen.view_models.views.lobby.bundle_model import BundleModel as BundleModel
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from halloween.gui.sounds import playSound as playSound
MAX_BONUSES_IN_VIEW = 10
AMOUNT_OF_KEYS_DEFAULT = 1
KEY_TOKEN: Any
_R_BACKPORT_TOOLTIP: Any

class BundleView(BaseView):
    _appLoader: Any
    _itemsCache: Any
    _hwController: Any
    _hwArtefactCtrl: Any
    _hwShopCtrl: Any
    __artefactID: Any
    __bonusCache: Any
    __tooltipCtx: Any
    __idGen: Any
    __uiLogger: Any
    def __init__(self, layoutID=..., artefactID='', *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _subscribe(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _unsubscribe(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillMoneyBalance(self, *args, **kwargs):
        ...
    def __fillBalance(self, *args, **kwargs):
        ...
    def __fillViewModel(self, *args, **kwargs):
        ...
    def _loadBundles(self, model, artefact):
        ...
    def _onPurchaseBundle(self, args):
        ...
    def _getEvents(self):
        ...
    def __isEnoughMoney(self, bundle, count):
        ...
    def __onArtefactKeyUpdated(self):
        ...
    # decorador original: @adisp_process
    def __processPurchase(self, bundleID, count):
        ...
    def __onBundlesUpdated(self):
        ...
    def __getMoney(self, currency):
        ...
    def __getTitleState(self, hasShopBundle, hasKeyBundle):
        ...
