# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/user_account_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.subscriptions_model import SubscriptionsModel as SubscriptionsModel
from gui.impl.gen.view_models.views.lobby.page.header.user_info_model import UserInfoModel as UserInfoModel

class UserAccountModel(ViewModel):
    __slots__: tuple
    onOpenAccountDashboard: Any
    def __init__(self, properties=2, commands=1):
        ...
    @property
    def userInfo(self):
        ...
    @staticmethod
    def getUserInfoType():
        ...
    @property
    def subscriptions(self):
        ...
    @staticmethod
    def getSubscriptionsType():
        ...
    def _initialize(self):
        ...
