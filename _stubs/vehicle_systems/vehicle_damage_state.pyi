# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/vehicle_damage_state.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants

class VehicleDamageState(object):
    MODEL_STATE_NAMES: tuple
    __healthToStateMap: dict
    __stateToModelEffectsMap: dict
    state: Any
    modelState: Any
    isCurrentModelDamaged: Any
    isCurrentModelUndamaged: Any
    isCurrentModelExploded: Any
    isAlive: Any
    isCrewDeath: Any
    isSubmersionDeath: Any
    isCrewActive: Any
    effect: Any
    __state: Any
    __model: Any
    __effect: Any
    @staticmethod
    def getState(health, isCrewActive, isUnderWater):
        ...
    @staticmethod
    def getStateParams(state):
        ...
    @staticmethod
    def isDamagedModel(model):
        ...
    @staticmethod
    def isUndamagedModel(model):
        ...
    @staticmethod
    def isExplodedModel(model):
        ...
    def __init__(self):
        ...
    def update(self, health, isCrewActive, isUnderWater):
        ...
