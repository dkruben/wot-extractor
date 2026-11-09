# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/configs/story_mode_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from game_params_common.base_manager import GameParamsSchema as GameParamsSchema
from dict2model import models as models, fields as fields, validate as validate, schemas as schemas
from game_params_common.scope import GameParamsScopeFlags as GameParamsScopeFlags
import datetime as datetime
_bannerSettingsSchema: Any
afkSchema: Any
afkModesSchema: Any
settingsSchema: Any

class EntryPointSettingsModel(models.Model):
    __slots__: tuple
    eventStartAt: Any
    eventEndAt: Any
    def __init__(self, eventStartAt, eventEndAt):
        ...

class SettingsModel(models.Model):
    __slots__: tuple
    enabled: Any
    waitTimeQueue: Any
    hideGameLoadingTimeout: Any
    joinToQueueFromLogin: Any
    afk: Any
    entryPoint: Any
    modeSelectorCardColumn: Any
    modeSelectorCardPriority: Any
    newbieBannerEnabled: Any
    newbieAdvertisingEnabled: Any
    parallaxEnabled: Any
    eventName: Any
    def __init__(self, enabled, waitTimeQueue, hideGameLoadingTimeout, joinToQueueFromLogin, afk, entryPoint, modeSelectorCardColumn, modeSelectorCardPriority, newbieBannerEnabled, newbieAdvertisingEnabled, parallaxEnabled, eventName):
        ...

class AfkModel(models.Model):
    __slots__: tuple
    maxPlayerInactiveTime: Any
    arenaWaitPlayerTime: Any
    def __init__(self, maxPlayerInactiveTime, arenaWaitPlayerTime):
        ...

class AfkModesModel(models.Model):
    __slots__: tuple
    onboarding: Any
    regular: Any
    def __init__(self, onboarding, regular):
        ...
