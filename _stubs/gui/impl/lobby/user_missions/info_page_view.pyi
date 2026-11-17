# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/info_page_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.user_missions.info_page_model import InfoPageModel as InfoPageModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.events_helpers import getRerollTimeout as getRerollTimeout
from gui.shared.system_factory import collectDynamicUmgInfoPagePresenters as collectDynamicUmgInfoPagePresenters

# base nao representavel no stub: ViewComponent[...]
class InfoPageView:
    def __init__(self, settings, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _getChildComponents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onViewClose(self):
        ...
