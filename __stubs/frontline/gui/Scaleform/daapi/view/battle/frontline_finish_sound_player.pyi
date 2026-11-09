# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_finish_sound_player.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from typing import Set as Set
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.daapi.view.battle.shared.finish_sound_player import FinishSoundPlayer as FinishSoundPlayer
from gui.battle_control.view_components import IViewComponentsCtrlListener as IViewComponentsCtrlListener
from constants import FINISH_REASON as FINISH_REASON, ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control import avatar_getter as avatar_getter
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND, EPIC_TIME_WWEVENTS as EPIC_TIME_WWEVENTS
_BATTLE_END_SOUND_TIME = 2
_FRONTLINE_SOUND_EVENTS: dict
_FRONTLINE_SOUND_NOTIFICATIONS: dict
_FRONTLINE_SOUND_NOTIFICATION_DELAY: dict

class FrontlineFinishSoundPlayer(FinishSoundPlayer, IViewComponentsCtrlListener):
    __soundID: Any
    __notificationDelayCB: Any
    __playEndSoundDelayCB: Any
    __timeIsOver: Any
    def __init__(self):
        ...
    def updateDeadVehicles(self, aliveAllies, deadAllies, aliveEnemies, deadEnemies):
        ...
    def detachedFromCtrl(self, ctrlID):
        ...
    def setTeamBaseCaptured(self, clientID, playerTeam):
        ...
    def addCapturedTeamBase(self, clientID, playerTeam, timeLeft, invadersCnt):
        ...
    def _playSoundNotification(self, winnerTeam, reason):
        ...
    def _checkTimeCondition(self):
        ...
    def __onEpicRoundFinished(self, winnerTeam, reason):
        ...
