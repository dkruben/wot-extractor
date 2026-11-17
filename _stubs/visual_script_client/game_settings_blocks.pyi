# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/game_settings_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from constants import IS_VS_EDITOR as IS_VS_EDITOR
from visual_script import ASPECT as ASPECT
from visual_script.block import Block as Block, Meta as Meta, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.dictionary_blocks import Dictionary as Dictionary
from visual_script.misc import errorVScript as errorVScript, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.tunable_event_block import TunableEventBlock as TunableEventBlock
import Windowing as Windowing
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class GameSettingsMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetGameSetting(Block, GameSettingsMeta):
    _settingTypes: dict
    _name: Any
    _slotType: Any
    _class: Any
    _convertor: Any
    _value: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    def _getValue(self):
        ...

class OnGameSettingsChanged(TunableEventBlock, GameSettingsMeta):
    _EVENT_SLOT_NAMES: list
    settingsCore: Any
    _settings: Any
    _lastSettings: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onSettingsChanged(self, diff):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self, res):
        ...

class OnWindowAccessibilityChanged(Block, GameSettingsMeta):
    _out: Any
    _isAccessible: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onWindowAccessibilityChanged(self, isWindowAccessible):
        ...
