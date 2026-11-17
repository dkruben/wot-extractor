# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/mode_selector/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks_common.state_machine import StateFlags as StateFlags
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.impl.lobby.mode_selector.fun_sub_selector_view import FunModeSubSelectorView as FunModeSubSelectorView
from gui.impl.gen import R as R
from gui.impl.lobby.mode_selector.states import ModeSelectorState as ModeSelectorState, EntryState as EntryState
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyStateDescription as LobbyStateDescription
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams as GuiImplViewLoadParams

# decorador original: @ModeSelectorState.parentOf
class FunRandomSubSelectorState(GuiImplViewLobbyState):
    STATE_ID = 'fun_random_sub_selector'
    VIEW_KEY: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _getViewLoadParams(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
