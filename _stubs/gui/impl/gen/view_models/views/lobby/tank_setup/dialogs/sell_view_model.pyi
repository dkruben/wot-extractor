# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/sell_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel as DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.equipment_price_model import EquipmentPriceModel as EquipmentPriceModel
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.current_balance_model import CurrentBalanceModel as CurrentBalanceModel

class ModuleType(Enum):
    IMPROVED = 'improved'
    TROPHY = 'trophy'
    STANDARD = 'standard'

class SellViewModel(DialogTemplateViewModel):
    __slots__: tuple
    onSell: Any
    onClose: Any
    def __init__(self, properties=10, commands=4):
        ...
    @property
    def equipmentPrice(self):
        ...
    @staticmethod
    def getEquipmentPriceType():
        ...
    @property
    def equipment(self):
        ...
    @staticmethod
    def getEquipmentType():
        ...
    def getModuleType(self):
        ...
    def setModuleType(self, value):
        ...
    def getBalance(self):
        ...
    def setBalance(self, value):
        ...
    @staticmethod
    def getBalanceType():
        ...
    def _initialize(self):
        ...
