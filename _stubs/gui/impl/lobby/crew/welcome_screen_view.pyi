# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/welcome_screen_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from .base_crew_view import BaseCrewSubView as BaseCrewSubView
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.welcome_screen_view_model import WelcomeScreenViewModel as WelcomeScreenViewModel
from gui.impl.pub import WindowImpl as WindowImpl

class WelcomeScreenView(BaseCrewSubView):
    __slots__: tuple
    __navigateFrom: Any
    __onCloseCallback: Any
    def __init__(self, layoutID=..., navigateFrom=None, onCloseCallback=None):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onViewClose(self):
        ...
    def _onDisconnected(self):
        ...

class WelcomeScreenViewWindow(WindowImpl):
    def __init__(self, navigateFrom=None, parent=None, onCloseCallback=None):
        ...
