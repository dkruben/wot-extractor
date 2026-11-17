# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/common/comp7_light_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
import enum as enum
from constants_utils import ConstInjector as ConstInjector
import UnitBase as UnitBase
COMP7_LIGHT_INBATTLE_CONFIGS: tuple
BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7_LIGHT: Any

class Configs(enum.Enum):
    COMP7_LIGHT_CONFIG = 'comp7_light_config'

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    COMP7_LIGHT = 35

class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    COMP7_LIGHT = 27

class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    COMP7_LIGHT = PREBATTLE_TYPE.COMP7_LIGHT

class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    COMP7_LIGHT = 16777216

class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    COMP7_LIGHT_ROSTER: Any

class GameSeasonType(constants.GameSeasonType, ConstInjector):
    COMP7_LIGHT = 9

class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    SET_COMP7_LIGHT_SQUAD_SIZE = 4302
