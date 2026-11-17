# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/skeletons/ls_quests_ui_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.game_control import IGameController as IGameController
from Event import Event as Event
from gui.server_events.event_items import Quest as Quest
from typing import Optional as Optional, Dict as Dict, Callable as Callable

class ILSQuestsUICache(IGameController):
    onCacheUpdated = None
    onSyncCompleted = None
    def getQuests(self, filterFunc=None):
        ...
