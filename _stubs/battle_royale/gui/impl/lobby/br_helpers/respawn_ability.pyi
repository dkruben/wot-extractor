# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/br_helpers/respawn_ability.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class RespawnAbility(object):
    __brController: Any
    @classmethod
    def getSoloRespawnPeriod(cls):
        ...
    @classmethod
    def getPlatoonRespawnPeriod(cls):
        ...
    @classmethod
    def getPlatoonTimeToResurrect(cls):
        ...
    @classmethod
    def _getParams(cls, battleType, key):
        ...
