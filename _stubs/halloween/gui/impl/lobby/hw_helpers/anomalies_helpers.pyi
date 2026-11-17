# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/hw_helpers/anomalies_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from halloween.gui import halloween_account_settings as hw_acc_settings
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from halloween_common.halloween_constants import AnomalySettings as AnomalySettings, ANOMALIES_SYSTEM_UNLOCKED as ANOMALIES_SYSTEM_UNLOCKED, AnomalyType as AnomalyType
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Set as Set

# decorador original: @dependency.replace_none_kwargs(...)
def isAnomaliesSystemAvailable(itemsCache=None):
    ...
def getShowedAnomaliesIDs():
    ...
def setAnomalyAsShowed(anomalyID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getKnownAnomaliesIDs(itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAnomaliesProgression(hwAnomaliesCtrl=None):
    ...
def getNewAnomaliesIDs():
    ...
def hasNewAnomalies():
    ...
def _getAnomalyIDByToken(anomalyToken):
    ...
def _getAnomalyTokenByID(anomalyID):
    ...
def getShowedAnomaliesTokens():
    ...
