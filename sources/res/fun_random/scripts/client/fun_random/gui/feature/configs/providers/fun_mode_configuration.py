# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/providers/fun_mode_configuration.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/configs/providers/fun_mode_configuration.py
from __future__ import absolute_import
import typing
from gui.shared.utils.functions import deepMergeDicts
from fun_random.gui.feature.configs.modes.mode import funModeCompositeConfigurationSchema
from fun_random.gui.feature.configs.providers.base_configuration import FunBaseConfigurationProvider
from fun_random.gui.shared.fun_system_factory import collectModeAssetsPackConfigPath
if typing.TYPE_CHECKING:
    from fun_random.gui.feature.configs.modes.mode import FunModeCompositeConfigurationModel
    from fun_random.helpers.server_settings import FunRandomConfig

class FunModeConfigurationProvider(FunBaseConfigurationProvider):
    _CONFIGURATION_SCHEMA = funModeCompositeConfigurationSchema
    _EMPTY_CONFIGURATION_PATH = 'fun_random/gui/configs/gamemodes/fun_modes/fun_mode_empty.xml'
    _UNDEFINED_ASSETS_PACK_PATH = 'fun_random/gui/configs/gamemodes/fun_modes/assets_packs/fun_assets_undefined.xml'

    def __init__(self, *args):
        super(FunModeConfigurationProvider, self).__init__('', *args)

    def getConfigurationModel(self):
        return self._configurationModel

    def _getRuntimeConfiguration(self, settings, *args):
        assetsPackConfigOverridePath = collectModeAssetsPackConfigPath(settings.assetsPointer)
        assetsPackConfig = self.getConfigurationByPath(self._UNDEFINED_ASSETS_PACK_PATH, assetsPackConfigOverridePath)
        configuration = {'mode': {'assetsPack': {'assetsPointer': (settings.assetsPointer)}}}
        deepMergeDicts(configuration, {'mode': {'assetsPack': assetsPackConfig}})
        return configuration
