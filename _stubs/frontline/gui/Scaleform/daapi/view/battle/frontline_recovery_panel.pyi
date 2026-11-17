# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_recovery_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from frontline.gui.Scaleform.daapi.view.meta.RecoveryPanelMeta import RecoveryPanelMeta as RecoveryPanelMeta
from gui.battle_control.avatar_getter import getSoundNotifications as getSoundNotifications
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _EVENT_ID
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import time_utils as time_utils, i18n as i18n
from constants import RM_STATE as RM_STATE
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND
from gui.battle_control import avatar_getter as avatar_getter
from PlayerEvents import g_playerEvents as g_playerEvents
_SHOW_HINT_TIME = 5
_SHOW_COOLDOWN_TIME = 5

class _CALLBACK_HIDE(object):
    ALL = 0
    HINT = 1
    COOLDOWN = 2

class FrontlineRecoveryPanel(RecoveryPanelMeta):
    sessionProvider: Any
    __hideHintCB: Any
    __hideCooldownCB: Any
    __cooldownTimerCallback: Any
    __nextActionTime: Any
    __recoveryActivated: Any
    __state: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __hideHint(self):
        ...
    def __hideCooldown(self, animate):
        ...
    def __onMappingChanged(self, *args):
        ...
    def __tick(self):
        ...
    def __cancelHideCallback(self, mode):
        ...
    def __playSound(self, eventName):
        ...
    def __onRoundFinished(self, winnerTeam, reason):
        ...
