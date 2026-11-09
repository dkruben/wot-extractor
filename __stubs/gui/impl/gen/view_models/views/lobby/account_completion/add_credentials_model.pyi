# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/account_completion/add_credentials_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_wgnp_overlay_view_model import BaseWgnpOverlayViewModel as BaseWgnpOverlayViewModel
from gui.impl.gen.view_models.views.lobby.account_completion.common.field_email_model import FieldEmailModel as FieldEmailModel

class AddCredentialsModel(BaseWgnpOverlayViewModel):
    __slots__: tuple
    def __init__(self, properties=13, commands=4):
        ...
    @property
    def email(self):
        ...
    @staticmethod
    def getEmailType():
        ...
    def getQuestID(self):
        ...
    def setQuestID(self, value):
        ...
    def getBonuses(self):
        ...
    def setBonuses(self, value):
        ...
    @staticmethod
    def getBonusesType():
        ...
    def getRewardsTitle(self):
        ...
    def setRewardsTitle(self, value):
        ...
    def _initialize(self):
        ...
