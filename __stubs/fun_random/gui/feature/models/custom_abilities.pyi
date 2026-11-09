# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/models/custom_abilities.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from items import vehicles as vehicles
from fun_random.gui.feature.configs.sub_modes.custom_abilities import FunSubModeCustomAbilityConfigModel as FunSubModeCustomAbilityConfigModel, FunSubModeCustomAbilitySlotConfigModel as FunSubModeCustomAbilitySlotConfigModel, FunSubModeCustomAbilityLayoutConfigModel as FunSubModeCustomAbilityLayoutConfigModel, FunSubModeCustomAbilitiesConfigModel as FunSubModeCustomAbilitiesConfigModel
from items.artefacts import Equipment as Equipment

class FunCustomAbility(object):
    intCD: Any
    imageName: Any
    def __init__(self, intCD, imageName):
        ...
    @classmethod
    def fromEquipmentItem(cls, equipment):
        ...
    @classmethod
    def fromCustomEquipmentConfig(cls, abilityConfig):
        ...

class FunCustomAbilitySlot(object):
    __slotConfig: Any
    __customAbility: Any
    def __init__(self, slotConfig, customAbility):
        ...
    @classmethod
    def fromCustomLayoutConfig(cls, customAbilitiesConfig, layoutConfig):
        ...
    @property
    def ability(self):
        ...
    @property
    def command(self):
        ...
    @property
    def tooltipAlias(self):
        ...
