# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTechnique.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import PROFILE_TECHNIQUE_MEMBER as PROFILE_TECHNIQUE_MEMBER
from constants import Configs as Configs
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK, MARK_ON_GUN_RECORD as MARK_ON_GUN_RECORD
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.AchievementsUtils import AchievementsUtils as AchievementsUtils
from gui.Scaleform.daapi.view.lobby.hof.hof_helpers import getHofRatingUrlForVehicle as getHofRatingUrlForVehicle, getHofDisabledKeys as getHofDisabledKeys, onServerSettingsChange as onServerSettingsChange, isHofButtonNew as isHofButtonNew, setHofButtonOld as setHofButtonOld
from gui.Scaleform.daapi.view.lobby.hof.web_handlers import createHofWebHandlers as createHofWebHandlers
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import ProfileUtils as ProfileUtils, DetailedStatisticsUtils as DetailedStatisticsUtils, STATISTICS_LAYOUT as STATISTICS_LAYOUT, FALLOUT_STATISTICS_LAYOUT as FALLOUT_STATISTICS_LAYOUT, BATTLE_ROYALE_VEHICLE_STATISTICS_LAYOUT as BATTLE_ROYALE_VEHICLE_STATISTICS_LAYOUT
from gui.Scaleform.daapi.view.lobby.profile.seasons_manager import makeTechniqueSeasonManagers as makeTechniqueSeasonManagers
from gui.Scaleform.daapi.view.meta.ProfileTechniqueMeta import ProfileTechniqueMeta as ProfileTechniqueMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.ACHIEVEMENTS_ALIASES import ACHIEVEMENTS_ALIASES as ACHIEVEMENTS_ALIASES
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS as PROFILE_CONSTANTS
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prestige.prestige_helpers import hasVehiclePrestige as hasVehiclePrestige, getVehiclePrestige as getVehiclePrestige, DEFAULT_PRESTIGE as DEFAULT_PRESTIGE
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.Vehicle import VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED as VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED, getIconResourceName as getIconResourceName
from gui.shared.gui_items.dossier import dumpDossier as dumpDossier
from gui.shared.gui_items.dossier.achievements import isMarkOfMasteryAchieved as isMarkOfMasteryAchieved
from gui.shared.gui_items.dossier.stats import UNAVAILABLE_MARKS_OF_MASTERY as UNAVAILABLE_MARKS_OF_MASTERY
from helpers import i18n as i18n, dependency as dependency
from math_common import round_py2_style_int as round_py2_style_int
from nations import NAMES as NAMES
from shared_utils import findFirst as findFirst
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from soft_exception import SoftException as SoftException
from gui.shared.events import ProfileTechniqueEvent as ProfileTechniqueEvent
_MARK_ON_GUN_MIN_LVL = 5

class ProfileTechnique(ProfileTechniqueMeta):
    comparisonBasket: Any
    lobbyContext: Any
    eventsCache: Any
    _selectedVehicleIntCD: Any
    __prestigeView: Any
    _seasonsManagers: Any
    _battlesType: Any
    def __init__(self, *args):
        ...
    def setSeason(self, seasonId):
        ...
    def requestDossier(self, bType):
        ...
    def showVehiclesRating(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getInitData(self, accountDossier=None, isFallout=False):
        ...
    def _setRatingButton(self):
        ...
    def setSelectedTableColumn(self, index, sortDirection):
        ...
    def invokeUpdate(self):
        ...
    def _getStorageId(self):
        ...
    def _getStorageData(self):
        ...
    def _getDefaultTableHeader(self, isFallout=False, showMarkOfMastery=True):
        ...
    def _createTableBtnInfo(self, iconId, buttonWidth, sortOrder, toolTip, defaultSortDirection, label='', iconSource='', inverted=False, sortType='numeric', showSeparator=True, enabled=True):
        ...
    def _getEmptyScreenLabel(self):
        ...
    def _getNecessaryStats(self, accountDossier=None):
        ...
    def _sendAccountData(self, targetData, accountDossier):
        ...
    def __getTableHeader(self, isFallout):
        ...
    def __getBattleRoyaleTechniqueListVehicles(self, targetData):
        ...
    def __getBattleRoyaleTableHeader(self):
        ...
    def _getTechniqueListVehicles(self, targetData, addVehiclesThatInHangarOnly=False):
        ...
    def __getDefaultVehicleList(self, targetData, addVehiclesThatInHangarOnly=False):
        ...
    def requestData(self, vehicleId):
        ...
    def _receiveVehicleDossier(self, vehicleIntCD, databaseId):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
    def _getLayout(self):
        ...
    def _unpackVehicleParams(self, vehParams):
        ...
    def _isPrestigeVisible(self):
        ...
    def __getAchievementsList(self, targetData, vehDossier, vehDossierDumped):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __dossierResyncHandler(self, *args):
        ...
    def __packAchievement(self, stats, vehDossier, record, vehDossierDumped):
        ...
    def __showMarksOnGun(self, vehicleIntCD):
        ...
