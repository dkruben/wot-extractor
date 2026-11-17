# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/collection/intro_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.collection.intro_view_model import IntroViewModel as IntroViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.collection.account_settings import setIntroShown as setIntroShown
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import isPlayerAccount as isPlayerAccount

class IntroView(ViewImpl):
    __slots__: tuple
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onClose(self):
        ...
