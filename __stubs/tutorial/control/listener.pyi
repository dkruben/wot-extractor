# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/control/listener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader, GuiGlobalSpaceID as GuiGlobalSpaceID

class AppLoaderListener(object):
    appLoader: Any
    __loader: Any
    def __init__(self):
        ...
    def start(self, loader):
        ...
    def stop(self):
        ...
    def __onGUISpaceEntered(self, spaceID):
        ...
    def __onGUISpaceLeft(self, spaceID):
        ...
    def __onGUISpaceBeforeEnter(self, spaceID):
        ...
