# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/session_stats_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, QUEUE_TYPE as QUEUE_TYPE
from gui.impl.gen.view_models.views.lobby.page.footer.session_stats_model import SessionStatsModel as SessionStatsModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

# base nao representavel no stub: ViewComponent[...]
class SessionStatsPresenter(IGlobalListener):
    __itemsCache: Any
    __lobbyContext: Any
    _supportedModes: Any
    def __init__(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def __onCacheResync(self, reason, _):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __updateSessionStats(self):
        ...
    def __updateBattleCount(self, model):
        ...
