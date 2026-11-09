# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/providers/base_configuration.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/configs/providers/base_configuration.py
from __future__ import absolute_import
import copy, typing, ResMgr, section2dict
from dict2model import schemas
from gui.shared.utils.functions import deepMergeDicts
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from dict2model import models
g_configurationsCache = {}

class FunBaseConfigurationProvider(object):
    _CONFIGURATION_SCHEMA = schemas.Schema({})
    _EMPTY_CONFIGURATION_PATH = ''

    def __init__(self, overridesPath, *args):
        configuration = copy.deepcopy(self.getConfigurationByPath(self._EMPTY_CONFIGURATION_PATH, overridesPath))
        deepMergeDicts(configuration, self._getRuntimeConfiguration(*args))
        self._configurationModel = self._CONFIGURATION_SCHEMA.deserialize(configuration)

    @classmethod
    def initConfigurationsCache(cls):
        cls.getConfigurationByPath(cls._EMPTY_CONFIGURATION_PATH)

    @classmethod
    def getConfigurationByPath(cls, configPath, overridesPath=''):
        global g_configurationsCache
        cacheKey = (
         configPath, overridesPath)
        if cacheKey in g_configurationsCache:
            return g_configurationsCache[cacheKey]
        else:
            section = ResMgr.openSection(configPath)
            if section is None:
                raise SoftException(('[FUN_RANDOM_CONFIGS] Cannot open or read config {}').format(configPath))
            configuration = section2dict.parse(section)
            deepMergeDicts(configuration, cls.getConfigurationByPath(overridesPath) if overridesPath else {})
            g_configurationsCache[cacheKey] = configuration
            ResMgr.purge(configPath, True)
            return configuration

    def getConfigurationModel(self):
        raise NotImplementedError

    def _getRuntimeConfiguration(self, *args):
        raise NotImplementedError
