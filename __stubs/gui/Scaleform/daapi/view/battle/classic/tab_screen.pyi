# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/classic/tab_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewvalues as viewvalues
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from ReplayEvents import g_replayEvents as g_replayEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import SELECTED_QUEST_IN_REPLAY as SELECTED_QUEST_IN_REPLAY
from account_helpers.settings_core.options import QuestsProgressViewType as QuestsProgressViewType
from account_helpers.settings_core.settings_constants import QUESTS_PROGRESS as QUESTS_PROGRESS
from gui.impl import backport as backport
from gui.Scaleform.daapi.view.meta.TabScreenMeta import TabScreenMeta as TabScreenMeta
from gui.Scaleform.genConsts.QUESTSPROGRESS import QUESTSPROGRESS as QUESTSPROGRESS
from gui.Scaleform.locale.INGAME_GUI import INGAME_GUI as INGAME_GUI
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.battle_control.battle_constants import TabsAliases as TabsAliases
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from gui.impl.gen import R as R
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from uilogging.player_satisfaction_rating.loggers import BattleTeamStatsViewLogger as BattleTeamStatsViewLogger
_logger: Any

class TabScreenComponent(TabScreenMeta):
    __settingsCore: Any
    __eventsCache: Any
    __lobbyContext: Any
    sessionProvider: Any
    _uiPlayerSatisfactionRatingLogger: Any
    __tabsMap: Any
    def __init__(self):
        ...
    @property
    def hasTabs(self):
        ...
    def hasTab(self, alias):
        ...
    def setActiveTab(self, tabAlias):
        ...
    def onStatsTableVisibiltyToggled(self, isVisible):
        ...
    def onSelectQuest(self, questID):
        ...
    def _populate(self):
        ...
    @staticmethod
    def _buildTabs(builder):
        ...
    def _dispose(self):
        ...
    def onToggleVisibility(self, isVisible):
        ...
    def _onToggleVisibility(self, isVisible):
        ...
    def __onQuestProgressInited(self):
        ...
    def __onReplayTimeWarpFinished(self):
        ...
    def __onReplayTimeWarpStart(self):
        ...
    def __onSettingsChange(self, diff):
        ...
    def __setQuestTrackingData(self):
        ...
    def __setNoQuestsDescription(self):
        ...

class _TabsBuilder(object):
    __lobbyContext: Any
    __tabs: Any
    def __init__(self):
        ...
    def addStatisticsTab(self):
        ...
    def addPersonalQuestsTab(self):
        ...
    def addBoostersTab(self):
        ...
    def getTabs(self):
        ...
    def __isBoosterProcessingAvailable(self):
        ...
