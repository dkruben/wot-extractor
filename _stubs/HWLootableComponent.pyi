# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/HWLootableComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from halloween.gui.shared.events import HWBattleLootEvent as HWBattleLootEvent
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from Event import Event as Event, EventManager as EventManager

class HWLootableComponent(DynamicScriptComponent):
    _eManager: Any
    onStartCapturing: Any
    onStopCapturing: Any
    onCapturingEntitiesChanged: Any
    def __init__(self, *args, **kwargs):
        ...
    def set_isCapturing(self, *args, **kwargs):
        ...
    def set_looterEntities(self, *args, **kwargs):
        ...
    def onDestroy(self):
        ...
    def onVehicleStartCapturing(self, vehID):
        ...
    def onVehicleCancelCapturing(self, vehID):
        ...
    def onLootCapturingSucceeded(self, vehID, vehIDs):
        ...
    def _onInitialised(self):
        ...
    def _capturingUpdate(self):
        ...
