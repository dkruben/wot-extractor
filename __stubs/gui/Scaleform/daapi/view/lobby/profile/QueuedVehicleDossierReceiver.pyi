# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/QueuedVehicleDossierReceiver.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
MIN_INTERVAL_BETWEEN_INVOKES = 300

class QueuedVehicleDossierReceiver(object):
    itemsCache: Any
    __isUnderRequesting: Any
    __queuedVehicleData: Any
    __lastInvokeTime: Any
    onDataReceived: Any
    def __init__(self):
        ...
    def invoke(self, databaseID, vehicleID):
        ...
    # decorador original: @adisp_process
    def __requestData(self, databaseID, vehicleID):
        ...
    def dispose(self):
        ...
