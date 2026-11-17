# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/contexts/ability_context.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from visual_script_client.contexts.vehicle_context import VehicleContextClient as VehicleContextClient
from visual_script.context import vse_event_out as vse_event_out, vse_set_property as vse_set_property, vse_get_property as vse_get_property
from visual_script.misc import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE

class AbilityContextClient(VehicleContextClient):
    canActivate: Any
    errorKey: Any
    equipmentName: Any
    def __init__(self, vehicle, equipmentName=None):
        ...
    # decorador original: @vse_get_property(...)
    def getEquipmentName(self):
        ...
    # decorador original: @vse_set_property(...)
    def setCanActivate(self, canActivate):
        ...
    # decorador original: @vse_set_property(...)
    def setErrorKey(self, errorKey):
        ...
    # decorador original: @vse_event_out(...)
    def canActive(self):
        ...
    # decorador original: @vse_event_out(...)
    def onSetErrorState(self, errorState):
        ...
    # decorador original: @vse_event_out(...)
    def ready(self):
        ...
    # decorador original: @vse_event_out(...)
    def active(self):
        ...
    # decorador original: @vse_event_out(...)
    def cooldown(self):
        ...
    # decorador original: @vse_event_out(...)
    def startupCooldown(self):
        ...
    # decorador original: @vse_event_out(...)
    def interrupted(self):
        ...
    # decorador original: @vse_event_out(...)
    def exhausted(self):
        ...
    # decorador original: @vse_event_out(...)
    def preparing(self):
        ...
    # decorador original: @vse_event_out(...)
    def cleanup(self):
        ...
    # decorador original: @vse_event_out(...)
    def unavailable(self):
        ...
    # decorador original: @vse_event_out(...)
    def deploying(self):
        ...
    def notrunning(self):
        ...
