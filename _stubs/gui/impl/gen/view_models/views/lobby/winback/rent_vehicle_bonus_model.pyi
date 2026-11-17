# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/winback/rent_vehicle_bonus_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.winback.vehicle_bonus_model import VehicleBonusModel as VehicleBonusModel

class RentType(Enum):
    TIME = 'time'
    WINS = 'wins'
    BATTLES = 'battles'

class RentVehicleBonusModel(VehicleBonusModel):
    __slots__: tuple
    def __init__(self, properties=21, commands=0):
        ...
    def getRentType(self):
        ...
    def setRentType(self, value):
        ...
    def getRentDuration(self):
        ...
    def setRentDuration(self, value):
        ...
    def _initialize(self):
        ...
