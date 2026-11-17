# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/Placement.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from constants import AirdropType as AirdropType
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_ERROR as LOG_ERROR
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from battle_royale.gui.shared.events import AirDropEvent as AirDropEvent
_TYPE_TO_PLACEMENT: dict

class IPlacementHandler(object):
    def onCreated(self, placement):
        ...
    def onDestroyed(self, placement):
        ...

class _AirDropCmpHandler(IPlacementHandler):
    __guiSessionProvider: Any
    __CMP_NAME = 'airDropComponent'
    def _getAirdropCmp(self):
        ...

class _AirdropLootHandler(_AirDropCmpHandler):
    def onCreated(self, placement):
        ...
    def onDestroyed(self, placement):
        ...

class _AirdropBotHandler(_AirDropCmpHandler):
    def onCreated(self, placement):
        ...

class Placement(BigWorld.Entity):
    __handler: Any
    def __init__(self):
        ...
    def onEnterWorld(self, *args):
        ...
    def onLeaveWorld(self):
        ...
