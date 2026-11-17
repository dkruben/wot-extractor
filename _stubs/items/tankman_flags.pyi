# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/tankman_flags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from struct_helpers import packByte as packByte

class TankmanFlags(object):
    __slots__: tuple
    EXTENDED_VEHICLE_TYPE_ID_FLAG = 128
    IS_PREMIUM_FLAG = 64
    IS_FEMALE_FLAG = 32
    HAS_FREE_SKILLS_FLAG = 16
    HAS_BONUS_SKILLS_FLAG = 8
    DISABLE_FIRST_SKILL_RESET = 4
    MORE_FLAGS_FLAG = 1
    OFFSET_BEFORE_FLAGS = 1
    _len: Any
    extendedVehicleTypeID: Any
    isPremium: Any
    isFemale: Any
    hasFreeSkills: Any
    hasBonusSkills: Any
    firstSkillResetDisabled: Any
    def __init__(self):
        ...
    @staticmethod
    def fromCDWithOffset(compactDescriptor):
        ...
    @classmethod
    def fromCD(cls, compactDescriptor):
        ...
    def pack(self):
        ...
    @property
    def len(self):
        ...
