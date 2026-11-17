# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_reinforcement_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frontline.gui.Scaleform.daapi.view.meta.FrontlineReinforcementPanelMeta import FrontlineReinforcementPanelMeta as FrontlineReinforcementPanelMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.battle_control.arena_info.interfaces import IArenaPeriodController as IArenaPeriodController
from helpers import time_utils as time_utils
from gui.battle_control.avatar_getter import getSoundNotifications as getSoundNotifications
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND

class FrontlineReinforcementPanel(FrontlineReinforcementPanelMeta, IArenaPeriodController):
    sessionProvider: Any
    __timestampSent: Any
    __timestamp: Any
    __timeCB: Any
    def __init__(self):
        ...
    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __sendTimestamp(self, nextReinforcementTimer):
        ...
    def __onRespawnLivesUpdated(self, playerLives):
        ...
    def __onPeriodChange(self, period):
        ...
    def __onReinforcementTimerUpdated(self, nextReinforcementTimer):
        ...
    def __onTeamRespawnLivesRestored(self, teams):
        ...
    def __onRespawnVisibilityChanged(self, isVisible, fromTab=False):
        ...
    def __playSound(self, eventName):
        ...
    def __tick(self):
        ...
