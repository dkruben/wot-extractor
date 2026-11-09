# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/battle_results/battle_results_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from typing import Dict as Dict
PATH_TO_CONFIG: dict
POSSIBLE_TYPES: tuple
ARENA_BONUS_TYPE_TO_SM_TYPE_BATTLE_RESULT: dict
ARENA_BONUS_TYPE_TO_SM_TYPE_AUTO_MAINTENANCE: dict

class BATTLE_RESULT_ENTRY_TYPE:
    COMMON = 1
    ACCOUNT_SELF = 2
    ACCOUNT_ALL = 3
    VEHICLE_SELF = 4
    VEHICLE_ALL = 5
    PLAYER_INFO = 6
    SERVER = 7
    ALL: tuple
