# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gameplay/listeners.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from frameworks_common.state_machine.events import StringEvent as StringEvent
from skeletons.gameplay import PlayerEventID as PlayerEventID, ReplayEventID as ReplayEventID

class PlayerEventsAdaptor(object):
    __slots__: tuple
    _machine: Any
    def __init__(self, machine):
        ...
    def startListening(self):
        ...
    def stopListening(self):
        ...
    def __onAccountBecomePlayer(self):
        ...
    def __onAccountBecomeNonPlayer(self):
        ...
    def __onAvatarBecomePlayer(self):
        ...
    def __onAvatarBecomeNonPlayer(self):
        ...
    def __onServerReplayEntering(self):
        ...
    def __onServerReplayExiting(self):
        ...
