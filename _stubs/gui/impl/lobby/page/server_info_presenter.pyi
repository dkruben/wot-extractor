# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/server_info_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.page.footer.server_info_model import ServerInfoModel as ServerInfoModel, PingStatus as PingStatus, ColorBlindMode as ColorBlindMode
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, PING_STATUSES as PING_STATUSES
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core import settings_constants as settings_constants
_GUI_PING_STATUS: dict

# base nao representavel no stub: ViewComponent[...]
class ServerInfoPresenter:
    __connectionMgr: Any
    __settingsCore: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getColorBlindMode(self):
        ...
    def _setColorblindSettings(self, *args):
        ...
    def _getEvents(self):
        ...
    def __onServersUpdate(self, _):
        ...
    def __updateModel(self):
        ...
