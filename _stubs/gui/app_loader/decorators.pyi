# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/app_loader/decorators.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.app_loader.settings import APP_NAME_SPACE as _SPACE
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
__all__: tuple

class app_getter(property):
    appLoader: Any
    _space: Any
    def __init__(self, fget=None, doc=None, space=None):
        ...
    def __get__(self, obj, objType=None):
        ...

class def_lobby(property):
    appLoader: Any
    def __get__(self, obj, objType=None):
        ...

class def_battle(property):
    appLoader: Any
    def __get__(self, obj, objType=None):
        ...

class sf_lobby(app_getter):
    def __init__(self, fget=None, doc=None):
        ...

class sf_battle(app_getter):
    def __init__(self, fget=None, doc=None):
        ...
