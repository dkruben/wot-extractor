# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/field_modification_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel

class FieldModificationModel(ViewModel):
    __slots__: tuple
    HIDDEN = 0
    LOCKED = 1
    UNLOCKED = 2
    onVehiclePostProgression: Any
    def __init__(self, properties=2, commands=1):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getCounter(self):
        ...
    def setCounter(self, value):
        ...
    def _initialize(self):
        ...
