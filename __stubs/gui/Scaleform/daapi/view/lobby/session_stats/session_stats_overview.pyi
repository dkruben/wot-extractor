# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/session_stats_overview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import Event as Event
import SoundGroups as SoundGroups
from account_helpers.AccountSettings import AccountSettings as AccountSettings, SESSION_STATS_SECTION as SESSION_STATS_SECTION, SESSION_STATS_PREV_BATTLE_COUNT as SESSION_STATS_PREV_BATTLE_COUNT, BATTLE_EFFICIENCY_SECTION_EXPANDED_FIELD as BATTLE_EFFICIENCY_SECTION_EXPANDED_FIELD
from account_helpers.settings_core.settings_constants import SESSION_STATS as SESSION_STATS
from adisp import adisp_process as adisp_process
from wg_async import wg_async as wg_async, wg_await as wg_await
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frameworks.wulf import WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hof.hof_helpers import getHofAchievementsStatisticUrl as getHofAchievementsStatisticUrl, getHofVehiclesStatisticUrl as getHofVehiclesStatisticUrl, isHofEnabled as isHofEnabled
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_settings_controller import SessionStatsSettingsController as SessionStatsSettingsController
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_views import SessionBattleStatsView as SessionBattleStatsView, SessionVehicleStatsView as SessionVehicleStatsView
from gui.Scaleform.daapi.view.lobby.session_stats.shared import toIntegral as toIntegral
from gui.Scaleform.daapi.view.meta.SessionStatsOverviewMeta import SessionStatsOverviewMeta as SessionStatsOverviewMeta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.SESSION_STATS_CONSTANTS import SESSION_STATS_CONSTANTS as SESSION_STATS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.game_control.links import URLMacros as URLMacros
from gui.impl import backport as backport
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.dialogs.builders import ResSimpleDialogBuilder as ResSimpleDialogBuilder, ResPureDialogBuilder as ResPureDialogBuilder
from gui.impl.gen import R as R
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.processors.session_stats import ResetSessionStatsProcessor as ResetSessionStatsProcessor
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
_TabData: Any
_TABS_DATA_ORDERED: list
_TABS_ID: dict
_HOF_URL_BY_TAB_ALIAS: dict

class SessionStatsOverview(SessionStatsOverviewMeta):
    _itemsCache: Any
    _lobbyContext: Any
    _eventsCache: Any
    __settingsController: Any
    _currentTabAlias: Any
    onShowSettings: Any
    __sessionVehicleStatsView: Any
    __sessionBattleStatsView: Any
    _isHofAccessible: Any
    def __init__(self):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def onClickMoreBtn(self):
        ...
    def onClickResetBtn(self):
        ...
    def onClickSettingsBtn(self):
        ...
    def onExpanded(self, value):
        ...
    def onTabSelected(self, alias):
        ...
    def updateData(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    # decorador original: @adisp_process
    def _showHof(self):
        ...
    # decorador original: @wg_async
    def _showStatsResetDialog(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    # decorador original: @adisp_process
    def __resetStats(self):
        ...
    def __updateViewHandler(self, reason, *_):
        ...
    def __makeInitVO(self):
        ...
    def __updateHeaderTooltip(self):
        ...
    def __getTitle(self, battleCnt):
        ...
    def __getHeaderImg(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __getButtonStates(self):
        ...
    def __timeToClearText(self, timeToClear):
        ...
    def __saveCurrentTab(self, alias):
        ...
    def __getSavedTab(self):
        ...
