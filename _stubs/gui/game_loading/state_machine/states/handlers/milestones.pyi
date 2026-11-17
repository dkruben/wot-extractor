# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_loading/state_machine/states/handlers/milestones.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from gui.game_loading import loggers as loggers
from gui.game_loading.resources.consts import MilestonesTypes as MilestonesTypes, Milestones as Milestones
from shared_utils import first as first
from gui.game_loading.state_machine.models import LoadingMilestoneModel as LoadingMilestoneModel
_logger: Any

class MilestonesHandler(object):
    __slots__: tuple
    _milestone: Any
    _milestonesSettings: Any
    _time: Any
    onMilestoneReached: Any
    onMilestoneTypeChanged: Any
    _milestones: Any
    def __init__(self, milestonesSettings):
        ...
    def chooseDefaultMilestoneType(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def getCurrentMilestone(self):
        ...
    def _onStandardLoading(self):
        ...
    def _chooseMilestonesType(self, milestonesType):
        ...
    def _onLoadingMilestoneReached(self, milestoneName):
        ...
    def _logTimeDelay(self):
        ...
    def __repr__(self):
        ...

class StatusTextMilestonesHandler(MilestonesHandler):
    __slots__: tuple

class ProgressBarMilestonesHandler(MilestonesHandler):
    __slots__: tuple
