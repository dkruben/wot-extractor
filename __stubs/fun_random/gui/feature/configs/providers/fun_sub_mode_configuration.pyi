# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/providers/fun_sub_mode_configuration.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.feature.configs.providers.base_configuration import FunBaseConfigurationProvider as FunBaseConfigurationProvider
from fun_random.gui.feature.configs.sub_modes.sub_mode import funSubModeCompositeConfigurationSchema as funSubModeCompositeConfigurationSchema
from fun_random.gui.feature.configs.sub_modes.sub_mode import FunSubModeCompositeConfigurationModel as FunSubModeCompositeConfigurationModel
from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode as IFunSubMode

class FunSubModeConfigurationProvider(FunBaseConfigurationProvider):
    _CONFIGURATION_SCHEMA = funSubModeCompositeConfigurationSchema
    _EMPTY_CONFIGURATION_PATH = 'fun_random/gui/configs/gamemodes/fun_sub_modes/fun_sub_mode_empty.xml'
    def getConfigurationModel(self):
        ...
    def _getRuntimeConfiguration(self, subMode, *args):
        ...
