# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/close_confiramtor_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import adisp as adisp
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.gen import R as R
from gui.prb_control.entities.base.ctx import LeavePrbAction as LeavePrbAction
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class CloseConfirmatorsHelper(object):
    __slots__: tuple
    _lobbyContext: Any
    __closeConfirmator: Any
    def __init__(self):
        ...
    def getRestrictedEvents(self):
        ...
    def getRestrictedSfViews(self):
        ...
    def getRestrictedGuiImplViews(self):
        ...
    def start(self, closeConfirmator):
        ...
    def stop(self):
        ...
    def _addPlatoonCreationConfirmator(self):
        ...
    def _deletePlatoonCreationConfirmator(self):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @wg_async
    def __confirmEvent(self, event, callback):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @wg_async
    def __confirmHeaderNavigation(self, callback):
        ...
    # decorador original: @adisp.adisp_async
    # decorador original: @wg_async
    def __confirmPlatoonCreation(self, callback):
        ...
