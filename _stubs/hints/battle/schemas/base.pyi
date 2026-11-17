# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/hints/battle/schemas/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT, IS_VS_EDITOR as IS_VS_EDITOR
from dict2model import exceptions as exceptions
from dict2model import fields as fields
from dict2model import models as models
from dict2model import schemas as schemas
from dict2model import validate as validate
from gui import makeHtmlString as makeHtmlString, g_htmlTemplates as g_htmlTemplates
from helpers import i18n as i18n, dependency as dependency
from hints.battle.schemas.const import HTML_TEMPLATE_PATH as HTML_TEMPLATE_PATH, MIN_SHOW_TIME_LOWER_LIMIT as MIN_SHOW_TIME_LOWER_LIMIT, MIN_SHOW_TIME_UPPER_LIMIT as MIN_SHOW_TIME_UPPER_LIMIT, DEFAULT_MIN_SHOW_TIME as DEFAULT_MIN_SHOW_TIME, DEFAULT_WAIT_TIME as DEFAULT_WAIT_TIME, DEFAULT_SHOW_TIME as DEFAULT_SHOW_TIME, DEFAULT_COOLDOWN_TIME as DEFAULT_COOLDOWN_TIME
from hints_common.battle.schemas.base import CommonHintSchema as CommonHintSchema, CommonHintModel as CommonHintModel, HMCPropsType as HMCPropsType, HMCContextType as HMCContextType
from py2to3 import patched_typing as patched_typing
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Optional as Optional
from dict2model.types import ValidatorsType as ValidatorsType
from hints_common.battle.schemas.base import CommonHintPropsSchema as CommonHintPropsSchema
from gui.battle_control.controllers.battle_hints.history import BattleHintsHistory as BattleHintsHistory
_logger: Any
_DEFAULT_DISPLAY_COUNT = 0
CHMTextType: Any
CHMVisualType: Any
CHMSoundType: Any
CHMLifecycleType: Any
CHMHistoryType: Any
CHMType: Any
clientHintTextSchema: Any
clientHintVisualSchema: Any
clientHintSoundSchema: Any
clientHintHistorySchema: Any
clientHintLifecycleSchema: Any
clientHintSchema: Any

class ClientHintTextModel(models.Model):
    __slots__: tuple
    raw: Any
    key: Any
    template: Any
    highlight: Any
    _message: Any
    def __init__(self, raw, key, template, highlight):
        ...
    @property
    def message(self):
        ...
    @staticmethod
    def _createMessage(raw='', key='', template=''):
        ...
    def _reprArgs(self):
        ...

class ClientHintVisualModel(models.Model):
    __slots__: tuple
    image: Any
    def __init__(self, image):
        ...
    def _reprArgs(self):
        ...

class ClientHintSoundModel(models.Model):
    __slots__: tuple
    fx: Any
    notify: Any
    aliveOnly: Any
    def __init__(self, fx, notify, aliveOnly):
        ...
    def createFx(self):
        ...
    def createNotify(self):
        ...
    def createAliveOnly(self):
        ...
    def _createFx(self):
        ...
    def _createNotify(self):
        ...
    def _createAliveOnly(self):
        ...
    def _reprArgs(self):
        ...

class ClientHintLifecycleModel(models.Model):
    __slots__: tuple
    showTime: Any
    minShowTime: Any
    waitTime: Any
    def __init__(self, showTime, minShowTime, waitTime):
        ...
    def _reprArgs(self):
        ...

class ClientHintHistoryModel(models.Model):
    __slots__: tuple
    modifyPriority: Any
    cooldown: Any
    totalDisplayCount: Any
    perBattleCount: Any
    def __init__(self, modifyPriority, cooldown, totalDisplayCount, perBattleCount):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: CommonHintModel[...]
# base nao representavel no stub: patched_typing.Generic[...]
class ClientHintModel:
    __slots__: tuple
    _sessionProvider: Any
    text: Any
    visual: Any
    sound: Any
    lifecycle: Any
    history: Any
    def __init__(self, props, context, text, visual, sound, lifecycle, history):
        ...
    def validate(self, *args, **kwargs):
        ...
    def canBeShown(self, historyStorage=None):
        ...
    def createVO(self, data=None):
        ...
    def _createVO(self, data):
        ...
    def _formatMessage(self, message, data):
        ...
    def _reprArgs(self):
        ...

# base nao representavel no stub: schemas.Schema[...]
class ClientHintTextSchema:
    __slots__: tuple
    def __init__(self, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...

# base nao representavel no stub: schemas.Schema[...]
class ClientHintVisualSchema:
    __slots__: tuple
    def __init__(self, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...

# base nao representavel no stub: schemas.Schema[...]
class ClientHintSoundSchema:
    __slots__: tuple
    def __init__(self, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...

# base nao representavel no stub: schemas.Schema[...]
class ClientHintHistorySchema:
    __slots__: tuple
    def __init__(self, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        ...

# base nao representavel no stub: CommonHintSchema[...]
class ClientHintSchema:
    __slots__: tuple
    textSchema: Any
    visualSchema: Any
    soundSchema: Any
    historySchema: Any
    def __init__(self, modelClass=..., propsSchema=None, contextSchema=None, textSchema=None, visualSchema=None, soundSchema=None, historySchema=None, serializedValidators=None, deserializedValidators=None):
        ...

def validateHintTextKey(key):
    ...
def validateHintTextTemplate(key):
    ...
def validateHintTextModel(model):
    ...
def validateLifecycleModel(model):
    ...
def validateHintModel(model):
    ...
