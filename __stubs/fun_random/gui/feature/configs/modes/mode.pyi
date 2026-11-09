# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/modes/mode.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import fields as fields, models as models, schemas as schemas
from fun_random.gui.feature.configs.modes.assets_pack import funModeAssetsPackConfigurationSchema as funModeAssetsPackConfigurationSchema
from fun_random.gui.feature.configs.modes.assets_pack import FunModeAssetsPackConfigurationModel as FunModeAssetsPackConfigurationModel
funModeConfigurationSchema: Any
funModeCompositeConfigurationSchema: Any

class FunModeConfigurationModel(models.Model):
    __slots__: tuple
    assetsPack: Any
    def __init__(self, assetsPack):
        ...

class FunModeCompositeConfigurationModel(models.Model):
    __slots__: tuple
    mode: Any
    def __init__(self, mode):
        ...
