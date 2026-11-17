# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/clans/cache_providers/clan_supply_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from copy import deepcopy as deepcopy
import typing as typing
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getClanSupplyEnabled as getClanSupplyEnabled
from gui.clans.cache_providers.base_provider import RequestSettings as RequestSettings, UpdatePeriodType as UpdatePeriodType, BaseProvider as BaseProvider
from gui.clans.cache_providers.example_responses.clan_supply import EXAMPLE_DATA as EXAMPLE_DATA
from gui.wgcg.clan_supply import contexts as contexts
from gui.clans.data_wrapper.clan_supply import DataNames as DataNames, QuestStatus as QuestStatus, Quest as Quest
from gui.wgnc import g_wgncEvents as g_wgncEvents
from gui.wgnc.settings import WGNC_DATA_PROXY_TYPE as WGNC_DATA_PROXY_TYPE
from helpers import time_utils as time_utils
from shared_utils import findFirst as findFirst, makeTupleByDict as makeTupleByDict
from typing import Optional as Optional, Dict as Dict
from gui.wgnc import proxy_data as proxy_data
from gui.clans.data_wrapper import clan_supply as clan_supply

class ClanSupplyProvider(BaseProvider):
    def start(self):
        ...
    def stop(self, withClear=False):
        ...
    def getProgressionSettings(self, useFake=False):
        ...
    def getProgressionProgress(self, useFake=False):
        ...
    def getQuestsInfo(self, useFake=False):
        ...
    @property
    def _dataNameContainer(self):
        ...
    @property
    def _isEnabled(self):
        ...
    @property
    def _fakeDataStorage(self):
        ...
    def _getSettings(self):
        ...
    def _dataReceived(self, dataName, data):
        ...
    def __onProxyDataItemShow(self, _, item):
        ...
    @staticmethod
    def __questInfoUpdater(cachedData, item):
        ...
