# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/veh_skill_tree_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from Event import Event as Event
from frameworks_common.state_machine import StateIdsObserver as StateIdsObserver
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import VEH_SKILL_TREE_INTRO_SHOWN as VEH_SKILL_TREE_INTRO_SHOWN
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree_model import VehSkillTreeModel as VehSkillTreeModel
from gui.impl.lobby.vehicle_hub import VehicleHubCtx as VehicleHubCtx, VehSkillTreeProgressionState as VehSkillTreeProgressionState, VehSkillTreePrestigeState as VehSkillTreePrestigeState, VehSkillTreeInitialState as VehSkillTreeInitialState
from gui.impl.lobby.vehicle_hub.sub_presenters.sub_presenter_base import SubPresenterBase as SubPresenterBase
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.prestige_presenter import PrestigePresenter as PrestigePresenter
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.tree_presenter import TreePresenter as TreePresenter
_logger: Any

class _VehicleSkillTreeStatesObserver(StateIdsObserver):
    onNavigationChanged: Any
    def __init__(self):
        ...
    def onEnterState(self, state, event):
        ...

class VehSkillTreeSubPresenter(SubPresenterBase):
    __presenters: Any
    __activeTab: Any
    __lsmObserver: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def currentPresenter(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def initialize(self, vhCtx, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def clear(self):
        ...
    def _getEvents(self):
        ...
    def __onNavigationChanged(self, tabName):
        ...
    @staticmethod
    def __markIntroShowed():
        ...
