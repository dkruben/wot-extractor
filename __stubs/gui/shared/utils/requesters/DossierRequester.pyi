# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/DossierRequester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from functools import partial as partial
from future.utils import iteritems as iteritems, viewitems as viewitems
import BigWorld as BigWorld
import constants as constants
import dossiers2 as dossiers2
import AccountCommands as AccountCommands
from adisp import adisp_async as adisp_async
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared.utils import code2str as code2str
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from gui.shared.utils.requesters.common import RequestProcessor as RequestProcessor
from skeletons.gui.shared.utils.requesters import IDossierRequester as IDossierRequester

class UserDossier(object):
    __queue: list
    __lastResponseTime = 0
    __request = None
    __cache: Any
    def __init__(self, databaseID):
        ...
    def __setLastResponseTime(self):
        ...
    def __nextRequestTime(self):
        ...
    def __processQueue(self):
        ...
    def __requestPlayerInfo(self, callback):
        ...
    def __requestAccountDossier(self, callback):
        ...
    def __requestVehicleDossier(self, vehCompDescr, callback):
        ...
    def __requestClanInfo(self, callback):
        ...
    def __processValueResponse(self, callback, code, value):
        ...
    # decorador original: @adisp_async
    def getAccountDossier(self, callback):
        ...
    # decorador original: @adisp_async
    def getClanInfo(self, callback):
        ...
    # decorador original: @adisp_async
    def getRated7x7Seasons(self, callback):
        ...
    # decorador original: @adisp_async
    def getRankedInfo(self, callback):
        ...
    # decorador original: @adisp_async
    def getGlobalRating(self, callback):
        ...
    # decorador original: @adisp_async
    def getVehicleDossier(self, vehCompDescr, callback):
        ...
    # decorador original: @adisp_async
    def getDogTag(self, callback):
        ...
    # decorador original: @adisp_async
    def getServiceRecordCustomization(self, callback):
        ...
    # decorador original: @adisp_async
    def getBattleRoyaleStats(self, callback):
        ...
    # decorador original: @adisp_async
    def getWTR(self, callback):
        ...
    # decorador original: @adisp_async
    def getLayout(self, callback):
        ...
    # decorador original: @adisp_async
    def getLayoutState(self, callback):
        ...
    @property
    def isHidden(self):
        ...
    @property
    def isAvailable(self):
        ...
    @property
    def isValid(self):
        ...

class DossierRequester(AbstractSyncDataRequester, IDossierRequester):
    __users: Any
    def __init__(self):
        ...
    def _requestCache(self, callback=None):
        ...
    def getVehicleDossier(self, vehTypeCompDescr):
        ...
    def getVehDossiersIterator(self):
        ...
    def getUserDossierRequester(self, databaseID):
        ...
    def closeUserDossier(self, databaseID):
        ...
    def onCenterIsLongDisconnected(self, isLongDisconnected):
        ...
