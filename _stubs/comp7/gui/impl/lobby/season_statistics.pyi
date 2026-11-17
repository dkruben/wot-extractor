# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/season_statistics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import typing as typing
import SoundGroups as SoundGroups
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_UI_SECTION as COMP7_UI_SECTION, COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN as COMP7_LAST_SEASON_WHERE_STATISTICS_SHOWN
from comp7.gui.impl.gen.view_models.views.lobby.constants import Constants as Constants
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName, SeasonPointState as SeasonPointState
from comp7.gui.impl.gen.view_models.views.lobby.season_statistics_model import SeasonStatisticsModel as SeasonStatisticsModel, SummaryStatisticsModel as SummaryStatisticsModel, VehicleStatisticsModel as VehicleStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.summary_statistics_model import SummaryStatisticsType as SummaryStatisticsType
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared
from comp7.gui.impl.lobby.tooltips.season_point_tooltip import SeasonPointTooltip as SeasonPointTooltip
from comp7.gui.shared.gui_items.dossier.stats import getComp7DossierStats as getComp7DossierStats
from comp7_common_const import seasonPointsCodeBySeasonNumber as seasonPointsCodeBySeasonNumber, seasonNameBySeasonNumber as seasonNameBySeasonNumber
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.gen import R as R
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.formatters import calculateWinRate as calculateWinRate
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.web import IWebController as IWebController
from gui.shared.gui_items.dossier.stats import AccountComp7StatsBlock as AccountComp7StatsBlock
SOUND_NAME = 'comp_7_season_statistics_screen_appear'
_logger: Any

class _SeasonStatistics(ViewImpl):
    __slots__: tuple
    __comp7Controller: Any
    __itemsCache: Any
    __webCtrl: Any
    __settingsCore: Any
    __seasonNumber: Any
    __summaryStatistics: Any
    def __init__(self, layoutID, seasonNumber, saveViewing):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *_, **__):
        ...
    def _finalize(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __setComp7SeasonStasisticsShown(self):
        ...
    def __updateData(self):
        ...
    def __updatePersonalData(self, model):
        ...
    def __updateSeasonPoints(self, model):
        ...
    def __updateSummaryStatistics(self, model):
        ...
    def __updateVehicleStats(self, model):
        ...
    @staticmethod
    def __playSound():
        ...
    def __onClose(self):
        ...

class SummarySeasonStat(object):
    _seasonStats: Any
    def __init__(self, seasonStats):
        ...
    @property
    def statType(self):
        ...
    def mainStat(self):
        ...
    def additionalStat(self):
        ...

class BattlesStat(SummarySeasonStat):
    @property
    def statType(self):
        ...
    def mainStat(self):
        ...
    def additionalStat(self):
        ...

class DamageStat(SummarySeasonStat):
    @property
    def statType(self):
        ...
    def mainStat(self):
        ...
    def additionalStat(self):
        ...

class PrestigePointsStat(SummarySeasonStat):
    @property
    def statType(self):
        ...
    def mainStat(self):
        ...
    def additionalStat(self):
        ...

class FragsStat(SummarySeasonStat):
    @property
    def statType(self):
        ...
    def mainStat(self):
        ...
    def additionalStat(self):
        ...

class WinSeriesStat(SummarySeasonStat):
    @property
    def statType(self):
        ...
    def mainStat(self):
        ...
    def additionalStat(self):
        ...

class SeasonStatisticsWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, seasonNumber, saveViewing, parent=None):
        ...
