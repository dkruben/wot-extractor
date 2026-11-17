# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/epic_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import IS_CLIENT as IS_CLIENT, OFFER_TOKEN_PREFIX as OFFER_TOKEN_PREFIX, IS_WEB as IS_WEB
from items.components.supply_slot_categories import SlotCategories as SlotCategories
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
EPIC_TOKEN_PREFIX = 'epic:'
EPIC_OFFER_TOKEN_PREFIX: Any
EPIC_SELECT_BONUS_NAME = 'epicSelectToken'
EPIC_SKILL_TOKEN_NAME = 'abilityToken'
LEVELUP_TOKEN_TEMPLATE = 'epicmetagame:levelup:'
EPIC_OFFER_TYPES: tuple
EPIC_CHOICE_REWARD_OFFER_TOKENS: Any
EPIC_CHOICE_REWARD_OFFER_GIFT_TOKENS: Any
EPICS_CHOICE_REWARD_OFFER_TOKEN_FREE_POSTFIX = 'free:'
EPIC_CHOICE_REWARD_OFFER_TOKEN_PAID_POSTFIX = 'paid:'
FRONTLINE_BONUSES_ORDER: tuple
EPIC_BATTLE_LEVEL_IMAGE_INDEX: tuple
CATEGORIES_ORDER: list

class EPIC_BATTLE_TEAM_ID(object):
    TEAM_ATTACKER = 1
    TEAM_DEFENDER = 2

class SECTOR_EDGE_STATE(CONST_CONTAINER):
    NONE = 0
    SAFE = 1
    DANGER = 2
