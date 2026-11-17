# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/maps_training.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import AccountCommands as AccountCommands
from Event import Event as Event
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from maps_training_common.helpers import extractScenarioProgress as extractScenarioProgress
from maps_training_common.maps_training_constants import DEFAULT_PROGRESS_VALUE as DEFAULT_PROGRESS_VALUE, MT_PDATA_KEY as MT_PDATA_KEY, VEHICLE_TYPE as VEHICLE_TYPE, MAX_SCENARIO_PROGRESS as MAX_SCENARIO_PROGRESS

class MapsTraining(object):
    __syncData: Any
    __account: Any
    __cache: Any
    onMapsTrainingDataChanged: Any
    __ignore: Any
    def __init__(self, syncData):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def getCache(self, callback=None):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...
    def __getResult(self, progress, vehType, team):
        ...
    def getGeometryData(self, geometryID):
        ...
