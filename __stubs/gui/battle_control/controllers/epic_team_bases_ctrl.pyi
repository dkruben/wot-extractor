# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/epic_team_bases_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from debug_utils import LOG_ERROR as LOG_ERROR
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from gui.battle_control.controllers.team_bases_ctrl import BattleTeamsBasesController as BattleTeamsBasesController, makeClientTeamBaseID as makeClientTeamBaseID
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class EpicBattleTeamsBasesController(BattleTeamsBasesController):
    sessionProvider: Any
    __capturedBasesDict: Any
    __currentBaseID: Any
    __currentBaseTeam: Any
    def __init__(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def _teamBaseLeft(self, points, invadersCnt):
        ...
    def _updatePoints(self, clientID):
        ...
    def __invalidateTeamBasePoints(self, baseID, points, timeLeft, invadersCnt, capturingStopped):
        ...
    def _addCapturingTeamBase(self, clientID, playerTeam, points, timeLeft, invadersCnt, capturingStopped):
        ...
    def __invalidateTeamBaseCaptured(self, baseID):
        ...
    def __onPlayerPhysicalLaneUpdated(self, laneID):
        ...
    def __isInMyLane(self, baseID):
        ...
    def __onSectorBaseCaptured(self, baseId, isPlayerTeam):
        ...
    def __onSectorBasePointsUpdate(self, baseId, isPlayerTeam, points, capturingStopped, invadersCount, expectedCaptureTime):
        ...

class EpicBattleTeamsBasesPlayer(EpicBattleTeamsBasesController):
    def _getProgressRate(self):
        ...

def createEpicTeamsBasesCtrl(setup):
    ...
