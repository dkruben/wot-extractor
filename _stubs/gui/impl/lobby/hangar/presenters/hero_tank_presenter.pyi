# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/hero_tank_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import Math as Math
from GUI import WGMarkerPositionController as WGMarkerPositionController
from HeroTank import HeroTank as HeroTank
from gui.impl.gen.view_models.views.lobby.hangar.hero_tank_model import HeroTankModel as HeroTankModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import HangarVehicleEvent as HangarVehicleEvent
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class HeroTankPresenter:
    __itemsCache: Any
    __space: Any
    __markerCtrl: Any
    __hasHeroTank: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def __clearMarkers(self, _):
        ...
    @staticmethod
    def __getCorrectedMarkerPosition(vehicle):
        ...
    def __fillHeroTank(self, *args):
        ...
    def __onCacheResync(self, reason, diff):
        ...
