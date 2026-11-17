# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/base.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import Union as Union
from gui.impl.gen.view_models.views.lobby.account_dashboard.account_dashboard_model import AccountDashboardModel as AccountDashboardModel

class FeatureItem(object):
    _viewModel: Any
    def __init__(self, viewModel):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createPopOverContent(self, event):
        ...
    def _fillModel(self, model):
        ...
    def fill(self, ctx=None):
        ...
    def getViewModel(self):
        ...
