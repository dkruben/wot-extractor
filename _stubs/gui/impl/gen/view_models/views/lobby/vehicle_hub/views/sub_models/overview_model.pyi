# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/overview_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel as VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel as SlotModel

class BenefitsEnum(Enum):
    EXPERIENCE = 'experience'
    CREDITS = 'credits'
    CREWS_TRAIN = 'crewsTrain'
    REPAIR_KIT = 'repairKit'
    BONDS = 'bonds'

class OverviewModel(ViewModel):
    __slots__: tuple
    onWatchMechanicsVideo: Any
    def __init__(self, properties=5, commands=1):
        ...
    def getMechanics(self):
        ...
    def setMechanics(self, value):
        ...
    @staticmethod
    def getMechanicsType():
        ...
    def getHistoricalReference(self):
        ...
    def setHistoricalReference(self, value):
        ...
    def getCustomDescription(self):
        ...
    def setCustomDescription(self, value):
        ...
    def getCrew(self):
        ...
    def setCrew(self, value):
        ...
    @staticmethod
    def getCrewType():
        ...
    def getBenefits(self):
        ...
    def setBenefits(self, value):
        ...
    @staticmethod
    def getBenefitsType():
        ...
    def _initialize(self):
        ...
