# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/sub_modes/sub_mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict, TYPE_CHECKING as TYPE_CHECKING
from dict2model import fields as fields, models as models, schemas as schemas
from fun_random.gui.feature.configs.common.gamemode import gameModeConfigurationSchema as gameModeConfigurationSchema
from fun_random.gui.feature.configs.sub_modes.custom_abilities import funSubModeCustomAbilitiesSchema as funSubModeCustomAbilitiesSchema, FunSubModeCustomAbilitiesConfigModel as FunSubModeCustomAbilitiesConfigModel
from fun_random.gui.feature.configs.sub_modes.custom_shells import funSubModeCustomShellsSchema as funSubModeCustomShellsSchema, FunSubModeCustomShellsConfigModel as FunSubModeCustomShellsConfigModel
from fun_random.gui.feature.configs.common.gamemode import GameModeConfigurationModel as GameModeConfigurationModel
funSubModeConfigurationSchema: Any
funSubModeCompositeConfigurationSchema: Any

class FunSubModeConfigurationModel(models.Model):
    __slots__: tuple
    isExclusiveHelpPages: Any
    hasBattleQueueWarning: Any
    assetsPointer: Any
    pbsEfficiency: Any
    customShells: Any
    customAbilities: Any
    showInfoPageOnFirstVisit: Any
    def __init__(self, isExclusiveHelpPages, hasBattleQueueWarning, assetsPointer, pbsEfficiency, customShells, customAbilities, showInfoPageOnFirstVisit):
        ...

class FunSubModeCompositeConfigurationModel(models.Model):
    __slots__: tuple
    common: Any
    subMode: Any
    def __init__(self, common, subMode):
        ...
