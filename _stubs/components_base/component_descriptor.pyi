# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/components_base/component_descriptor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from components_base.auto_properties import AutoProperty as AutoProperty
from components_base.component_controller import ComponentController as ComponentController

class ComponentDescriptor(AutoProperty):
    def __init__(self, fieldName=None):
        ...
    def __set__(self, instance, value):
        ...
    def __setValue(self, instance, value):
        ...
    def __isIterable(self, value):
        ...

class ComponentDescriptorTyped(ComponentDescriptor):
    allowedType: Any
    def __init__(self, allowedType, fieldName=None):
        ...
    def __set__(self, instance, value):
        ...
