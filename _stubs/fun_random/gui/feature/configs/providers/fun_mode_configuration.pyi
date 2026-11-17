# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/providers/fun_mode_configuration.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.shared.utils.functions import deepMergeDicts as deepMergeDicts
from fun_random.gui.feature.configs.modes.mode import funModeCompositeConfigurationSchema as funModeCompositeConfigurationSchema
from fun_random.gui.feature.configs.providers.base_configuration import FunBaseConfigurationProvider as FunBaseConfigurationProvider
from fun_random.gui.shared.fun_system_factory import collectModeAssetsPackConfigPath as collectModeAssetsPackConfigPath
from fun_random.gui.feature.configs.modes.mode import FunModeCompositeConfigurationModel as FunModeCompositeConfigurationModel
from fun_random.helpers.server_settings import FunRandomConfig as FunRandomConfig

class FunModeConfigurationProvider(FunBaseConfigurationProvider):
    _CONFIGURATION_SCHEMA = funModeCompositeConfigurationSchema
    _EMPTY_CONFIGURATION_PATH = 'fun_random/gui/configs/gamemodes/fun_modes/fun_mode_empty.xml'
    _UNDEFINED_ASSETS_PACK_PATH: str
    def __init__(self, *args):
        ...
    def getConfigurationModel(self):
        ...
    def _getRuntimeConfiguration(self, settings, *args):
        ...
