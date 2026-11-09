# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/ReplayAccount.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import enum as enum
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from PlayerEvents import g_playerEvents as g_playerEvents
from ReplayEvents import g_replayEvents as g_replayEvents
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
import os as os
_logger: Any
PlayerReplayAccount = ReplayAccount

class State(enum.IntEnum):
    PRE_START_REPLAY = 0
    STARTED_PLAYBACK = 1
    FINISHED_PLAYBACK = 2

class ReplayAccount(BigWorld.Entity):
    connectionMgr: Any
    state: Any
    def __init__(self):
        ...
    def onBecomePlayer(self):
        ...
    def onBecomeNonPlayer(self):
        ...
    def onKickedFromServer(self, reason, kickReasonType, expiryTime):
        ...
    def handleKeyEvent(self, *args, **kwargs):
        ...
    def __onReplayTerminated(self, reason):
        ...
    def __start(self):
        ...
    def __stop(self):
        ...
