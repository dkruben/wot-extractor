# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.proto_states import generateBasicHangarStateClasses as generateBasicHangarStateClasses, generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, SFViewLobbyState as SFViewLobbyState, LobbyStateFlags as LobbyStateFlags
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
_logger: Any
HangarState: Any
DefaultHangarState: Any
AllVehiclesState: Any
EasyTankEquipState: Any
LoadoutState: Any
LoadoutConfirmState: Any
LoadoutSectionState: Any
ShellsLoadoutState: Any
EquipmentLoadoutState: Any
InstructionsLoadoutState: Any
ConsumablesLoadoutState: Any

# decorador original: @SubScopeSubLayerState.parentOf
class LegacyHangarState(SFViewLobbyState, IPrbListener):
    STATE_ID = VIEW_ALIAS.LEGACY_LOBBY_HANGAR
    VIEW_KEY: Any
    __LEGACY_HANGAR_MODE_FLAGS: set
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    @classmethod
    def addLegacyHangarFunctionalFlag(cls, flag):
        ...
    def _shouldHijack(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
