# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/mapbox/tank_carousel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import Configs as Configs
from gui.filters.mapbox_carousel_filter import MapboxCarouselFilter as MapboxCarouselFilter
from gui.Scaleform.daapi.view.lobby.hangar.carousels import BattlePassTankCarousel as BattlePassTankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.mapbox.carousel_data_provider import MapboxCarouselDataProvider as MapboxCarouselDataProvider
from helpers import server_settings as server_settings

class MapboxTankCarousel(BattlePassTankCarousel):
    _carouselDPCls: Any
    _carouselFilterCls: Any
    def __init__(self):
        ...
    def _onServerSettingChanged(self, diff, skipVehicles=False):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingChanged(self, *_):
        ...
