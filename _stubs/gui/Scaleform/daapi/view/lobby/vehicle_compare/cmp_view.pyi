# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import range as range
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_parameters import CMP_HIDDEN_PARAMETERS as CMP_HIDDEN_PARAMETERS, IVehCompareView as IVehCompareView, VehCompareBasketParamsCache as VehCompareBasketParamsCache
from gui.Scaleform.daapi.view.meta.VehicleCompareViewMeta import VehicleCompareViewMeta as VehicleCompareViewMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import ListDAAPIDataProvider as ListDAAPIDataProvider
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.game_control.veh_comparison_basket import MAX_VEHICLES_TO_COMPARE_COUNT as MAX_VEHICLES_TO_COMPARE_COUNT
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar, showVehiclePreview as showVehiclePreview, showHangar as showHangar
from gui.shared.events import LoadViewEvent as LoadViewEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.items_parameters.formatters import getAllParametersTitles as getAllParametersTitles
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from tutorial.hints_manager import HINT_SHOWN_STATUS as HINT_SHOWN_STATUS

class VehicleCompareView(LobbySubView, VehicleCompareViewMeta):
    __background_alpha__ = 0.0
    itemsCache: Any
    comparisonBasket: Any
    __vehDP: Any
    __paramsCache: Any
    __backAlias: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def onSelectModulesClick(self, vehicleID, index):
        ...
    def onRemoveAllVehicles(self):
        ...
    def onRemoveVehicle(self, index):
        ...
    def onRevertVehicle(self, index):
        ...
    def onGoToPreviewClick(self, slotID):
        ...
    def onGoToHangarClick(self, vehicleID):
        ...
    def onParamDeltaRequested(self, index, paramID):
        ...
    def onBackClick(self):
        ...
    def _populate(self):
        ...
    def _setViewData(self):
        ...
    def _dispose(self):
        ...
    def __clearParamsCache(self):
        ...
    def __updateUI(self, *data):
        ...
    def __onVehCmpBasketStateChanged(self):
        ...
    def __updateDifferenceAttention(self):
        ...
    def __onVehicleParamsChanged(self, _):
        ...
    def __onNationChange(self, _):
        ...

class VehiclesDataProvider(ListDAAPIDataProvider, IVehCompareView):
    __list: Any
    def __init__(self):
        ...
    @property
    def sortedCollection(self):
        ...
    @property
    def collection(self):
        ...
    def emptyItem(self):
        ...
    def buildList(self, *args):
        ...
    def updateItems(self, *args):
        ...
    def clear(self):
        ...
    def fini(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _updateVehicleConfigHint(settingsCore=None):
    ...
