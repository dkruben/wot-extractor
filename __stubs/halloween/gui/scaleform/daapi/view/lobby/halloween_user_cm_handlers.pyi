# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/lobby/halloween_user_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import adisp as adisp
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.daapi.view.lobby.rally.UnitUserCMHandler import UnitUserCMHandler as UnitUserCMHandler
from gui.Scaleform.daapi.view.lobby.lobby_constants import USER as USER
from gui.Scaleform.daapi.view.lobby.user_cm_handlers import AppealCMHandler as AppealCMHandler
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from halloween.gui.halloween_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from halloween.gui.shared.event_dispatcher import showHangar as showHangar
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from halloween_common.halloween_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
CREATE_HALLOWEEN_SQUAD = 'createHalloweenSquad'
EXCLUDE_CM_CLASS: tuple
HIGHLIGHT_COLOR = 13347959

class HWAppealCMHandler(AppealCMHandler):
    __uiLogger: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def onOptionSelect(self, optionId):
        ...

# decorador original: @adisp.adisp_process
# decorador original: @dependency.replace_none_kwargs(...)
def createHalloweenSquadHandler(cm, ctrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def halloweenSquadOptionBuilder(cm, options, userCMInfo, ctrl=None):
    ...
