# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/role_slot_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.price_model import PriceModel as PriceModel
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.feature_tooltip_view_model import FeatureTooltipViewModel as FeatureTooltipViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.role_model import RoleModel as RoleModel

class RoleSlotTooltipViewModel(FeatureTooltipViewModel):
    __slots__: tuple
    def __init__(self, properties=8, commands=0):
        ...
    @property
    def price(self):
        ...
    @staticmethod
    def getPriceType():
        ...
    @property
    def moneyShortage(self):
        ...
    @staticmethod
    def getMoneyShortageType():
        ...
    @property
    def chosenRole(self):
        ...
    @staticmethod
    def getChosenRoleType():
        ...
    def getAvailableRoles(self):
        ...
    def setAvailableRoles(self, value):
        ...
    @staticmethod
    def getAvailableRolesType():
        ...
    def getSlots(self):
        ...
    def setSlots(self, value):
        ...
    @staticmethod
    def getSlotsType():
        ...
    def _initialize(self):
        ...
