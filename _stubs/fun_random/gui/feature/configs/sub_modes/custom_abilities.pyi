# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/sub_modes/custom_abilities.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import fields as fields, models as models, schemas as schemas
funSubModeCustomAbilitySchema: Any
funSubModeCustomAbilitySlotSchema: Any
funSubModeCustomAbilityLayoutSchema: Any
funSubModeCustomAbilitiesSchema: Any

class FunSubModeCustomAbilityConfigModel(models.Model):
    __slots__: tuple
    intCD: Any
    def __init__(self, intCD):
        ...

class FunSubModeCustomAbilitySlotConfigModel(models.Model):
    __slots__: tuple
    command: Any
    tooltipAlias: Any
    def __init__(self, command, tooltipAlias):
        ...

class FunSubModeCustomAbilityLayoutConfigModel(models.Model):
    __slots__: tuple
    abilityIndex: Any
    slotIndex: Any
    def __init__(self, abilityIndex, slotIndex):
        ...

class FunSubModeCustomAbilitiesConfigModel(models.Model):
    __slots__: tuple
    abilities: Any
    slots: Any
    layouts: Any
    def __init__(self, abilities=None, slots=None, layouts=None):
        ...
    @property
    def exists(self):
        ...
