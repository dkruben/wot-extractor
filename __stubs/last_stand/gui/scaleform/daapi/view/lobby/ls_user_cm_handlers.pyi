# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/ls_user_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import adisp as adisp
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.lobby.rally.UnitUserCMHandler import UnitUserCMHandler as UnitUserCMHandler
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import USER as USER, AppealCMHandler as AppealCMHandler
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from last_stand.gui.ls_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from last_stand.gui.shared.event_dispatcher import showHangar as showHangar
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand_common.last_stand_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
CREATE_LS_SQUAD = 'createLSSquad'
EXCLUDE_CM_CLASS: tuple
HIGHLIGHT_COLOR = 13347959

class LSAppealCMHandler(AppealCMHandler):
    def onOptionSelect(self, optionId):
        ...

# decorador original: @adisp.adisp_process
# decorador original: @dependency.replace_none_kwargs(...)
def createLSSquadHandler(cm, ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def lsSquadOptionBuilder(cm, options, userCMInfo, ctrl=None):
    ...
