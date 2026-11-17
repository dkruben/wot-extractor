# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/visual_script/voiceover_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from visual_script.block import Block as Block
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script_client.sound_blocks import SoundMeta as SoundMeta

class PlayVoiceover(Block, SoundMeta):
    _in: Any
    _vehicle: Any
    _voiceover: Any
    _delay: Any
    _out: Any
    _finished: Any
    def __init__(self, *args, **kwargs):
        ...
    def validate(self):
        ...
    def _execute(self):
        ...

class StopVoiceover(Block, SoundMeta):
    _in: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
