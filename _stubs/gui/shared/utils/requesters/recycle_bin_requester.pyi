# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/recycle_bin_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from ItemRestore import RESTORE_VEHICLE_TYPE as RESTORE_VEHICLE_TYPE
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from helpers import time_utils as time_utils
from skeletons.gui.shared.utils.requesters import IRecycleBinRequester as IRecycleBinRequester
_VehicleRestoreInfo: Any

class VehicleRestoreInfo(_VehicleRestoreInfo):
    def getRestoreTimeLeft(self):
        ...
    def getRestoreCooldownTimeLeft(self):
        ...
    def isLimited(self):
        ...
    def isInCooldown(self):
        ...
    def isUnlimited(self):
        ...
    def isRestorePossible(self):
        ...
    def __getTimeGone(self):
        ...

class RecycleBinRequester(AbstractSyncDataRequester, IRecycleBinRequester):
    @property
    def recycleBin(self):
        ...
    @property
    def vehiclesBuffer(self):
        ...
    def getVehicleRestoreInfo(self, intCD, restoreDuration, restoreCooldown):
        ...
    def getVehiclesIntCDs(self):
        ...
    def getTankmen(self, maxDuration):
        ...
    def getTankman(self, invID, maxDuration):
        ...
    def _requestCache(self, callback=None):
        ...
