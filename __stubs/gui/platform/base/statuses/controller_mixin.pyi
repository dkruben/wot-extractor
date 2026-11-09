# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/base/statuses/controller_mixin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import operator as operator
from functools import partial as partial
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.platform.base.statuses.status import Status as Status
from gui.platform.base.statuses.constants import StatusTypes as StatusTypes, DEFAULT_CONTEXT as DEFAULT_CONTEXT
from gui.platform.base.statuses.events_mgr import StatusEventsManager as StatusEventsManager
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class StatusesMixin(object):
    itemsCache: Any
    lobbyContext: Any
    DEFAULT_STATUS: Any
    _statuses: Any
    _statusEventsMgr: Any
    _statusTokens: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    @property
    def statusEvents(self):
        ...
    def getCurrentStatus(self, context=...):
        ...
    def _start(self):
        ...
    def _stop(self):
        ...
    def _getStatus(self, context=...):
        ...
    def _updateStatus(self, status, context=...):
        ...
    def _checkStatusTokens(self, *args, **kwargs):
        ...
    def _onClientUpdated(self, diff, _):
        ...
    @property
    def _serverSettings(self):
        ...
    def _onServerSettingsChanged(self, *_):
        ...
    def _checkIsEnabled(self, _):
        ...
    def _getStatusTokensSettings(self):
        ...
    def _processStatusTokens(self, validator):
        ...
