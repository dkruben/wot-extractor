# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/hangar_preset/battle_royale_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.hangar_presets.providers import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from battle_royale.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import BattleRoyaleLobbyHeaderHelper as BattleRoyaleLobbyHeaderHelper

class BattleRoyaleHangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    __slots__: tuple
    _QUEUE_TYPE = QUEUE_TYPE.BATTLE_ROYALE
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = BattleRoyaleLobbyHeaderHelper
    _platoonCtrl: Any
    def getSuggestedBonusType(self):
        ...
