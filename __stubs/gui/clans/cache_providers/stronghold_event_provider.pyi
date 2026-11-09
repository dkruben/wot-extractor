# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/cache_providers/stronghold_event_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from constants import CLAN_ROLES as CLAN_ROLES
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventEnabled as getStrongholdEventEnabled
from gui.clans.cache_providers.base_provider import BaseProvider as BaseProvider, RequestSettings as RequestSettings, UpdatePeriodType as UpdatePeriodType
from gui.wgcg.clan.contexts import StrongholdEventSettingsCtx as StrongholdEventSettingsCtx
from helpers import time_utils as time_utils
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from typing import Optional as Optional, Dict as Dict
from gui.clans.data_wrapper.stronghold_event import StrongholdEventSettingsData as StrongholdEventSettingsData

class _DataNames(CONST_CONTAINER):
    SETTINGS = 'SETTINGS'

class StrongholdEventProvider(BaseProvider):
    __clanCache: Any
    def __init__(self, clanCache):
        ...
    def start(self):
        ...
    def getSettings(self):
        ...
    def isRunning(self):
        ...
    def canUnfreezeVehicles(self):
        ...
    @property
    def _dataNameContainer(self):
        ...
    @property
    def _isEnabled(self):
        ...
    def _getSettings(self):
        ...
