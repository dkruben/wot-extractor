# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/settings_core/settings_storages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import weakref as weakref
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from AvatarInputHandler.cameras import FovExtended as FovExtended
from adisp import adisp_async as adisp_async
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs import TimerConfirmDialogMeta as TimerConfirmDialogMeta
from gui.shared.utils.monitor_settings import g_monitorSettings as g_monitorSettings
from messenger import g_settings as messenger_settings

class ISettingsStorage(object):
    _manager: Any
    _core: Any
    _settings: Any
    def __init__(self, manager, core):
        ...
    def store(self, setting):
        ...
    def extract(self, settingOption, default=None):
        ...
    def apply(self, restartApproved):
        ...
    def clear(self):
        ...

class ServerSettingsStorage(ISettingsStorage):
    _section: Any
    def __init__(self, manager, core, section):
        ...
    def apply(self, restartApproved):
        ...
    def extract(self, settingOption, default=None):
        ...

class VideoSettingsStorage(ISettingsStorage):
    @property
    def windowMode(self):
        ...
    @windowMode.setter
    def windowMode(self, value):
        ...
    @property
    def resolution(self):
        ...
    @resolution.setter
    def resolution(self, value):
        ...
    @property
    def refreshRate(self):
        ...
    @refreshRate.setter
    def refreshRate(self, value):
        ...
    @property
    def videoMode(self):
        ...
    def videoModeForAdapterOutputIndex(self, adapterOutputIndex):
        ...
    @property
    def windowSize(self):
        ...
    @windowSize.setter
    def windowSize(self, value):
        ...
    @property
    def borderlessSize(self):
        ...
    @borderlessSize.setter
    def borderlessSize(self, value):
        ...
    @property
    def monitor(self):
        ...
    @monitor.setter
    def monitor(self, value):
        ...
    def apply(self, restartApproved):
        ...

class MessengerSettingsStorage(object):
    _proxy: Any
    _settings: Any
    def __init__(self, proxy=None):
        ...
    def store(self, setting):
        ...
    def extract(self, settingOption, default=None):
        ...
    def apply(self, restartApproved):
        ...
    def clear(self):
        ...

class AimSettingsStorage(ISettingsStorage):
    def apply(self, restartApproved):
        ...
    def extract(self, settingOption, key=None, default=None):
        ...

class MarkersSettingsStorage(ISettingsStorage):
    def apply(self, restartApproved):
        ...
    def extract(self, settingOption, key=None, default=None):
        ...

class FOVSettingsStorage(ISettingsStorage):
    __dynamicFOVEnabled: Any
    __FOV: Any
    def __init__(self, manager=None, core=None):
        ...
    def proxyDynamicFOVEnabled(self, option):
        ...
    @property
    def dynamicFOVEnabled(self):
        ...
    @dynamicFOVEnabled.setter
    def dynamicFOVEnabled(self, value):
        ...
    def proxyFOV(self, option):
        ...
    @property
    def FOV(self):
        ...
    @FOV.setter
    def FOV(self, value):
        ...
    def apply(self, restartApproved, forceApply=False):
        ...
