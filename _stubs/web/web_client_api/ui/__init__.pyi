# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from web.web_client_api import w2capi as w2capi, w2c as w2c, W2CSchema as W2CSchema
from web.web_client_api.battle_pass import BattlePassWebApiMixin as BattlePassWebApiMixin
from web.web_client_api.seniority_awards import OpenSeniorityAwardsWebApi as OpenSeniorityAwardsWebApi
from web.web_client_api.ui import hangar as hangar
from web.web_client_api.ui.badges import BadgesWebApiMixin as BadgesWebApiMixin
from web.web_client_api.ui.barracks import BarracksWebApiMixin as BarracksWebApiMixin
from web.web_client_api.ui.battle_royale import OpenBattleRoyaleHangarMixin as OpenBattleRoyaleHangarMixin
from web.web_client_api.ui.boosters import BoostersWindowWebApiMixin as BoostersWindowWebApiMixin
from web.web_client_api.ui.browser import CloseBrowserViewWebApiMixin as CloseBrowserViewWebApiMixin
from web.web_client_api.ui.browser import CloseBrowserWindowWebApiMixin as CloseBrowserWindowWebApiMixin
from web.web_client_api.ui.browser import OpenBrowserOverlayWebApiMixin as OpenBrowserOverlayWebApiMixin, OpenBuyGoldWebApiMixin as OpenBuyGoldWebApiMixin
from web.web_client_api.ui.browser import OpenBrowserWindowWebApiMixin as OpenBrowserWindowWebApiMixin
from web.web_client_api.ui.browser import OpenExternalBrowserWebApiMixin as OpenExternalBrowserWebApiMixin
from web.web_client_api.ui.chat import ChatWebApiMixin as ChatWebApiMixin
from web.web_client_api.ui.clan import ClanWindowWebApiMixin as ClanWindowWebApiMixin
from web.web_client_api.ui.dialogs import DialogsWebApiMixin as DialogsWebApiMixin
from web.web_client_api.ui.frontline import OpenFrontLinePagesMixin as OpenFrontLinePagesMixin
from web.web_client_api.ui.manual import ManualPageWebApiMixin as ManualPageWebApiMixin
from web.web_client_api.ui.maps_training import OpenMapsTrainingMixin as OpenMapsTrainingMixin
from web.web_client_api.ui.menu import UserMenuWebApiMixin as UserMenuWebApiMixin
from web.web_client_api.ui.missions import MissionsWebApiMixin as MissionsWebApiMixin, PersonalMissionsWebApiMixin as PersonalMissionsWebApiMixin
from web.web_client_api.ui.notification import NotificationWebApiMixin as NotificationWebApiMixin
from web.web_client_api.ui.premium import PremiumViewsWebApiMixin as PremiumViewsWebApiMixin
from web.web_client_api.ui.profile import ProfileTabWebApiMixin as ProfileTabWebApiMixin, ProfileWindowWebApiMixin as ProfileWindowWebApiMixin
from web.web_client_api.ui.ranked import OpenRankedPagesMixin as OpenRankedPagesMixin
from web.web_client_api.ui.referral import ReferralProgramPagesMixin as ReferralProgramPagesMixin
from web.web_client_api.ui.shop import ShopWebApiMixin as ShopWebApiMixin
from web.web_client_api.ui.squad import SquadWebApiMixin as SquadWebApiMixin
from web.web_client_api.ui.storage import StorageWebApiMixin as StorageWebApiMixin
from web.web_client_api.ui.strongholds import StrongholdsWebApiMixin as StrongholdsWebApiMixin
from web.web_client_api.ui.tankman import OpenTankmanWebApiMixin as OpenTankmanWebApiMixin
from web.web_client_api.ui.techtree import TechTreeTabWebApiMixin as TechTreeTabWebApiMixin
from web.web_client_api.ui.util import UtilWebApiMixin as UtilWebApiMixin
from web.web_client_api.ui.vehicle import VehicleCompareWebApiMixin as VehicleCompareWebApiMixin
from web.web_client_api.ui.vehicle import VehicleComparisonBasketWebApiMixin as VehicleComparisonBasketWebApiMixin
from web.web_client_api.ui.vehicle import VehiclePreviewWebApiMixin as VehiclePreviewWebApiMixin
from web.web_client_api.ui.vehicle import VehicleSellWebApiMixin as VehicleSellWebApiMixin
from web.web_client_api.ui.waiting import WaitingWebApiMixin as WaitingWebApiMixin

# decorador original: @w2capi(...)
class OpenWindowWebApi(OpenBrowserWindowWebApiMixin, ClanWindowWebApiMixin, ProfileWindowWebApiMixin, OpenExternalBrowserWebApiMixin, VehicleSellWebApiMixin, hangar.HangarWindowsWebApiMixin, BoostersWindowWebApiMixin, ManualPageWebApiMixin, ChatWebApiMixin, SquadWebApiMixin, OpenBrowserOverlayWebApiMixin, PremiumViewsWebApiMixin, OpenBuyGoldWebApiMixin, OpenTankmanWebApiMixin, DialogsWebApiMixin, OpenRankedPagesMixin, OpenSeniorityAwardsWebApi):
    ...

# decorador original: @w2capi(...)
class CloseWindowWebApi(CloseBrowserWindowWebApiMixin):
    ...

# decorador original: @w2capi(...)
class CloseViewWebApi(CloseBrowserViewWebApiMixin):
    ...

# decorador original: @w2capi(...)
class OpenTabWebApi(hangar.HangarTabWebApiMixin, ProfileTabWebApiMixin, VehiclePreviewWebApiMixin, TechTreeTabWebApiMixin, VehicleComparisonBasketWebApiMixin, MissionsWebApiMixin, BarracksWebApiMixin, ShopWebApiMixin, StorageWebApiMixin, StrongholdsWebApiMixin, PersonalMissionsWebApiMixin, BadgesWebApiMixin, OpenFrontLinePagesMixin, ReferralProgramPagesMixin, OpenMapsTrainingMixin, OpenBattleRoyaleHangarMixin, BattlePassWebApiMixin):
    @classmethod
    def addTabIdCallback(cls, tabId, callback):
        ...

# decorador original: @w2capi(...)
class NotificationWebApi(NotificationWebApiMixin):
    ...

# decorador original: @w2capi(...)
class ContextMenuWebApi(UserMenuWebApiMixin):
    ...

# decorador original: @w2capi(...)
class UtilWebApi(UtilWebApiMixin, VehicleCompareWebApiMixin, WaitingWebApiMixin):
    def _utilFini(self):
        ...
