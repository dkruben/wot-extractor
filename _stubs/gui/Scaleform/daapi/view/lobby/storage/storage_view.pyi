# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/storage_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import LAST_STORAGE_VISITED_TIMESTAMP as LAST_STORAGE_VISITED_TIMESTAMP
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.storage import getSectionsList as getSectionsList
from gui.Scaleform.daapi.view.lobby.storage.sound_constants import STORAGE_SOUND_SPACE as STORAGE_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getStorageShellsData as getStorageShellsData
from gui.Scaleform.daapi.view.meta.StorageViewMeta import StorageViewMeta as StorageViewMeta
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.time_utils import getCurrentTimestamp as getCurrentTimestamp
from shared_utils import first as first
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersNovelty as IOffersNovelty, IOffersDataProvider as IOffersDataProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.storage_novelty import IStorageNovelty as IStorageNovelty

class StorageView(LobbySubView, StorageViewMeta):
    __background_alpha__ = 1.0
    __lobbyContext: Any
    __itemsCache: Any
    __offersProvider: Any
    __storageNovelty: Any
    __offersNovelty: Any
    _COMMON_SOUND_SPACE = STORAGE_SOUND_SPACE
    _AUTO_TAB_SELECT_ENABLE: list
    __sections: Any
    __showDummyScreen: Any
    __isItemsForSellEmpty: Any
    __activeSectionIdx: Any
    __activeTab: Any
    def __init__(self, ctx=None):
        ...
    def onClose(self):
        ...
    def navigateToHangar(self):
        ...
    def findActiveSectionAndTabId(self):
        ...
    def _populate(self):
        ...
    def _invalidate(self, *args, **kwargs):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __initialize(self):
        ...
    def __saveLastTimestamp(self):
        ...
    def __addHandlers(self):
        ...
    def __removeHandlers(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __rebuildSections(self):
        ...
    def __updateWindowForHiddenSection(self, hiddenSectionAlias):
        ...
    def __onBlueprintsModeChanged(self, _):
        ...
    def __onOffersChanged(self):
        ...
    def __onInventoryUpdated(self, diff):
        ...
    def __switchSection(self, sectionName, sectionTab=None, skipRefresh=False):
        ...
    def __findActiveSectionAndTab(self):
        ...
    def __getItemsForSellEmpty(self):
        ...
    def __createSections(self):
        ...
    def __setActiveSectionIdx(self, sectionAlias):
        ...
    def __onStorageNoveltyUpdated(self):
        ...
    def __onOffersNoveltyUpdated(self):
        ...
    def __setTabCounter(self, tabId, value):
        ...
    def __isSectionExist(self, tabId):
        ...
