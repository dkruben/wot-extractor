# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/siegeEffectsController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
import Math as Math
from constants import VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE
from cgf_script.registration import registerComponent as registerComponent

# decorador original: @registerComponent
class SiegeEffectsController(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False
    SIEGE_IMPULSE = 0.1
    SIEGE_START_NAME = 'siegeStart'
    SIEGE_PROGRESS_NAME = 'siegeProgress'
    __appearance: Any
    __effectManager: Any
    __hasSwitchImpulse: Any
    __state: Any
    __pendingStateChanges: Any
    def __init__(self, appearance, hasSwitchImpulse):
        ...
    def destroy(self):
        ...
    def __shake(self):
        ...
    def onSiegeStateChanged(self, newState):
        ...
    def tick(self):
        ...
