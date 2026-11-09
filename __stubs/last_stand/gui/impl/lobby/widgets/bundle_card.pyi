# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/widgets/bundle_card.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.bundle_card_model import BundleCardModel as BundleCardModel
from last_stand.gui.shared.event_dispatcher import showLSShopBundle as showLSShopBundle
from last_stand.skeletons.ls_shop_controller import ILSShopController as ILSShopController

# base nao representavel no stub: ViewComponent[...]
class BundleCard:
    lsShopCtrl: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __fillModel(self):
        ...
    def __onClick(self, args):
        ...
    def __onBundlesUpdated(self):
        ...
