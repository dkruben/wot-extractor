# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/clan_supply/main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from functools import partial as partial
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR as GUI_START_BEHAVIOR
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import GuiSettingsBehavior as GuiSettingsBehavior
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.gen.view_models.views.lobby.clan_supply.clan_supply_model import ClanSupplyModel as ClanSupplyModel, ClanSupplyViews as ClanSupplyViews
from gui.impl.gen.view_models.views.lobby.clan_supply.tab_model import TabModel as TabModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.clan_supply.pages.progression_page import ProgressionPage as ProgressionPage
from gui.impl.lobby.clan_supply.pages.quests_page import QuestsPage as QuestsPage
from gui.impl.lobby.clan_supply.sound_helper import getMainSoundSpace as getMainSoundSpace
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showStrongholds as showStrongholds, showBrowserOverlayView as showBrowserOverlayView
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.clan_supply.constants import ClanSupplyLogKeys as ClanSupplyLogKeys
from uilogging.clan_supply.loggers import ClanSupplyEventLogger as ClanSupplyEventLogger
from typing import Optional as Optional
_logger: Any
_SubModelInfo: Any

class MainView(ViewImpl):
    __slots__: tuple
    _COMMON_SOUND_SPACE: Any
    __itemsCache: Any
    __wallet: Any
    __settingsCore: Any
    __tabID2ScreenEventLog: dict
    __tabID2SidebarLog: dict
    __presenterLoader: Any
    __tabId: Any
    __isClosingBySelf: Any
    __uiLogger: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def switchPage(self, tabId, *args, **kwargs):
        ...
    def _onLoading(self, tabId=None, parentScreenLog=None, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    @property
    def __currentPage(self):
        ...
    def __initPages(self):
        ...
    def __clearPages(self):
        ...
    def __updateTabs(self):
        ...
    def __onClose(self):
        ...
    # decorador original: @args2params(...)
    def __onSideBarTabChanged(self, tabId):
        ...
    def __onInfoPageOpen(self):
        ...
    def __tryShowInfoPage(self):
        ...
    def __openInfoPage(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateBalance(self, value=None, model=None):
        ...

class PresenterLazyLoader(object):
    __presentersCache: Any
    __mainView: Any
    __loadersMap: Any
    def __init__(self, mainView):
        ...
    def clear(self):
        ...
    def __getitem__(self, item):
        ...
    def __contains__(self, item):
        ...
    def __tryToLoadPresenter(self, key):
        ...
    def __loadProgression(self):
        ...
    def __loadQuests(self):
        ...
    @staticmethod
    def __makeSubModel(viewAlias, loader):
        ...
