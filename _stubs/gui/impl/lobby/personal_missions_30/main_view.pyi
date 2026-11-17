# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_missions_30/main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
import typing as typing
from functools import partial as partial
from future.utils import listvalues as listvalues
from account_helpers.settings_core.settings_constants import PersonalMission3 as PersonalMission3, PersonalMission4 as PersonalMission4
from constants import DAILY_QUESTS_CONFIG as DAILY_QUESTS_CONFIG, Configs as Configs
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleCDForStyle as getVehicleCDForStyle
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl import backport as backport
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.personal_missions_30.additional_mission_model import AdditionalMissionModel as AdditionalMissionModel, AdditionalMissionType as AdditionalMissionType
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory as MissionCategory, OperationState as OperationState
from gui.impl.gen.view_models.views.lobby.personal_missions_30.detail_model import DetailModel as DetailModel, DetailStatus as DetailStatus
from gui.impl.gen.view_models.views.lobby.personal_missions_30.main_view_model import AnimationState as AnimationState, MainScreenState as MainScreenState, MainViewModel as MainViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.main_view_reward_model import MainViewRewardModel as MainViewRewardModel, RewardsType as RewardsType
from gui.impl.gen.view_models.views.lobby.personal_missions_30.mission_model import MissionModel as MissionModel, MissionStatus as MissionStatus
from gui.impl.gen.view_models.views.lobby.personal_missions_30.missions_model import MissionsModel as MissionsModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_model import OperationModel as OperationModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.operation_status_model import OperationStatus as OperationStatus
from gui.impl.gen.view_models.views.lobby.personal_missions_30.quest_model import QuestModel as QuestModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.select_operation_model import SelectOperationModel as SelectOperationModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.personal_missions_30.bonus_packers import getBonusPacker as getBonusPacker, packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from gui.impl.lobby.personal_missions_30.hangar_helpers import AssemblingManager as AssemblingManager
from gui.impl.lobby.personal_missions_30.personal_mission_constants import MAX_DETAIL_ID as MAX_DETAIL_ID, MISSIONS_ROLES_TO_CATEGORIES as MISSIONS_ROLES_TO_CATEGORIES, PERSONAL_MISSIONS_CAMPAIGN_3_SPACE as PERSONAL_MISSIONS_CAMPAIGN_3_SPACE, REWARDS_VIEW_TYPES as REWARDS_VIEW_TYPES, IntroKeys as IntroKeys, SoundsKeys as SoundsKeys
from gui.impl.lobby.personal_missions_30.state import AssemblingState as AssemblingState, MissionsState as MissionsState, ProgressionState as ProgressionState
from gui.impl.lobby.personal_missions_30.tooltips.mission_progress_tooltip import MissionProgressTooltip as MissionProgressTooltip
from gui.impl.lobby.personal_missions_30.tooltips.missions_category_tooltip import MissionsCategoryTooltip as MissionsCategoryTooltip
from gui.impl.lobby.personal_missions_30.views_helpers import getDetailedOperationStatus as getDetailedOperationStatus, getDetailNameByToken as getDetailNameByToken, getMainRewardInfo as getMainRewardInfo, getMissionConfigData as getMissionConfigData, getOperationStatus as getOperationStatus, getQuestsByOperationsChains as getQuestsByOperationsChains, getRegularQuestsPMPoints as getRegularQuestsPMPoints, getBranchSortedPmOperations as getBranchSortedPmOperations, getStageNumberByDetailId as getStageNumberByDetailId, getVehicleDetails as getVehicleDetails, hasAssemblingVideo as hasAssemblingVideo, isIntroShown as isIntroShown, isVehDetailInstalled as isVehDetailInstalled, showRewardVehicleInHangar as showRewardVehicleInHangar, showStageAssemblingVideo as showStageAssemblingVideo, getOperationBannerState as getOperationBannerState, setPMInstalledVehDetails as setPMInstalledVehDetails, getPMInstalledVehDetails as getPMInstalledVehDetails, getPersonalMissionData as getPersonalMissionData, getCheckedPMPointsKey as getCheckedPMPointsKey, setPersonalMissionData as setPersonalMissionData, getCurrentOperationLastInstalledDetail as getCurrentOperationLastInstalledDetail, getBranchesSortedPmOperations as getBranchesSortedPmOperations, checkPM4FirstEntrance as checkPM4FirstEntrance
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.server_events.events_dispatcher import showMissions as showMissions
from gui.server_events.events_helpers import isDailyQuestsEnable as isDailyQuestsEnable, isWeeklyQuestsEnable as isWeeklyQuestsEnable
from gui.server_events.finders import PM_OPERATION_POINTS_TOKEN as PM_OPERATION_POINTS_TOKEN
from gui.shared.event_dispatcher import showHangar as showHangar, showPMAdvancedRewardsWindow as showPMAdvancedRewardsWindow, showVehicleHubOverview as showVehicleHubOverview, showWithoutAwardListOperationIntroWindow as showWithoutAwardListOperationIntroWindow, showStylePreview as showStylePreview
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.processors import quests as quests_proc
from gui.shared.gui_items.processors.quests import PMActivateSeason as PMActivateSeason, PMGetQuestRewards as PMGetQuestRewards
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils import decorators as decorators
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES
from personal_missions import g_cache as pm_cache
from shared_utils import first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IAchievements20EarningController as IAchievements20EarningController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Tuple as Tuple, Set as Set
from gui.server_events.event_items import PMOperation as PMOperation, PersonalMission as PersonalMission
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker

class MainView(ViewImpl):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_CAMPAIGN_3_SPACE
    __eventsCache: Any
    __settingsCore: Any
    __customization: Any
    __lobbyContext: Any
    __itemsCache: Any
    __achievementsController: Any
    __blur: Any
    __initState: Any
    __assemblingManager: Any
    __tooltipData: Any
    __quests: Any
    __needQuestsUpdate: Any
    __campaign: Any
    __campaignOperations: Any
    __operation: Any
    __operationsToUpdate: Any
    __lastInstalledDetail: Any
    __operationStatus: Any
    def __init__(self, layoutID, operationID, state, assemblingManager):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def getOperationID(self):
        ...
    def getBranchID(self):
        ...
    def getBranchName(self):
        ...
    def isCurrentOperationFullCompleted(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def setProgressionState(self):
        ...
    def setMissionsState(self):
        ...
    def setAssemblingState(self):
        ...
    def setAnimationState(self, state):
        ...
    def setCameraFlightInProgress(self, isInProgress):
        ...
    def getMainScreenState(self):
        ...
    def _onFocus(self, focused):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def _finalize(self):
        ...
    def __onCommonSync(self, *_):
        ...
    def __onPmEventsSync(self, diff=None):
        ...
    def __onItemsSyncCompleted(self, _, diff):
        ...
    def __onPmItemsSync(self, *_):
        ...
    def __onSelectOperation(self, data):
        ...
    def __onOperationStatusButtonClick(self):
        ...
    # decorador original: @args2params(...)
    def __onDetailInfo(self, detailId):
        ...
    def __onGoToAssembling(self):
        ...
    def __setFreeCamera(self):
        ...
    # decorador original: @args2params(...)
    def __onClaimDetail(self, detailId):
        ...
    def __pushDetailMessage(self, detailName):
        ...
    # decorador original: @args2params(...)
    def __onMissionShow(self, category):
        ...
    def setMissionViewCategory(self, category):
        ...
    @staticmethod
    def __onAdditionalMissionShow():
        ...
    def __onVehiclePreview(self):
        ...
    def __showVehicleInHangar(self):
        ...
    # decorador original: @args2params(...)
    def __showStylePreview(self, styleId):
        ...
    # decorador original: @args2params(...)
    def __updateAnimationState(self, animationState):
        ...
    def __showRewardVehicle(self):
        ...
    def __setAllOperationsUpdateStatus(self, needUpdate=False):
        ...
    # decorador original: @args2params(...)
    def __changeMissionsCategory(self, category):
        ...
    def __onBack(self):
        ...
    def __showOperationVehicleVideo(self):
        ...
    # decorador original: @args2params(...)
    def __showDetailVideo(self, detailId):
        ...
    def __onServerSettingsChanged(self, diff=None):
        ...
    def __onSettingsChanged(self, diff):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __processOperation(self, branch, operation, questIDS=None):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __switchCampaign(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __claimReward(self, detailName):
        ...
    def __getOperationFromModel(self, operationID):
        ...
    def __updateViewModel(self, operationToUpdate=None):
        ...
    def __fillOperationModel(self, operationModel, operation):
        ...
    def __fillOperationPoints(self, operationModel, operation):
        ...
    def __fillBannerModel(self, bannerModel):
        ...
    def __fillMainRewards(self, operationModel, operation):
        ...
    def __fillDetails(self, operationModel, operation):
        ...
    def __fillRewardTankModel(self, mainViewModel):
        ...
    def __fillMenuItems(self, mainViewModel):
        ...
    def __fillAdditionalMissionsModel(self, operationModel, operation):
        ...
    def __fillActualMissionsModel(self, operationModel, operation):
        ...
    def __updateAllMissions(self):
        ...
    def __updateMissions(self, missions):
        ...
    def __fillMissionModel(self, missionModel, mission, missionIndex, maxMissionNumber, bonusPacker):
        ...
    def __fillRewards(self, rewardsModel, bonuses, packer):
        ...
    def __fillOperationStatusModel(self, mainModel):
        ...
    def __getDetailStatus(self, minDetailPoints, maxDetailPoints, totalPoints, isInstalled, operation, detailIndex):
        ...
    def __getCheckedPmPointsData(self, pmPointsTotal, pmPointsMax):
        ...
    def __setCheckedPMPointsData(self):
        ...

class PersonalMissions3Window(WindowImpl):
    _TRANSPARENT_BACKGROUND_ALPHA = 0.0
    __background_alpha__: Any
    def __init__(self, layer, **kwargs):
        ...
