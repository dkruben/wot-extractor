# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/VehiclesSpawnListStorage.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.moves import pickle as pickle
from Event import Event as Event
from VehiclesSpawnListStorageCommon import convertTuplesToVehicleSpawnData as convertTuplesToVehicleSpawnData
_logger: Any

class VehiclesSpawnListStorage(object):
    onSpawnListUpdated: Any
    def __init__(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomePlayer(self):
        ...
    def onBecomeNonPlayer(self):
        ...
    def updateSpawnList(self, spawnListData):
        ...
