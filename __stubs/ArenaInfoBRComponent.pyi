# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/ArenaInfoBRComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import BigWorld as BigWorld
import CGF as CGF
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import vehicles as vehicles
import GenericComponents as GenericComponents
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from battle_royale.gui.shared.events import AirDropEvent as AirDropEvent
from typing import List as List
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV

class ArenaInfoBRComponent(DynamicScriptComponent, CallbackDelayer):
    __guiSessionProvider: Any
    def __init__(self):
        ...
    def _onAvatarReady(self):
        ...
    def onLeaveWorld(self, *args):
        ...
    def notifyLaunchPosition(self, equipmentId, position, launchTime, duration):
        ...
    @property
    def battleRoyaleComponent(self):
        ...
    def __showGuiMarker(self, equipment, position, delay):
        ...
    def __launch(self, equipment, position, duration):
        ...
    def set_nextDropWave(self, prev):
        ...
    def set_defeatedTeams(self, _prev):
        ...
    def set_isRespawnTimeFinished(self, prev):
        ...
