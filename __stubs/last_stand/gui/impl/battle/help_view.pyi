# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/battle/help_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer, ViewModel as ViewModel
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class HelpView(ViewImpl):
    _appLoader: Any
    _sessionProvider: Any
    def __init__(self):
        ...
    @classmethod
    def getLayoutId(cls):
        ...
    @property
    def _battleApp(self):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...

class HelpWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
