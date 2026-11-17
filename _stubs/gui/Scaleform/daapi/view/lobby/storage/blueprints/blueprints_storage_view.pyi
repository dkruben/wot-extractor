# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/blueprints/blueprints_storage_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import nations as nations
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.blueprints import BlueprintsStorageCarouselDataProvider as BlueprintsStorageCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.storage.blueprints import BlueprintsStorageCarouselFilter as BlueprintsStorageCarouselFilter
from gui.Scaleform.daapi.view.lobby.storage.storage_carousel_environment import StorageCarouselEnvironment as StorageCarouselEnvironment
from gui.Scaleform.daapi.view.meta.StorageCategoryBlueprintsViewMeta import StorageCategoryBlueprintsViewMeta as StorageCategoryBlueprintsViewMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.requesters.blueprints_requester import getNationalFragmentCD as getNationalFragmentCD
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.locale.STORAGE import STORAGE as STORAGE
from gui import GUI_NATIONS as GUI_NATIONS
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class StorageCategoryBlueprintsView(StorageCategoryBlueprintsViewMeta, StorageCarouselEnvironment):
    __lobbyCtx: Any
    __needToResetScrollTo: Any
    __currentFilteredVehicles: Any
    __isFilterCounterShown: Any
    def __init__(self):
        ...
    def navigateToBlueprintScreen(self, itemId):
        ...
    def selectConvertible(self, value):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _createDataProvider(self):
        ...
    def _onCacheResync(self, reason, diff):
        ...
    @staticmethod
    def __makeFragmentVO(count, iconName, tooltipData=None):
        ...
    def __onViewLoaded(self, view, *args, **kwargs):
        ...
    def __onUpdateBlueprints(self, _):
        ...
    def __updateVehicles(self, vehicles=None, filterCriteria=None):
        ...
    def __updateUniversalFragments(self):
        ...
    def __updateNationFragments(self):
        ...
    def __updateIntelligence(self):
        ...
    def __updateFilterWarning(self):
        ...
    def __areCertainLevelsChosenInFilter(self, chosenKeys):
        ...
    def __restoreCarouselState(self):
        ...
