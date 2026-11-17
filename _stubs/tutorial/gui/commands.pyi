# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/gui/commands.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import types as types
from tutorial.control import g_tutorialWeaver as g_tutorialWeaver
from tutorial.logger import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
__all__: tuple

class GUICommand(object):
    def invoke(self, gui, cmdData):
        ...

class _PyDummyMethod(GUICommand):
    def invoke(self, gui, cmdData):
        ...

class _PyInvokeMethod(GUICommand):
    def _py_searchMethod(self, gui, cmdData):
        ...
    def invoke(self, gui, cmdData):
        ...

class _PyNoGuiInvokeMethod(GUICommand):
    def invoke(self, _, cmdData):
        ...

class GUICommandsFactory(object):
    __typeMap: Any
    def __init__(self, typeMap=None):
        ...
    def _factory(self, cmdType):
        ...
    def invoke(self, root, data):
        ...
