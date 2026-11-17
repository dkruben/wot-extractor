# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/epicBattle/tank_carousel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.filters.epic_battle_carousel_filter import EpicBattleCarouselFilter as EpicBattleCarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel as TankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.epicBattle.carousel_data_provider import EpicBattleCarouselDataProvider as EpicBattleCarouselDataProvider
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicBattleTankCarousel(TankCarousel):
    __epicController: Any
    _DISABLED_FILTERS: list
    _carouselDPCls: Any
    _carouselFilterCls: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _getInitialFilterVO(self, contexts):
        ...
