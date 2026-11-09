# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/settings/SettingsWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import Sound as Sound
import functools as functools
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import WGC as WGC
import VOIP as VOIP
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COLOR_SETTINGS_TAB_IDX as COLOR_SETTINGS_TAB_IDX
from account_helpers.settings_core.ServerSettingsManager import LIMITED_UI_KEY as LIMITED_UI_KEY
from account_helpers.settings_core.settings_constants import SETTINGS_GROUP as SETTINGS_GROUP
from constants import MISC_GUI_SETTINGS as MISC_GUI_SETTINGS
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_WARNING as LOG_WARNING
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from account_helpers.counter_settings import getNewSettings as getNewSettings, invalidateSettings as invalidateSettings
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.SETTINGS import SETTINGS as SETTINGS
from gui import DialogsInterface as DialogsInterface, g_guiResetters as g_guiResetters
from gui.limited_ui.lui_rules_storage import LuiRuleTypes as LuiRuleTypes
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils import flashObject2Dict as flashObject2Dict, decorators as decorators, graphics as graphics
from gui.Scaleform.daapi.view.meta.SettingsWindowMeta import SettingsWindowMeta as SettingsWindowMeta
from gui.Scaleform.daapi.view.common.settings.SettingsParams import SettingsParams as SettingsParams
from account_helpers.settings_core import settings_constants as settings_constants
from account_helpers.settings_core.options import APPLY_METHOD as APPLY_METHOD
from helpers import dependency as dependency, server_settings as server_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from gui.Scaleform.genConsts.SETTINGS_DIALOGS import SETTINGS_DIALOGS as SETTINGS_DIALOGS
from gui.shared.formatters import icons as icons
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IAnonymizerController as IAnonymizerController, ILimitedUIController as ILimitedUIController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.battle_hints.newbie_battle_hints_controller import INewbieBattleHintsController as INewbieBattleHintsController
from uilogging.limited_ui.constants import LimitedUILogItem as LimitedUILogItem, LimitedUILogScreenParent as LimitedUILogScreenParent
from uilogging.limited_ui.loggers import LimitedUILogger as LimitedUILogger
from uilogging.newbie_hints.loggers import NewbieHintsSettingsUILogger as NewbieHintsSettingsUILogger, NewbieHintsSettingsTooltipsUILogger as NewbieHintsSettingsTooltipsUILogger
_PAGES: tuple
_PAGES_INDICES: Any
_g_lastTabIdx = 0

class SettingsWindow(SettingsWindowMeta):
    anonymizerController: Any
    settingsCore: Any
    lobbyContext: Any
    limitedUIController: Any
    __redefinedKeyModeEnabled: Any
    __isBattleSettings: Any
    __uiNewbieHintsTooltipLogger: Any
    __uiNewbieHintsLogger: Any
    params: Any
    __currentSettings: Any
    def __init__(self, ctx=None):
        ...
    # decorador original: @proto_getter(...)
    def bwProto(self):
        ...
    def __getSettingsParam(self):
        ...
    def __getSettings(self):
        ...
    def __commitSettings(self, settings=None, restartApproved=False, isCloseWnd=False):
        ...
    def __apply(self, settings, restartApproved=False, isCloseWnd=False):
        ...
    def __restartGame(self):
        ...
    def _populate(self):
        ...
    def _update(self):
        ...
    def _dispose(self):
        ...
    def onTabSelected(self, tabId):
        ...
    def onCounterTargetVisited(self, tabName, subTabName, controlsIDs):
        ...
    def onSettingsChange(self, settingName, settingValue):
        ...
    def applySettings(self, settings, isCloseWnd):
        ...
    def _applySettings(self, settings, isCloseWnd):
        ...
    def onWindowClose(self):
        ...
    def onRecreateDevice(self):
        ...
    def autodetectQuality(self):
        ...
    def autodetectAcousticType(self):
        ...
    def autodetectPhysicsSoundQuality(self):
        ...
    def canSelectAcousticType(self, index):
        ...
    def canSelectPhysicsSoundQuality(self, optionIdx):
        ...
    def startVOIPTest(self, isVoiceTestStarted):
        ...
    # decorador original: @decorators.adisp_process(...)
    def updateCaptureDevices(self):
        ...
    def altVoicesPreview(self):
        ...
    def altBulbPreview(self, sampleID):
        ...
    def artyBulbPreview(self, sampleID):
        ...
    def stopVoicesPreview(self):
        ...
    def stopAltBulbPreview(self):
        ...
    def stopArtyBulbPreview(self):
        ...
    def isSoundModeValid(self):
        ...
    def showWarningDialog(self, dialogID, settings, isCloseWnd):
        ...
    def openGammaWizard(self, x, y, size):
        ...
    def openColorSettings(self):
        ...
    def restartNewbieBattleHints(self):
        ...
    def __updateInterfaceScale(self):
        ...
    def __isGraphicsPresetApplied(self, settings):
        ...
    def __onSettingsChanged(self, diff):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingChanged(self, diff):
        ...
    def __refreshSettings(self, **_):
        ...
    def __setColorGradingTechnique(self, value=None):
        ...
    def __setLimitedUISettingVisibility(self):
        ...
    def __applyLimitedUISetting(self):
        ...
    def __setPhysicsSoundVisibility(self):
        ...
    def __updateNewSettingsCounters(self):
        ...

def _getLastTabIndex():
    ...
def _setLastTabIndex(idx):
    ...
def _delayCall(delay, function):
    ...
