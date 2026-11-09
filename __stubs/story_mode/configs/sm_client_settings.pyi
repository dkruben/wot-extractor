# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/configs/sm_client_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import typing as typing
import ResMgr as ResMgr
import section2dict as section2dict
from dict2model import models as models, schemas as schemas, fields as fields, validate as validate, exceptions as exceptions
from soft_exception import SoftException as SoftException
from story_mode_common.story_mode_constants import EventMissionSelector as EventMissionSelector, MissionsDifficulty as MissionsDifficulty, EXTENSION_NAME as EXTENSION_NAME
_CLIENT_SETTINGS_PATH: Any
battlesCountSelectorSchema: Any
missionSelectorsSchema: Any
eventSchema: Any
clientSettingsSchema: Any
_g_clientSettings = None

class BattlesCountSelectorModel(models.Model):
    __slots__: tuple
    normal: Any
    hard: Any
    def __init__(self, normal=0, hard=0):
        ...
    def getDifficulty(self, playerBattles):
        ...

class MissionSelectorsModel(models.Model):
    __slots__: tuple
    active: Any
    default: Any
    withUnlockMission: Any
    battlesCount: Any
    def __init__(self, active=..., default=None, withUnlockMission=None, battlesCount=None):
        ...

class EventModel(models.Model):
    __slots__: tuple
    missionSelectors: Any
    def __init__(self, missionSelectors=None):
        ...

class ClientSettingsModel(models.Model):
    __slots__: tuple
    event: Any
    def __init__(self, event=None):
        ...

def _validateMissionSelectors(selectorsModel):
    ...
def initialize():
    ...
def getClientSettings():
    ...
