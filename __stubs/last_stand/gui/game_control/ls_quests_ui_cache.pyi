# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/ls_quests_ui_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
from future.utils import viewitems as viewitems
from constants import EVENT_CLIENT_DATA as EVENT_CLIENT_DATA
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from helpers import dependency as dependency
from last_stand.skeletons.ls_quests_ui_cache import ILSQuestsUICache as ILSQuestsUICache
from last_stand_common.last_stand_constants import LS_QUESTS_PREFIX as LS_QUESTS_PREFIX
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Optional as Optional, Dict as Dict, Callable as Callable
from gui.server_events.event_items import Quest as Quest
from gui.shared.events import GUICommonEvent as GUICommonEvent

class LSQuestsUICache(ILSQuestsUICache):
    _eventsCache: Any
    _cache: Any
    onCacheUpdated: Any
    onSyncCompleted: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def getQuests(self, filterFunc=None):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def _onQuestsUpdated(self, _):
        ...
    def _updateCache(self):
        ...
    def _onSyncCompleted(self, *_):
        ...
