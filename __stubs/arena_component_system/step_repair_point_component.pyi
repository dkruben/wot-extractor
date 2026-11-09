# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/step_repair_point_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
import Event as Event

class StepRepairPointComponent(ClientArenaComponent):
    stepRepairPoints: Any
    repairPointPlayerActions: Any
    __stepRepairPoints: Any
    __repairPointPlayerAction: Any
    onStepRepairPointAdded: Any
    onStepRepairPointActiveStateChanged: Any
    onStepRepairPointPlayerAction: Any
    def __init__(self, componentSystem):
        ...
    def destroy(self):
        ...
    def addStepRepairPoint(self, stepRepairPoint):
        ...
    def removeStepRepairPoint(self, stepRepairPoint):
        ...
    def stepRepairPointActiveStateChanged(self, stepRepairPoint):
        ...
    def stepRepairPointPlayerAction(self, repairPointIndex, action, nextActionTime, pointsHealed):
        ...
    def getRepairPointPlayerAction(self, repairPointIndex):
        ...
    def getClosestRepairPoint(self, pos):
        ...
