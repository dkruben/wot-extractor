# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/progressive_reward_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import IS_LOOT_BOXES_ENABLED as IS_LOOT_BOXES_ENABLED
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import PROGRESSIVE_REWARD_VISITED as PROGRESSIVE_REWARD_VISITED
from gui.Scaleform.daapi.view.meta.ProgressiveRewardWidgetMeta import ProgressiveRewardWidgetMeta as ProgressiveRewardWidgetMeta
from gui.impl import backport as backport
from gui.impl.auxiliary.rewards_helper import getProgressiveRewardVO as getProgressiveRewardVO
from gui.impl.gen import R as R
from gui.shared import events as events
from gui.shared.event_dispatcher import showProgressiveRewardWindow as showProgressiveRewardWindow
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class ProgressiveRewardWidget(ProgressiveRewardWidgetMeta):
    _eventsCache: Any
    _lobbyContext: Any
    _itemsCache: Any
    def onWidgetClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onSyncCompleted(self, *_):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __onItemsCacheSyncCompleted(self, reason, diff):
        ...
    def __update(self):
        ...
