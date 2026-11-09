# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/lootbox_entry_point_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers.AccountSettings import LOOT_BOXES_HAS_NEW as LOOT_BOXES_HAS_NEW
from constants import IS_LOOT_BOXES_ENABLED as IS_LOOT_BOXES_ENABLED
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.entry_point_view_model import EntryPointViewModel as EntryPointViewModel
from gui.impl.lobby.lootbox_system.base.tooltips.entry_point_tooltip import EntryPointTooltip as EntryPointTooltip
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lootbox_system.base.common import Views as Views, ViewID as ViewID
from helpers import dependency as dependency
from helpers.server_settings import LOOTBOX_SYSTEM_CONFIG as LOOTBOX_SYSTEM_CONFIG
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class LootboxEntryPointPresenter:
    __itemsCache: Any
    __lootBoxes: Any
    __lobbyContext: Any
    def __init__(self):
        ...
    def prepare(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def __getEnabled(self):
        ...
    def __fillEventInfo(self):
        ...
    def __onBoxesCountChanged(self):
        ...
    def __onLootBoxesStatusChanged(self):
        ...
    def __onAvailabilityChanged(self):
        ...
    def __updateBoxesCount(self, model=None):
        ...
    def __updateTime(self, model=None):
        ...
    def __getEventExpireTime(self):
        ...
    def __showMain(self):
        ...
