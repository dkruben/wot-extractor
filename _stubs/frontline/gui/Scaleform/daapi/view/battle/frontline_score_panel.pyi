# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_score_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD
from debug_utils import LOG_ERROR as LOG_ERROR
from frontline.gui.Scaleform.daapi.view.meta.FrontlineScorePanelMeta import FrontlineScorePanelMeta as FrontlineScorePanelMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
from gui.battle_control.controllers.epic_missions_ctrl import PlayerMission as PlayerMission

class FrontlineScorePanel(FrontlineScorePanelMeta):
    sessionProvider: Any
    __hqMsgSent: Any
    __nearestHQ: Any
    __currentTargetID: Any
    __currentTargetType: Any
    __isInFreeSpectatorMode: Any
    __isInRespawn: Any
    __isInHQSector: Any
    __currentMission: Any
    __prebattleTimeSent: Any
    __debugData: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def __onSpectatorModeChanged(self, mode):
        ...
    def __onVehicleDeployed(self):
        ...
    def __onRespawnVisibilityChanged(self, isVisible, fromTab=False):
        ...
    def __onArenaPeriodChange(self, arenaPeriod, endTime, *_):
        ...
    def _dispose(self):
        ...
    def __onHQDestroyed(self, id_):
        ...
    def __onSectorBasePointsUpdate(self, id_, isPlayerTeam, points, capturingStopped, invadersCount, expectedCaptureTime):
        ...
    def __onDestructibleEntityHealthChanged(self, hqID, newHealth, maxHealth, attackerID, attackReason, hitFlags):
        ...
    def __onDestructibleEntityAdded(self, entity):
        ...
    def __onPlayerMissionUpdated(self, mission, _):
        ...
    def __onHQBattleStarted(self):
        ...
    def __onSectorBaseCaptured(self, id_, isPlayerTeam):
        ...
    def __onSectorBaseAdded(self, sectorBase):
        ...
    def __onNearestObjectiveChanged(self, objID, objDistance):
        ...
    def __onPlayerMissionReset(self):
        ...
    def __removeTarget(self):
        ...
    def __updateTarget(self):
        ...
