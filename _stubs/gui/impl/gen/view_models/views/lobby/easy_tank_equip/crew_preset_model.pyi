# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/easy_tank_equip/crew_preset_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel as TankmanModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel as PresetModel

class CrewPresetType(Enum):
    EXPERIENCED = 'experienced'
    NEW_CREW = 'newCrew'

class CrewPresetModel(PresetModel):
    __slots__: tuple
    def __init__(self, properties=8, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getTankmen(self):
        ...
    def setTankmen(self, value):
        ...
    @staticmethod
    def getTankmenType():
        ...
    def getRecruitsCount(self):
        ...
    def setRecruitsCount(self, value):
        ...
    def _initialize(self):
        ...
