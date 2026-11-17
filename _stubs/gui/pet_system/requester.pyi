# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/requester.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from gui.pet_system.constants import PS_PDATA_KEYS as PS_PDATA_KEYS
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester as AbstractSyncDataRequester
from pet_system_common.pet_constants import PETS_SYSTEM_PDATA_KEY as PETS_SYSTEM_PDATA_KEY, PetStateBehavior as PetStateBehavior
from skeletons.gui.shared.utils.requesters import IPetSystemRequester as IPetSystemRequester
from typing import List as List, Dict as Dict, Any as Any, Set as Set
PetID: _Any
EventID: _Any
NameID: _Any
BonusID: _Any
Synergy: _Any
SynergyLevel: _Any
_logger: _Any
INVALID_PET_ID = 0
INVALID_EVENT_ID = 0

class PetRequesterRequester(AbstractSyncDataRequester, IPetSystemRequester):
    dataKey = PETS_SYSTEM_PDATA_KEY
    def isPetUnlocked(self, petID):
        ...
    def getActivePetID(self):
        ...
    def getActiveEventID(self):
        ...
    def getUnlockedPetIDs(self):
        ...
    def getStateBehavior(self):
        ...
    def getSelectedName(self, petID):
        ...
    def getBonuses(self):
        ...
    def getActiveBonus(self):
        ...
    def getAppliedBonusCount(self):
        ...
    def getSynergyPoints(self, petID):
        ...
    def getSynergyLevel(self, petID):
        ...
    def getFirstClickedSynergyPets(self):
        ...
    def __getSynergyStorage(self, petID):
        ...
    def _requestCache(self, callback=None):
        ...
    def _preprocessValidData(self, data):
        ...
