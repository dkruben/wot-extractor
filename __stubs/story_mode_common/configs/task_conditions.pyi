# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/configs/task_conditions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import enum as enum
from dict2model import fields as fields
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
_VALUE_FIELD_BY_TYPE: dict
_VSE_SLOT_BY_TYPE: dict

# decorador original: @enum.unique
class TaskConditionType(str, enum.Enum):
    INT = 'int'
    FLOAT = 'float'
    def getSchemaFieldType(self):
        ...
    def getVseSlotType(self):
        ...
