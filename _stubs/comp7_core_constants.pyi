# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/common/comp7_core_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import enum as enum
import constants as constants
from constants_utils import ConstInjector as ConstInjector
ROLE_EQUIPMENT_TAG = 'roleEquipment'

class ArenaPrebattlePhase(object):
    NONE = 0
    PREPICK = 1
    VOTING = 2
    PICK = 3

class FINISH_REASON(constants.FINISH_REASON, ConstInjector):
    SURVIVORS_LEFT = 201
    DAMAGE_DEALT = 202
    FIRST_KILL = 203
    DRAW_RESOLVED_REASONS: tuple

class SubMode(enum.Enum):
    REGULAR = 'regular'
    NIGHT_MAPS = 'night_maps'

def injectCommonConstants(personality):
    ...
