# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/user_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.comp7_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from comp7.gui.Scaleform.daapi.view.lobby.lobby_constants import USER as USER
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import BaseUserCMHandler as BaseUserCMHandler, UserVehicleCMHandler as UserVehicleCMHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7LeaderboardCMHandler(BaseUserCMHandler):
    def _generateOptions(self, ctx=None):
        ...

def createComp7Squad(cm):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def addComp7SquadInfo(handler, options, userCMInfo, comp7Ctrl=None):
    ...
