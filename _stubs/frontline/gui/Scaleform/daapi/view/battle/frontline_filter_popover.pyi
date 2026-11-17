# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_filter_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frontline.gui.Scaleform.daapi.view.meta.FrontlineCarouselFilterPopoverMeta import FrontlineCarouselFilterPopoverMeta as FrontlineCarouselFilterPopoverMeta
from gui.filters.carousel_filter import FILTER_KEYS as FILTER_KEYS
from gui.Scaleform.daapi.view.common.common_constants import FILTER_POPOVER_SECTION as FILTER_POPOVER_SECTION
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehiclePlaylistsController as IVehiclePlaylistsController

class FrontlineBattleTankCarouselFilterPopover(FrontlineCarouselFilterPopoverMeta):
    _BASE_SPECIALS_LIST: list
    __vehiclePlaylistsCtrl: Any
    def _getInitialVO(self, filters, xpRateMultiplier):
        ...
    def _generateMapping(self, hasRented, hasEvent, hasRoles, hasCustomization, **kwargs):
        ...
    def onPlayListsChange(self, playListId):
        ...
    def setTankCarousel(self, carousel):
        ...
