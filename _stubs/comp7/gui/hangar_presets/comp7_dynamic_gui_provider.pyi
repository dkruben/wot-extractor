# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/hangar_presets/comp7_dynamic_gui_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_modifiers_common import BattleModifiers as BattleModifiers
from comp7.gui.impl.lobby.missions.missions_helpers import Comp7MissionsGuiHelper as Comp7MissionsGuiHelper
from comp7.gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import Comp7LobbyHeaderHelper as Comp7LobbyHeaderHelper
from constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.hangar_presets.providers.default_dynamic_gui_provider import DefaultHangarDynamicGuiProvider as DefaultHangarDynamicGuiProvider
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7HangarDynamicGuiProvider(DefaultHangarDynamicGuiProvider):
    _QUEUE_TYPE = QUEUE_TYPE.COMP7
    _BONUS_TYPES: tuple
    _LOBBY_HEADER_HELPER = Comp7LobbyHeaderHelper
    _MISSIONS_HELPER = Comp7MissionsGuiHelper
    __comp7Controller: Any
    def getBattleModifiers(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getComp7BattleModifiers(comp7Controller=None):
    ...
