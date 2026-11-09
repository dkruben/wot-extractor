# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/buy_vehicle_option_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_price_model import BuyVehiclePriceModel as BuyVehiclePriceModel
from gui.impl.gen.view_models.views.lobby.hangar.buy_vehicle_simple_tooltip_model import BuyVehicleSimpleTooltipModel as BuyVehicleSimpleTooltipModel

class OptionState(Enum):
    DEFAULT = 'default'
    WARNING = 'warning'
    SELECTED = 'selected'
    DISABLED = 'disabled'

class BuyVehicleOptionModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=7, commands=0):
        ...
    @property
    def price(self):
        ...
    @staticmethod
    def getPriceType():
        ...
    @property
    def tooltip(self):
        ...
    @staticmethod
    def getTooltipType():
        ...
    def getName(self):
        ...
    def setName(self, value):
        ...
    def getOptionState(self):
        ...
    def setOptionState(self, value):
        ...
    def getIcon(self):
        ...
    def setIcon(self, value):
        ...
    def getTitle(self):
        ...
    def setTitle(self, value):
        ...
    def getIsPriceVisible(self):
        ...
    def setIsPriceVisible(self, value):
        ...
    def _initialize(self):
        ...
