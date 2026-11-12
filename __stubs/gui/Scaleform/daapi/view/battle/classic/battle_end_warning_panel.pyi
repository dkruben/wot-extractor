# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/classic/battle_end_warning_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.daapi.view.meta.BattleEndWarningPanelMeta import BattleEndWarningPanelMeta as BattleEndWarningPanelMeta
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView as IAbstractPeriodView
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_WARNING_TEXT_KEY = '#ingame_gui:battleEndWarning/text'
_SWF_FILE_NAME = 'BattleEndWarningPanel.swf'
_CALLBACK_NAME = 'battle.onLoadEndWarningPanel'

class _WWISE_EVENTS(object):
    APPEAR = 'time_buzzer_01'

class BattleEndWarningPanel(BattleEndWarningPanelMeta, IAbstractPeriodView):
    sessionProvider: Any
    __duration: Any
    __appearTime: Any
    __roundLength: Any
    __isShown: Any
    __warningIsValid: Any
    __currPeriod: Any
    def __init__(self):
        ...
    def isLoaded(self):
        ...
    def setPeriod(self, period):
        ...
    def setTotalTime(self, totalTime):
        ...
    def _dispose(self):
        ...
    def _callWWISE(self, wwiseEventName):
        ...
    def __isAlertTimerInterval(self, totalTime):
        ...
    def __validateWarningTime(self):
        ...
