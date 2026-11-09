# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/gun_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING, Tuple as Tuple
from items.components import legacy_stuff as legacy_stuff
from py2to3.patched_future import with_metaclass as with_metaclass
from soft_exception import SoftException as SoftException
from wrapped_reflection_framework import reflectedNamedTuple as reflectedNamedTuple
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
from items.vehicle_items import Shell as Shell
RecoilEffect: Any

# base nao representavel no stub: with_metaclass(...)
class GunShot:
    __slots__: tuple
    shell: Any
    defaultPortion: Any
    piercingPower: Any
    speed: Any
    gravity: Any
    nominalMaxDistance: Any
    maxDistance: Any
    maxHeight: Any
    def __init__(self, shell, defaultPortion, piercingPower, speed, gravity, maxDistance, maxHeight):
        ...
    def __repr__(self):
        ...
    def copy(self):
        ...
