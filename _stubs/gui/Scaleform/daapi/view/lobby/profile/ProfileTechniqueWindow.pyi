# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTechniqueWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.profile.QueuedVehicleDossierReceiver import QueuedVehicleDossierReceiver as QueuedVehicleDossierReceiver
from gui.Scaleform.daapi.view.lobby.profile.ProfileTechnique import ProfileTechnique as ProfileTechnique

class ProfileTechniqueWindow(ProfileTechnique):
    __dataReceiver: Any
    __currentlyRequestingVehicleId: Any
    def __init__(self, *args):
        ...
    def requestData(self, vehicleId):
        ...
    def invokeUpdate(self):
        ...
    def _dispose(self):
        ...
    def _setRatingButton(self):
        ...
    def __requestedDataReceived(self, databaseID, vehicleID):
        ...
