# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/sound_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from py2to3.patched_future import with_metaclass as with_metaclass
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass, reflectedNamedTuple as reflectedNamedTuple
__all__: tuple
SoundPair: Any
StatedSounds: Any
HullAimingSound: Any
SoundSiegeModeStateChange: Any

# base nao representavel no stub: with_metaclass(...)
class WWTripleSoundConfig:
    __slots__: tuple
    __eventNames: Any
    def __init__(self, wwsound, wwsoundPC, wwsoundNPC):
        ...
    def _configure(self, wwsound, wwsoundPC, wwsoundNPC):
        ...
    def isEmpty(self):
        ...
    def getEvents(self):
        ...
