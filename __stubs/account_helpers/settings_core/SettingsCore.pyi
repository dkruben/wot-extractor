# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/settings_core/SettingsCore.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from account_helpers.settings_core.InterfaceScaleManager import InterfaceScaleManager as InterfaceScaleManager
from account_helpers.settings_core.ServerSettingsManager import ServerSettingsManager as ServerSettingsManager, SETTINGS_SECTIONS as SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import SPGAim as SPGAim, CONTOUR as CONTOUR, ArmorFlashlight as ArmorFlashlight
from adisp import adisp_process as adisp_process
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui.Scaleform.locale.SETTINGS import SETTINGS as SETTINGS
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class SettingsCore(ISettingsCore):
    onOnceOnlyHintsChanged: Any
    onSettingsChanged: Any
    onSettingsApplied: Any
    onSettingsReady: Any
    __serverSettings: Any
    __interfaceScale: Any
    __storages: Any
    __options: Any
    __disabledStorages: Any
    __overriddenUserSettings: Any
    __isReady: Any
    isDeviseRecreated: Any
    isChangesConfirmed: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    @property
    def options(self):
        ...
    @property
    def storages(self):
        ...
    @property
    def interfaceScale(self):
        ...
    @property
    def serverSettings(self):
        ...
    def packSettings(self, names):
        ...
    def getSetting(self, name):
        ...
    def getApplyMethod(self, diff):
        ...
    def applySetting(self, key, value):
        ...
    def previewSetting(self, name, value):
        ...
    def applySettings(self, diff):
        ...
    def revertSettings(self):
        ...
    def isSettingChanged(self, name, value):
        ...
    def applyStorages(self, restartApproved, force=False):
        ...
    # decorador original: @adisp_process
    def confirmChanges(self, confirmators):
        ...
    def clearStorages(self):
        ...
    def setOverrideSettings(self, overrideDict, disableStorages):
        ...
    def unsetOverrideSettings(self):
        ...
    def isReady(self):
        ...
    def __onAccountSettingsChanging(self, key, value):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _getStunSwitch(lobbyContext=None):
    ...
