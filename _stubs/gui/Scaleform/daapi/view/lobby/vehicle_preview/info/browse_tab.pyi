# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/browse_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import OFFER_CHANGED_EVENT as OFFER_CHANGED_EVENT
from gui.Scaleform.daapi.view.meta.VehiclePreviewBrowseTabMeta import VehiclePreviewBrowseTabMeta as VehiclePreviewBrowseTabMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW as VEHICLE_PREVIEW
from gui.shared import g_eventBus as g_eventBus, events as events
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.money import Currency as Currency
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache
_MAX_LENGTH_FULL_DESCRIPTION_NO_KPI = 400
_MAX_LENGTH_FULL_DESCRIPTION_WITH_KPI = 280

class VehiclePreviewBrowseTab(VehiclePreviewBrowseTabMeta):
    itemsCache: Any
    __isHeroTank: Any
    __offer: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def setActiveState(self, isActive):
        ...
    def onDisclaimerClick(self):
        ...
    def setHeroTank(self, isHeroTank):
        ...
    def setActiveOffer(self, offer):
        ...
    def update(self, *_):
        ...
    def _update(self):
        ...
    def __onOfferChanged(self, event):
        ...
    def __isFrontlineCreditsOffer(self):
        ...
