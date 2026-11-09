# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/battle_pass/carousel_data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import HangarCarouselDataProvider as HangarCarouselDataProvider
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController

class BattlePassCarouselDataProvider(HangarCarouselDataProvider):
    battlePassController: Any
    def _buildVehicle(self, vehicle):
        ...
    def _isBattlePassHidden(self, vehicle):
        ...
