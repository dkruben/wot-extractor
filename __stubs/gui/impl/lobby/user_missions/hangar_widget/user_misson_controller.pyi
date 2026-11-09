# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/user_misson_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.umg import WeightsModel as WeightsModel
from config_schemas.umg import umgMissionsConfigSchema as umgMissionsConfigSchema
from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from gui.impl.lobby.user_missions.hangar_widget.providers.quest_providers import DailyQuestProvider as DailyQuestProvider, PremiumQuestProvider as PremiumQuestProvider, WeeklyQuestProvider as WeeklyQuestProvider
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from gui.impl.lobby.user_missions.hangar_widget.providers.quest_providers import QuestProviderBase as QuestProviderBase

class MissionLoader(object):
    __slots__: tuple
    providers: Any
    def __init__(self):
        ...
    def addProviders(self, providers):
        ...
    def loadQuests(self):
        ...
    def updateConfig(self, config):
        ...
    def destroy(self):
        ...

class MissionInitializer(object):
    __slots__: tuple
    eventsCache: Any
    loader: Any
    config: Any
    def __init__(self, loader, eventsCache):
        ...
    def initialize(self):
        ...
    def destroy(self):
        ...

class MissionController(object):
    eventsCache: Any
    gameSession: Any
    quests: Any
    initializer: Any
    loader: Any
    onChanged: Any
    def __init__(self):
        ...
    def initData(self):
        ...
    def subscribe(self):
        ...
    def unsubscribe(self):
        ...
    def refresh(self):
        ...
    def getSortedQuests(self):
        ...
    def destroy(self):
        ...
    def _onSyncCompleted(self, *args, **kwargs):
        ...
    def _onPremiumTypeChanged(self, *args, **kwargs):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
