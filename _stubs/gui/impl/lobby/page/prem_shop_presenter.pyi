# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/prem_shop_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.page.header.premium_shop_model import PremiumShopModel as PremiumShopModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import OpenLinkEvent as OpenLinkEvent
from helpers import dependency as dependency
from skeletons.gui.login_manager import ILoginManager as ILoginManager

# base nao representavel no stub: ViewComponent[...]
class PremShopPresenter:
    __loginManager: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __onPremShopUpdate(self):
        ...
    def __onOpenExternalPremiumShop(self):
        ...
