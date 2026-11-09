# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/vehicle_selector.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from fort_rush.gui.impl.battle.fort_rush_vehicle_selector import FortRushVehicleSelectorView as FortRushVehicleSelectorView
from fort_rush.gui.battle_control.controllers.respawn_ctrl import ISpawnListener as ISpawnListener
_logger: Any

class FortRushVehicleSelectorComponent(InjectComponentAdaptor, ISpawnListener):
    def _makeInjectView(self):
        ...
    def setSpawnPoints(self, points, pointId=None):
        ...
    def showSpawnPoints(self):
        ...
    def closeSpawnPoints(self):
        ...
    def updatePoint(self, vehicleId, pointId, prevPointId):
        ...
    def updateCloseTime(self, timeLeft, state):
        ...
    def onSelectPoint(self, pointId):
        ...
    def setSpawnType(self, spawnType):
        ...
