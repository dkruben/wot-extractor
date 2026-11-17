# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/components_base/component_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from py2to3.patched_future import with_metaclass as with_metaclass
from components_base.auto_properties import AutoPropertyInitMetaclass as AutoPropertyInitMetaclass
from components_base.component import Component as Component

# base nao representavel no stub: with_metaclass(...)
class ComponentController:
    _components: Any
    __touchedDescriptors: Any
    __name: Any
    def __init__(self, name=''):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def touchDescriptor(self, descriptorName):
        ...
    def addComponent(self, component, name=''):
        ...
    def removeComponent(self, component):
        ...
    def destroy(self):
        ...
    def reset(self):
        ...
    def registerComponent(self, component):
        ...
