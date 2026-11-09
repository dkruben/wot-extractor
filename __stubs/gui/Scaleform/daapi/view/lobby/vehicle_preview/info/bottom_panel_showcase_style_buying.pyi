# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_showcase_style_buying.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.view.lobby.vehicle_preview.preview_bottom_panel_constants import ObtainingMethodInfo as ObtainingMethodInfo, ObtainingMethods as ObtainingMethods, getShowcaseStyleObtainingInfo as getShowcaseStyleObtainingInfo
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelShowcaseStyleBuyingMeta import VehiclePreviewBottomPanelShowcaseStyleBuyingMeta as VehiclePreviewBottomPanelShowcaseStyleBuyingMeta
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info import dyn_currencies_utils as dyn_utils
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info.style_buying import StyleBuyingProcessor as StyleBuyingProcessor
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.SystemMessages import SM_TYPE as SM_TYPE, pushI18nMessage as pushI18nMessage
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.scheduled_notifications import PeriodicNotifier as PeriodicNotifier
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from typing import Dict as Dict, Optional as Optional, Union as Union
from gui.shared.money import Money as Money
from gui.shared.gui_items.customization.c11n_items import Style as Style
_ACTION_BTN_TOOLTIPS = R.strings.vehicle_preview.showcaseStyleBuying.actionBtn.tooltip

class _FinalizationNotifier(PeriodicNotifier):
    def __init__(self, deltaFunc, updateFunc):
        ...
    def onFinalNotification(self):
        ...
    def _wrapDeltaFunc(self, deltaFunc):
        ...

class VehiclePreviewBottomPanelShowcaseStyleBuying(VehiclePreviewBottomPanelShowcaseStyleBuyingMeta):
    __itemsCache: Any
    __style: Any
    __price: Any
    __dynPrice: Any
    __endTime: Any
    __originalPrice: Any
    __originalDynPrice: Any
    __discountPercent: Any
    __obtainingInfo: Any
    __notifier: Any
    __buyingProcessor: Any
    def __init__(self):
        ...
    def setData(self, style, price, endTime, originalPrice, buyParams, discountPercent, obtainingMethod):
        ...
    def update(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _destroy(self):
        ...
    def __prepareVO(self):
        ...
    def onBuyClick(self):
        ...
    def __getActionBtnTooltip(self, priceMoney):
        ...
    def __getActionBtnLabel(self):
        ...
    @property
    def __haveSuitableVehicles(self):
        ...
    def __onBuy(self):
        ...
    def __getTimeLeftStr(self):
        ...
    def __getTimeDelta(self):
        ...
    def __updateTimer(self):
        ...
    def __onTimeOver(self):
        ...
    def __onSyncCompleted(self, *_):
        ...
