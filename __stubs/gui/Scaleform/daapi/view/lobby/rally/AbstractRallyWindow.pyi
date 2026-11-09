# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rally/AbstractRallyWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.meta.AbstractRallyWindowMeta import AbstractRallyWindowMeta as AbstractRallyWindowMeta
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction, PrbAction as PrbAction
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared.events import RallyWindowEvent as RallyWindowEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE

class AbstractRallyWindow(AbstractRallyWindowMeta, IPrbListener):
    _viewToLoad: Any
    _viewToUnload: Any
    _currentView: Any
    def __init__(self):
        ...
    def getFlashAliases(self):
        ...
    def getPythonAliases(self):
        ...
    def minimizing(self):
        ...
    def onWindowClose(self):
        ...
    def _getPythonAlias(self, flashAlias):
        ...
    def _requestViewLoad(self, flashAlias, itemID):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _dispose(self):
        ...
    # decorador original: @adisp_process
    def _doLeave(self, isExit=True):
        ...
    # decorador original: @adisp_process
    def _doSelect(self, prebattleActionName, accountsToInvite=None):
        ...
    def __onClose(self, event):
        ...
