# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/request/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from web.web_client_api import w2capi as w2capi
from web.web_client_api.request.access_token import AccessTokenWebApiMixin as AccessTokenWebApiMixin
from web.web_client_api.request.graphics_settings import GraphicsSettingsWebApiMixin as GraphicsSettingsWebApiMixin
from web.web_client_api.request.reactive_communication import ReactiveCommunicationConfigWebApiMixin as ReactiveCommunicationConfigWebApiMixin
from web.web_client_api.request.settings import SettingsWebApiMixin as SettingsWebApiMixin
from web.web_client_api.request.spa_id import SpaIdWebApiMixin as SpaIdWebApiMixin
from web.web_client_api.request.wgni_token import WgniTokenWebApiMixin as WgniTokenWebApiMixin

# decorador original: @w2capi(...)
class RequestWebApi(AccessTokenWebApiMixin, GraphicsSettingsWebApiMixin, ReactiveCommunicationConfigWebApiMixin, SettingsWebApiMixin, SpaIdWebApiMixin, WgniTokenWebApiMixin):
    ...
