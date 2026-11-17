# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/pbh_prefab_loader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import CGF as CGF
import Math as Math
from enum import Enum as Enum
from gui.battle_control.controllers.prebattle_highlights.pbh_helpers import getPbhAnchorData as getPbhAnchorData, getPbhPetAnchorGo as getPbhPetAnchorGo, getPbhSpacePrefab as getPbhSpacePrefab
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers import dependency as dependency
from pet_system_common.pet_constants import PetsConsts as PetsConsts
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class PrefabLoaderStatus(Enum):
    INITIAL = 'initial'
    LOADING = 'loading'
    LOADED = 'loaded'
    FAILED = 'failed'

class PBHPrefabLoader(object):
    __petController: Any
    __sessionProvider: Any
    __winnersGetter: Any
    __sizeGetter: Any
    __callback: Any
    __prefabStatus: Any
    __loadedGo: Any
    __callbackDelayer: Any
    def __init__(self, winnersGetter, sizeGetter):
        ...
    @property
    def status(self):
        ...
    def loadPBHPrefab(self, callback):
        ...
    def reset(self):
        ...
    def clear(self):
        ...
    def __loadPets(self):
        ...
    def __onPrefabLoaded(self, objects, queue):
        ...
    def __getPetBattlePrefabByID(self, petID):
        ...
    def __togglePBHSpacePrefab(self, activate):
        ...
