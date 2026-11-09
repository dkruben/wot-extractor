# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_demo_client/test_client_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
from cgf_demo.demo_category import DEMO_CATEGORY as DEMO_CATEGORY
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
_logger: Any

# decorador original: @registerComponent
class ClientTestComponent(object):
    group = DEMO_CATEGORY
    editorTitle = 'Client Test'
    domain = CGF.Domain.ClientEditor
    stringList: Any
    intList: Any
    floatList: Any
    double: Any
    integer: Any
    string: Any
    transformLink: Any

class ClientTestSystem(CGF.System):
    ClientTestCreated: Any
    TransformAccess: Any
    Reactions: Any
    def update(self):
        ...
