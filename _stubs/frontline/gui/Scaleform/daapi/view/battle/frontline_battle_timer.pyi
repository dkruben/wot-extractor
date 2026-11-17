# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_battle_timer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frontline.gui.Scaleform.daapi.view.meta.FrontlineBattleTimerMeta import FrontlineBattleTimerMeta as FrontlineBattleTimerMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND, EPIC_OVERTIME_SOUND_NOTIFICATIONS as EPIC_OVERTIME_SOUND_NOTIFICATIONS
from gui.battle_control import avatar_getter as avatar_getter

class FrontlineBattleTimer(FrontlineBattleTimerMeta):
    sessionProvider: Any
    __overtimeEnd: Any
    __overtimeCB: Any
    __overTimeMaxTimeFac: Any
    __overTimeTickingPlaying: Any
    __overTimeActive: Any
    def __init__(self):
        ...
    def _sendTime(self, totalTime):
        ...
    def _setColor(self):
        ...
    def _startTicking(self):
        ...
    def _triggerSoundNotification(self, notificationName):
        ...
    def _stopOvertimeTicking(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onOvertimeStart(self, endTime):
        ...
    def __onOvertimeOver(self):
        ...
    def __overtimeTick(self):
        ...
