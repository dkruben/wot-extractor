# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TeamInfoPBHComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from helpers import isPlayerAvatar as isPlayerAvatar, dependency as dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class TeamInfoPBHComponent(DynamicScriptComponent):
    __sessionProvider: Any
    def __init__(self, *_, **__):
        ...
    def _onAvatarReady(self):
        ...
    def set_winners(self, _):
        ...
    def __updateWinnersInfo(self):
        ...
    @classmethod
    def getInstance(cls):
        ...
    def __convertWinnerToDict(self, winner):
        ...
