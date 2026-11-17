# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/account_dashboard/account_dashboard_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.bonus_xp_model import BonusXpModel as BonusXpModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.dog_tags_model import DogTagsModel as DogTagsModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.excluded_maps_model import ExcludedMapsModel as ExcludedMapsModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.header_model import HeaderModel as HeaderModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.parental_control_model import ParentalControlModel as ParentalControlModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.premium_account_model import PremiumAccountModel as PremiumAccountModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.premium_quests_model import PremiumQuestsModel as PremiumQuestsModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.reserve_stock_model import ReserveStockModel as ReserveStockModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.subscriptions_entry_point_model import SubscriptionsEntryPointModel as SubscriptionsEntryPointModel

class AccountDashboardModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=11, commands=1):
        ...
    @property
    def header(self):
        ...
    @staticmethod
    def getHeaderType():
        ...
    @property
    def dogTags(self):
        ...
    @staticmethod
    def getDogTagsType():
        ...
    @property
    def premiumAccount(self):
        ...
    @staticmethod
    def getPremiumAccountType():
        ...
    @property
    def excludedMaps(self):
        ...
    @staticmethod
    def getExcludedMapsType():
        ...
    @property
    def premiumQuests(self):
        ...
    @staticmethod
    def getPremiumQuestsType():
        ...
    @property
    def reserveStock(self):
        ...
    @staticmethod
    def getReserveStockType():
        ...
    @property
    def bonusXp(self):
        ...
    @staticmethod
    def getBonusXpType():
        ...
    @property
    def parentalControl(self):
        ...
    @staticmethod
    def getParentalControlType():
        ...
    @property
    def subscriptions(self):
        ...
    @staticmethod
    def getSubscriptionsType():
        ...
    def getIsParentalControlEnabled(self):
        ...
    def setIsParentalControlEnabled(self, value):
        ...
    def getIsPlayerSubscriptionsEntrypointHidden(self):
        ...
    def setIsPlayerSubscriptionsEntrypointHidden(self, value):
        ...
    def _initialize(self):
        ...
