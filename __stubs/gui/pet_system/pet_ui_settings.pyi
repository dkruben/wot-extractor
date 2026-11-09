# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/pet_ui_settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from copy import deepcopy as deepcopy
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import PetSystem as PetSystem
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared import events as events_constants
from gui.shared import g_eventBus as g_eventBus
from typing import Set as Set
PetID: Any
NameID: Any
SynergyLevel: Any

class PetUISettings(object):
    @classmethod
    def getSeenPetNameIDs(cls):
        ...
    @classmethod
    def setSeenPetNameIDs(cls, seenPetNames):
        ...
    @classmethod
    def getLastSeenSynergyLevel(cls, petID):
        ...
    @classmethod
    def setLastSeenSynergyLevel(cls, petID, level):
        ...
    @classmethod
    def getSeenInStoragePetIDs(cls):
        ...
    @classmethod
    def setSeenInStoragePetIDs(cls, seenPetIDs):
        ...
    @classmethod
    def getSeenPromoPetIDs(cls):
        ...
    @classmethod
    def addSeenPromoPetID(cls, seenPetID):
        ...
    @classmethod
    def _setSetting(cls, settingName, settingValue):
        ...
    @classmethod
    def _getSetting(cls, settingName):
        ...
