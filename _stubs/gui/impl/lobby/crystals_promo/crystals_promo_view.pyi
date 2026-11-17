# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crystals_promo/crystals_promo_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings, CRYSTALS_INFO_SHOWN as CRYSTALS_INFO_SHOWN
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, IS_CHINA as IS_CHINA
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBonsDevicesUrl as getBonsDevicesUrl, getBonsVehiclesUrl as getBonsVehiclesUrl, getBonsInstructionsUrl as getBonsInstructionsUrl
from gui.impl.backport.backport_system_locale import getIntegralFormat as getIntegralFormat
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crystals_promo.condition_model import ConditionModel as ConditionModel
from gui.impl.gen.view_models.views.lobby.crystals_promo.crystals_promo_view_model import CrystalsPromoViewModel as CrystalsPromoViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shop import showIngameShop as showIngameShop, Origin as Origin
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency, server_settings as server_settings
from shared_utils import findFirst as findFirst
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_DEFAULT_VEHICLE_PRICE = 1500
_DEFAULT_EQUIPMENT_PRICE = 3000
_DEFAULT_INSTRUCTION_PRICE = 6
_DEFAULT_LEVEL = 10

class CrystalsPromoView(ViewImpl):
    __slots__: tuple
    __lobbyContext: Any
    __appLoader: Any
    __shopUrlsMap: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updateCondition(self, model):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, *_):
        ...
    def __goToShopHandler(self, args=None):
        ...
    @classmethod
    def __fillBattleItemModel(cls, model, item, bonusTypeLabel):
        ...
    @staticmethod
    def __createConditionModel(position, win, defeat):
        ...
