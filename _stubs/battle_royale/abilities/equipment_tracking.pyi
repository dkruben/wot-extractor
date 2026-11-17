# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/abilities/equipment_tracking.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import CGF as CGF
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent

# decorador original: @registerComponent
class EquipmentAnimatorTrigger(object):
    domain = CGF.Domain.ClientEditor
    activeTrigger: Any
    inactiveTrigger: Any

class EquipmentStateComponent(object):
    state: Any
    __state: Any
    def __init__(self, state):
        ...

class EquipmentTrackerComponent(object):
    __equipmentGameObjects: Any
    __reservedIDs: Any
    def __init__(self):
        ...
    def reserveID(self, equipmentID):
        ...
    def isReserved(self, equipmentID):
        ...
    def startTrack(self, equipmentID, gameObject):
        ...
    def getEquipmentGameObject(self, equipmentID):
        ...
