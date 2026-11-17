# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/death_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
import Event as Event
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class DeathScreenController(IArenaVehiclesController, Event.EventsSubscriber):
    sessionProvider: Any
    _SKIP_SCREEN_FOR_TOP_POSITIONS = 0
    _SCREEN_SHOW_DELAY = 0.0
    onShowDeathScreen: Any
    onHideDeathScreen: Any
    onWinnerScreen: Any
    _isShown: Any
    __delayedCB: Any
    def __init__(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def __onVehicleControlling(self, _):
        ...
    def __onPlayerRankUpdated(self, playerRank):
        ...
    def __timeToShowHasCome(self, event):
        ...
    def __clear(self):
        ...
