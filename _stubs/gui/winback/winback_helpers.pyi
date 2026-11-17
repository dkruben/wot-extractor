# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/winback/winback_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import Winback as Winback
from adisp import adisp_process as adisp_process
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.impl.gen import R as R
from gui.impl.lobby.winback.winback_leave_mode_dialog_view import WinbackLeaveModeDialogView as WinbackLeaveModeDialogView
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared import g_eventBus as g_eventBus, events as events
from helpers import dependency as dependency

# decorador original: @adisp_process
def leaveWinbackMode(reason, showConfirmDialog=False, callback=None):
    ...
# decorador original: @adisp_process
def selectRandom():
    ...
def getWinbackSetting(settingName):
    ...
def setWinbackSetting(settingName, settingValue):
    ...
def getQuestsFormatterBonusType():
    ...
