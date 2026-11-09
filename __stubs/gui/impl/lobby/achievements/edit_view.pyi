# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/edit_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
import wg_async as future_async
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS as UI_STORAGE_KEYS
from adisp import adisp_process as adisp_process
from constants import AchievementsLayoutStates as AchievementsLayoutStates, Configs as Configs
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.achievements.achievements_helper import fillAchievementSectionModel as fillAchievementSectionModel, fillAchievementModel as fillAchievementModel, convertAchievementsToDbIds as convertAchievementsToDbIds, convertDbIdsToAchievements as convertDbIdsToAchievements
from gui.game_control.wot_plus.service_record_customization.service_record_customization import CdnResourcesCacheManager as CdnResourcesCacheManager, ServiceRecordAssetManager as ServiceRecordAssetManager
from gui.impl.backport import TooltipData as TooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.achievements.dialogs.edit_confirm_model import DialogType as DialogType
from gui.impl.gen.view_models.views.lobby.achievements.views.edit_view_model import EditViewModel as EditViewModel
from gui.impl.lobby.achievements.dialogs.achievement_edit_confirm import showDialog as showDialog
from gui.impl.lobby.achievements.profile_utils import isLayoutEnabled as isLayoutEnabled, isSummaryEnabled as isSummaryEnabled
from gui.impl.lobby.achievements.tooltips.auto_setting_tooltip import AutoSettingTooltip as AutoSettingTooltip
from gui.impl.lobby.achievements.tooltips.editing_tooltip import EditingTooltip as EditingTooltip
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.dossier import dumpDossier as dumpDossier
from gui.shared.gui_items.dossier.achievements.abstract import isRareAchievement as isRareAchievement
from gui.shared.gui_items.processors.achievements import SetAchievementsLayout as SetAchievementsLayout
from helpers import dependency as dependency, server_settings as server_settings
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from shared_utils import nextTick as nextTick
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict

class EditView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __lobbyContext: Any
    __settingsCore: Any
    __wotPlusCtrl: Any
    __dossier: Any
    __isAutoSelect: Any
    __selectedAchievements: Any
    __dialogType: Any
    __initialState: Any
    __achievementBitmask: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillAchievementsModel(self, model=None):
        ...
    def __fillOtherAchievements(self, model):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __fillFirstEntryState(self, model=None):
        ...
    def __getSignificantAchievementsList(self):
        ...
    def __significantAchievements(self):
        ...
    def __getBackportTooltipData(self, name, block):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onChangeAutoSelect(self, model=None):
        ...
    def __isIdenticalToSelectedAchievements(self, achievements):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onReplaceAchievement(self, args, model=None):
        ...
    def __hasChanges(self):
        ...
    def __getAchievementByName(self, name):
        ...
    def __fillSelectedAchievement(self):
        ...
    def __getAchievementsBitmask(self):
        ...
    # decorador original: @adisp_process
    def __onSave(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onCancel(self, model=None):
        ...
    # decorador original: @nextTick
    # decorador original: @future_async.wg_async
    def __onShowExitConfirm(self):
        ...
    def __getConfirmDialogType(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, diff):
        ...
    def __onRenewableSubscriptionStatusChanged(self):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __onHideFirstEntryState(self):
        ...

class EditWindow(LobbyWindow):
    def __init__(self, parent=None, *args, **kwargs):
        ...
