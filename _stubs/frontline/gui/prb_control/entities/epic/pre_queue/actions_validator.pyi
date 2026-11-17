# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic/pre_queue/actions_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frontline.gui.frontline_helpers import isAnnouncedCycleState as isAnnouncedCycleState
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import isVehLevelUnlockableInBattle as isVehLevelUnlockableInBattle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator as BaseActionsValidator, ActionsValidatorComposite as ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator as PreQueueActionsValidator
from gui.prb_control.items import ValidationResult as ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION, PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicVehicleValidator(BaseActionsValidator):
    def _validate(self):
        ...

class EpicActionsValidator(PreQueueActionsValidator):
    __epicController: Any
    __epicVehicleValidator: Any
    def __init__(self, entity):
        ...
    def _createVehiclesValidator(self, entity):
        ...
    def _validate(self):
        ...
