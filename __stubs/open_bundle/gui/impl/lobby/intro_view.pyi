# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowLayer as WindowLayer, WindowFlags as WindowFlags
from gui.shared import g_eventBus as g_eventBus, events as events
from open_bundle.helpers.account_settings import setIntroShown as setIntroShown
from open_bundle.gui.impl.gen.view_models.views.lobby.intro_view_model import IntroViewModel as IntroViewModel
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController as IOpenBundleController
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from helpers import dependency as dependency

class Intro(ViewImpl):
    __openBundle: Any
    __bundleID: Any
    def __init__(self, layoutID, model, bundleID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def _bundle(self):
        ...
    def _onLoading(self, *arg, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onStatusChanged(self, *_):
        ...
    def __onClose(self):
        ...
    def __onExternalLink(self):
        ...

class IntroWindow(WindowImpl):
    def __init__(self, bundleID):
        ...
