# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/techtree/unlock.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view import dialogs as dialogs
from gui.Scaleform.daapi.view.lobby.techtree.settings import RequestState as RequestState, UnlockStats as UnlockStats
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.impl import backport as backport
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors import Processor as Processor, plugins as proc_plugs
UnlockItemCtx: Any

class UnlockItemConfirmator(proc_plugs.DialogAbstractConfirmator):
    _unlockCtx: Any
    _costCtx: Any
    __itemType: Any
    def __init__(self, unlockCtx, costCtx, activeHandler=None, isEnabled=True):
        ...
    def __del__(self):
        ...
    def _makeMeta(self):
        ...
    def __destroy(self):
        ...
    def __onBlueprintsModeChanged(self, _):
        ...

class UnlockItemValidator(proc_plugs.SyncValidator):
    __unlockCtx: Any
    __costCtx: Any
    def __init__(self, unlockCtx, costCtx, isEnabled=True):
        ...
    def __del__(self):
        ...
    def _validate(self):
        ...

class UnlockItemProcessor(Processor):
    vehTypeCD: Any
    unlockIdx: Any
    def __init__(self, vehTypeCD, unlockIdx, plugins=None):
        ...
    def _request(self, callback):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...

def makeCostCtx(vehXP, xpCost, xpDiscount):
    ...
