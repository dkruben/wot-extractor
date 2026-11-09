# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_missions_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from frontline.gui.Scaleform.daapi.view.meta.FrontlineMissionsPanelMeta import FrontlineMissionsPanelMeta as FrontlineMissionsPanelMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import time_utils as time_utils
from gui.battle_control.controllers.epic_missions_ctrl import PlayerMission as PlayerMission
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
import BigWorld as BigWorld

class FrontlineMissionsPanel(FrontlineMissionsPanelMeta, CallbackDelayer):
    sessionProvider: Any
    __nearestHQ: Any
    __timeCB: Any
    __currentEndTime: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __killTimeCallback(self):
        ...
    def __startCountdownTimer(self):
        ...
    def __tick(self):
        ...
    def __onPlayerMissionUpdated(self, mission, additionalDescription=None):
        ...
    def __onPlayerMissionReset(self):
        ...
    def __onPlayerMissionTimerSet(self, timeStamp):
        ...
    def __onNearestObjectiveChanged(self, objID, objDistance):
        ...
