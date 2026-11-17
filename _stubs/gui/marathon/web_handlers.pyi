# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/marathon/web_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from functools import partial as partial
from gui.server_events.events_dispatcher import showMissionsMarathon as showMissionsMarathon
from gui.shared.event_dispatcher import showStorage as showStorage
from web.web_client_api import webApiCollection as webApiCollection, w2capi as w2capi
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi as PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.quests import QuestsWebApi as QuestsWebApi
from web.web_client_api.request.access_token import AccessTokenWebApiMixin as AccessTokenWebApiMixin
from web.web_client_api.request.spa_id import SpaIdWebApiMixin as SpaIdWebApiMixin
from web.web_client_api.request.wgni_token import WgniTokenWebApiMixin as WgniTokenWebApiMixin
from web.web_client_api.rewards import RewardsWebApi as RewardsWebApi
from web.web_client_api.shop import ShopWebApi as ShopWebApi
from web.web_client_api.social import SocialWebApi as SocialWebApi
from web.web_client_api.sound import HangarSoundWebApi as HangarSoundWebApi, SoundStateWebApi as SoundStateWebApi
from web.web_client_api.ui import CloseWindowWebApi as CloseWindowWebApi, NotificationWebApi as NotificationWebApi
from web.web_client_api.sound import SoundWebApi as SoundWebApi
from web.web_client_api.ui import ContextMenuWebApi as ContextMenuWebApi, OpenWindowWebApi as OpenWindowWebApi, VehiclePreviewWebApiMixin as VehiclePreviewWebApiMixin, UtilWebApi as UtilWebApi
from web.web_client_api.ui.hangar import HangarTabWebApiMixin as HangarTabWebApiMixin
from web.web_client_api.ui.missions import MissionsWebApiMixin as MissionsWebApiMixin
from web.web_client_api.ui.profile import ProfileTabWebApiMixin as ProfileTabWebApiMixin
from web.web_client_api.vehicles import VehiclesWebApi as VehiclesWebApi
from web.web_client_api.ui.shop import ShopWebApiMixin as ShopWebApiMixin
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
_DEFAULT_MARATHON_WEB_API_COLLECTION: tuple

# decorador original: @w2capi(...)
class _RequestWebApi(AccessTokenWebApiMixin, WgniTokenWebApiMixin, SpaIdWebApiMixin):
    ...

# decorador original: @w2capi(...)
class _OpenTabWebApi(HangarTabWebApiMixin, ProfileTabWebApiMixin, ShopWebApiMixin, VehiclePreviewWebApiMixin, MissionsWebApiMixin):
    def _getVehicleStylePreviewCallback(self, cmd):
        ...

def createDefaultMarathonWebHandlers():
    ...
