# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/battle_pass/tank_carousel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter as BattlePassCarouselFilter
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel as TankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_data_provider import BattlePassCarouselDataProvider as BattlePassCarouselDataProvider
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class BattlePassTankCarousel(TankCarousel):
    _battlePassController: Any
    _carouselDPCls: Any
    _carouselFilterCls: Any
    def __init__(self):
        ...
    def _getFiltersPopoverAlias(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _updateFilter(self):
        ...
    def __onBattlePassSettingsChanged(self, *_):
        ...
    def __onPointsUpdated(self):
        ...
    def __onViewLoaded(self, view, *args, **kwargs):
        ...
