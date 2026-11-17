# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/idle_crew_bonus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class IdleCrewBonusEnum(Enum):
    DISABLED = 'Disabled'
    ENABLED = 'Enabled'
    ACTIVEONCURRENTVEHICLE = 'ActiveOnCurrentVehicle'
    INCOMPATIBLEWITHCURRENTVEHICLE = 'IncompatibleWithCurrentVehicle'
    ACTIVEONANOTHERVEHICLE = 'ActiveOnAnotherVehicle'
    POSTPROGRESSIONREACHED = 'PostProgressionReached'
    INVISIBLE = 'Invisible'

class IdleCrewBonus(ViewModel):
    __slots__: tuple
    def __init__(self, properties=1, commands=0):
        ...
    def getIdleCrewBonus(self):
        ...
    def setIdleCrewBonus(self, value):
        ...
    def _initialize(self):
        ...
