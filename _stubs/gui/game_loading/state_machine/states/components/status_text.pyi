# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/components/status_text.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import game_loading_bindings as game_loading_bindings
from frameworks_common.state_machine import StateFlags as StateFlags, StateEvent as StateEvent
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.consts import MilestonesTypes as MilestonesTypes, Milestones as Milestones
from gui.game_loading.state_machine.const import TickingMode as TickingMode
from gui.game_loading.state_machine.models import LoadingMilestoneModel as LoadingMilestoneModel
from gui.game_loading.state_machine.states.base import BaseViewResourcesTickingState as BaseViewResourcesTickingState, BaseTickingState as BaseTickingState
from gui.game_loading.state_machine.states.handlers.milestones import StatusTextMilestonesHandler as StatusTextMilestonesHandler
from gui.game_loading.resources.models import StatusTextModel as StatusTextModel
_logger: Any

class StatusTextStateComponent(BaseViewResourcesTickingState):
    __slots__: tuple
    def _view(self, resource):
        ...

class MilestoneStatusTextStateComponent(BaseTickingState):
    __slots__: tuple
    _milestonesHandler: Any
    _milestone: Any
    _retainMilestones: Any
    def __init__(self, stateID, milestonesSettings, flags=..., tickingMode=..., onCompleteEvent=None):
        ...
    def setRetainMilestones(self, value):
        ...
    def _start(self):
        ...
    def _stop(self):
        ...
    def _onMilestoneReached(self, newMilestone):
        ...
    def _onMilestoneTypeChanged(self, newMilestone):
        ...
    def _task(self):
        ...
    @staticmethod
    def _setStatus(newStatus):
        ...
