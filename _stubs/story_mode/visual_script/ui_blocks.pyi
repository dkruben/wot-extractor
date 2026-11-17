# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/visual_script/ui_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import aih_constants as aih_constants
from visual_script.misc import errorVScript as errorVScript
from visual_script.block import Block as Block
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script_client.battle_hud_block import BattleHUDEventMeta as BattleHUDEventMeta
from constants import IS_EDITOR as IS_EDITOR
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
observers: Any

class ShowWinMessage(Block, BattleHUDEventMeta):
    _in: Any
    _teamSlot: Any
    _reasonSlot: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...

class SetAnimatedHintPenetrationMessage(Block, BattleHUDEventMeta):
    _SHOT_RESULT_TO_PIERCING_CHANCE_HINT: dict
    _in: Any
    _penetration: Any
    _isColorBlind: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def validate(self):
        ...
    def _execute(self):
        ...
