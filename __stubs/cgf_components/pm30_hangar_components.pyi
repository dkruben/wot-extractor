# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/cgf_components/pm30_hangar_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CGF as CGF
import Event as Event
from cgf_components.hover_component import SelectionComponent as SelectionComponent
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, event_bus as event_bus
from typing import Callable as Callable, Optional as Optional
PERSONAL_MISSIONS_SUB_HANGAR_IS_READY = 'pmSubHangarIsReady'
OPERATION = 'operation{}'
VEHICLE_FOR_OPERATION = 'vehicleForOperation{}'
STAGES_COMPONENT_FOR_OPERATION = 'stagesComponentForOperation{}'
OPERATION_IDS_RANGE: Any
STAGES_RANGE: Any
Fades: Any
Stages: Any

# decorador original: @registerComponent
class HangarOperationsComponent(object):
    editorTitle = 'Operations links'
    category = 'PersonalMissions 3.0'
    domain = CGF.Domain.ClientEditor
    operation8: Any
    operation9: Any
    operation10: Any
    operation11: Any
    def getOperationObject(self, operationID):
        ...

# decorador original: @registerComponent
class PersonalMissionsSelectionComponent(object):
    editorTitle = 'PM Selection'
    category = 'PersonalMissions 3.0'
    domain = CGF.Domain.ClientEditor

# decorador original: @registerComponent
class AssemblingStagesComponent(Stages):
    editorTitle = 'Assembling Stages'
    category = 'PersonalMissions 3.0'
    domain = CGF.Domain.ClientEditor
    cape: Any
    support: Any

class HangarOperationsSystem(CGF.System):
    HangarOperationActivated: Any
    HangarOperationDeactivated: Any
    HangarOperationIterate: Any
    MissionSelectionActivated: Any
    MissionSelectionDeactivated: Any
    StagesAccess: Any
    Reactions: Any
    onVehicleClick: Any
    gameObjectsAreRemoved: Any
    timers: Any
    def __init__(self):
        ...
    def update(self):
        ...
    def onHangarOperationRemoved(self, stagesAccess):
        ...
    def onHangarOperationAdded(self, hangarOperationsComponent, stagesAccess):
        ...
    def onSelectionAdded(self, selectionComponent):
        ...
    def onSelectionRemoved(self, selectionComponent):
        ...
    def tick(self):
        ...
    def addTimer(self, timerName, duration, callback):
        ...
    def setVehicleGOForOperation(self, operationID, vehicleGO):
        ...
    def setStagesForOperation(self, stagesAccess, operationID, vehicleGO):
        ...
    def getVehicleForOperation(self, operationID):
        ...
    def getStagesForOperation(self, operationID):
        ...
    def onVehicleClickAction(self):
        ...

def getComponentProperties(stageKey):
    ...
