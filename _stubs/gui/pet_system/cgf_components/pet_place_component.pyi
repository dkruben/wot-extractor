# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/cgf_components/pet_place_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import WWISE as WWISE
import Math as Math
import CGF as CGF
from typing import List as List
from collections import namedtuple as namedtuple
from functools import partial as partial
from cgf_script.registration import ComponentProperty as ComponentProperty, registerComponent as registerComponent
from gui.pet_system.constants import PetPlaceName as PetPlaceName
from helpers import dependency as dependency
from pet_system_common import pet_constants as pet_constants
from pet_system_common.pet_constants import PetsConsts as PetsConsts, PET_RTPC_DOG_TYPE as PET_RTPC_DOG_TYPE
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from typing import Optional as Optional
_ActivePrefabInfo: Any
_LoadingPrefabInfo: Any

# decorador original: @registerComponent
class PetPlaceComponent(object):
    domain = CGF.Domain.Client
    editorTitle = 'Pet Place Component'
    group = 'Pets'
    names: dict
    placeName: Any

class PetPrefabSystem(CGF.System):
    petController: Any
    lobbyContext: Any
    _activePet = None
    _loadingPet = None
    PlacementActivated: Any
    PlaceIterate: Any
    Reactions: Any
    def onMappingLoaded(self):
        ...
    def onMappingUnloaded(self):
        ...
    def update(self):
        ...
    def _createPet(self, prefabPath, placeGO, petID):
        ...
    def _removePet(self):
        ...
    def _setRTPC(self, petID):
        ...
    def _onPrefabLoaded(self, loadingPet, petID, objects, queue):
        ...
    def updateActivePet(self, petID):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def onUpdatePetPlace(self, petPlaceName):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def getPetPrefabByID(petID, petContoller=None):
    ...
