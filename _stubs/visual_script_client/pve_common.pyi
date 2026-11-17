# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/pve_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import IntEnum as IntEnum
from constants import IS_VS_EDITOR as IS_VS_EDITOR
from pve_battle_hud import getPveHudLogger as getPveHudLogger
from visual_script import ASPECT as ASPECT
from visual_script.block import Block as Block
from visual_script.misc import EDITOR_TYPE as EDITOR_TYPE, errorVScript as errorVScript
from visual_script.pve_battle_hud_blocks import PVEBattleHUDMeta as PVEBattleHUDMeta
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import dependency as dependency
_logger: Any

class SettingType(IntEnum):
    GENERAL = 0
    ITEM = 1

class PropertySlotSpec(object):
    __slots__: tuple
    slotName: Any
    slotType: Any
    defaultValue: Any
    editorData: Any
    required: Any
    def __init__(self, slotName, slotType, defaultValue=None, editorData=None, required=False):
        ...

class ClientBattleHUDWidgetSettings(Block, PVEBattleHUDMeta):
    _SETTINGS_MODEL = None
    _WIDGET_TYPE = None
    _SETTINGS_CONFIG: list
    _SETTING_TYPE = None
    _ID_SLOT: Any
    _inSlot: Any
    _outSlot: Any
    _slotSpecs: Any
    _settingsSlots: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def validate(self):
        ...
    def _execute(self):
        ...
    def __makeSettingsSlot(self, slotSpec):
        ...
    @staticmethod
    def __getSettingValue(slot, slotType):
        ...
