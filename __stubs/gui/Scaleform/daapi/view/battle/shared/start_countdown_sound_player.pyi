# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/start_countdown_sound_player.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import WWISE as WWISE
from helpers import dependency as dependency
import BattleReplay as BattleReplay
from gui.battle_control.battle_constants import COUNTDOWN_STATE as COUNTDOWN_STATE
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from gui.battle_control.view_components import IViewComponentsCtrlListener as IViewComponentsCtrlListener
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any
_RTPC = 'RTPC_ext_battle_countdown_timer'

class StartCountdownSoundPlayer(IAbstractPeriodView, IViewComponentsCtrlListener):
    __soundID: Any
    def __init__(self):
        ...
    def setCountdown(self, state, timeLeft):
        ...
    def __updateSound(self, timeLeft):
        ...
    def __checkNotReplay(self):
        ...
    def __playSound(self, timeLeft):
        ...
