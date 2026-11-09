# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dog_tags_common/config/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from soft_exception import SoftException as SoftException
DOG_TAGS_FILE = 'scripts/item_defs/dog_tags/dog_tags.xml'
DOG_TAGS_SCHEMA_FILE = 'scripts/item_defs/dog_tags/dog_tags_schema.xsd'
DEFAULT_GRADE = 0
NO_PROGRESS = 0
TRIUMPH_GRADES = 4
DEDICATION_GRADES = 10
SKILL_GRADES = 10
RANKED_SKILL_GRADES = 10
STARTING_COMPONENT_TYPES: tuple
SEND_NEW_GRADING_NOTIFICATION: tuple
DEFAULT_BOT_STRATEGY = BotDogTagStrategy.DEFAULT
DEFAULT_BOT_STRATEGY_DEVELOP = BotDogTagStrategy.RANDOM
MAX_GRADE = 9

class ComponentViewType(Enum):
    BACKGROUND = 'background'
    ENGRAVING = 'engraving'
    def getTabIdx(self):
        ...

class ComponentPurpose(Enum):
    BASE = 'BASE'
    TRIUMPH_MEDAL = 'TRIUMPH_MEDAL'
    TRIUMPH = 'TRIUMPH'
    DEDICATION = 'DEDICATION'
    SKILL = 'SKILL'
    RANKED_SKILL = 'RANKED_SKILL'
    COUPLED = 'COUPLED'

class ComponentNumberType(Enum):
    NUMBER = 'NUMBER'
    PERCENTAGE = 'PERCENTAGE'

class DogTagsException(SoftException):
    err: Any
    args: Any
    def __init__(self, err, *args):
        ...

class ParseException(DogTagsException):
    PREFIX = 'PARSE_ERR_%d: '
    PATH = "Error in section '%s': "
    CAN_NOT_OPEN_XML = 1
    XML_VALIDATION_FAILED = 2
    TAG_DUPLICITY = 3
    PARAM_DUPLICITY = 4
    WRONG_PARAM_VALUE = 5
    STARTING_COMPONENT_DUPLICITY = 6
    STARTING_COMPONENT_INVALID_ID = 7
    ERR_STR: dict
    def __str__(self):
        ...

class ValidateException(DogTagsException):
    PREFIX = 'VALIDATE_ERR_%d: '
    HAS_GRADES = 1
    HAS_UNLOCK_KEY = 2
    WRONG_NUMBER_OF_GRADES = 3
    DEFAULT_WRONG_GRADES = 4
    WRONG_TYPE_VIEW_COMBINATION = 5
    STARTING_COMPONENT_INVALID_TYPE = 7
    STARTING_COMPONENT_WRONG_DATA = 9
    STARTING_COMPONENT_NON_DEFAULT = 10
    SHOULD_BE_DEFAULT_OR_HAS_UNLOCK_KEY = 11
    DEFAULT_HIDDEN = 12
    CANNOT_BE_DEFAULT = 13
    UNLOCK_KEY_AND_EXTERNAL_UNLOCK = 14
    WRONG_COUPLED_COMPONENT_ID = 15
    ERR_STR: dict
    def __str__(self):
        ...

class ParameterType(Enum):
    INT = 0
    BOOL = 1
    STR = 2
    INT_LIST = 3
    STR_LIST = 4
    VIEW_TYPE = 5
    TYPE = 6
    NUMBER_TYPE = 7
    FLOAT_LIST = 8

class Visibility(Enum):
    SERVER = 0
    CLIENT = 1
    ALL = 2

class BotDogTagStrategy(Enum):
    DEFAULT = 1
    RANDOM = 2
