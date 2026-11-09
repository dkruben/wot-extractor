# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/ExtensionsManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import ResMgr as ResMgr
from collections import namedtuple as namedtuple
_EXTENSIONS_RELATIVE_DIR = '../wot_ext'
_EXTENSIONS_ABS_DIR = 'res/wot_ext'
_EXTENSION_PATH_TEMPLATE = '{root}/{extension}/{path}'
_SETTINGS_FORMATTER = '@({})'
_EXT_FORMATTER_ARGUMENT = 'EXTENSION'
_EXT_FORMATTER: Any
_EXTENSION_IMPORT_PATHS: list
Extension: Any
g_extensionsManager: Any

class ExtensionsManager(object):
    __slots__: tuple
    _extensions: Any
    def __init__(self):
        ...
    @property
    def extensions(self):
        ...
    @property
    def activeExtensions(self):
        ...
    @property
    def activePaths(self):
        ...
    def hasExtensions(self):
        ...
    def _readExtensions(self):
        ...
    def getExtensionPath(self, path):
        ...
    @staticmethod
    def _readExtension(root):
        ...
    @staticmethod
    def _getExtensionsDirList():
        ...

def makeExtensionPath(extension, path):
    ...
