# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/battle_control/controllers/settings_contoller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import ResMgr as ResMgr
import section2dict as section2dict
from dict2model import models as models, schemas as schemas, fields as fields, validate as validate
from gui.battle_control.arena_info.interfaces import IOverrideSettingsController as IOverrideSettingsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore, ISettingsCache as ISettingsCache
_tabSettingsSchema: Any
_overrideControlSchema: Any
_overrideSettingsSchema: Any

class OverrideSettingsController(IOverrideSettingsController):
    __slots__: tuple
    _OVERRIDE_SETTINGS_PATH = 'story_mode/gui/override_settings.xml'
    settingsCore: Any
    settingsCache: Any
    _data: Any
    def __init__(self):
        ...
    @property
    def defaultTab(self):
        ...
    @property
    def disabledTabs(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def __onSettingsReady(self, *_):
        ...

class TabSettingsModel(models.Model):
    __slots__: tuple
    defaultTab: Any
    disabledTabs: Any
    def __init__(self, defaultTab, disabledTabs):
        ...

class OverrideControlModel(models.Model):
    __slots__: tuple
    storage: Any
    option: Any
    group: Any
    value: Any
    def __init__(self, storage, option, group, value):
        ...

class OverrideSettingsModel(models.Model):
    __slots__: tuple
    tabSettings: Any
    overrides: Any
    def __init__(self, tabSettings, overrides):
        ...
