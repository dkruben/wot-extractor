# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cgf_script/registration.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
import CGF as CGF
import BigWorld as BigWorld
from future.utils import viewitems as viewitems
g_propertyIndex = 0

class ComponentProperty(object):
    __metadata: Any
    __index: Any
    __baseIndex: Any
    def __init__(self, type=..., value=None, editorName='', **kwarg):
        ...
    def __get__(self, instance, owner=None):
        ...
    def __set__(self, instance, value):
        ...
    def applyIndex(self, shift):
        ...
    @property
    def metadata(self):
        ...
    @property
    def name(self):
        ...
    @name.setter
    def name(self, value):
        ...
    @property
    def ownerName(self):
        ...
    @ownerName.setter
    def ownerName(self, value):
        ...
    @property
    def index(self):
        ...
    def __call__(self, *args, **kwargs):
        ...

def defaultRegistrator(cls):
    ...
def registerComponent(cls):
    ...
def registerReplicableComponent(cls):
    ...
def registerModule(cls):
    ...
def bonusCapsPredicate(caps, spaceID):
    ...
