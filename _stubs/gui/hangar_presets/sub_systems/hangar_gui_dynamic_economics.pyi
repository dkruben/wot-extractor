# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/hangar_presets/sub_systems/hangar_gui_dynamic_economics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.hangar_presets.providers.base_dynamic_gui_provider import IHangarDynamicGuiProvider as IHangarDynamicGuiProvider

class HangarGuiDynamicEconomics(IHangarGuiController.IHangarGuiDynamicEconomics):
    __lobbyContext: Any
    __providersHolder: Any
    def __init__(self, providersHolder):
        ...
    def fini(self):
        ...
    def checkBonusCaps(self, bonusType, bonusCaps):
        ...
    def checkCurrentBonusCaps(self, bonusCaps, default=False):
        ...
    def checkCrystalRewards(self, bonusType):
        ...
    def checkCurrentCrystalRewards(self, default=False):
        ...
    def __checkBonusCaps(self, bonusType, bonusCaps, guiProvider):
        ...
    def __checkCrystalRewards(self, bonusType, guiProvider):
        ...
