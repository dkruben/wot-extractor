# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/requesters/vehicle_rotation_requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IVehicleRotationRequester as IVehicleRotationRequester

class VehicleRotationRequester(AbstractSyncDataRequester, IVehicleRotationRequester):
    def getBattlesCount(self, groupNum):
        ...
    def isGroupLocked(self, groupNum):
        ...
    def getGroupNum(self, vehIntCD):
        ...
    def isInfinite(self, groupNum):
        ...
    def unlockedBy(self, groupNum):
        ...
    @property
    def _groupLocks(self):
        ...
    def _requestCache(self, callback=None):
        ...
