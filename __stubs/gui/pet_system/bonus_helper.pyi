# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/bonus_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from gui.impl.gen.view_models.views.lobby.pet_system.pet_bonus_model import PetBonusModel as PetBonusModel
from gui.impl.gen.view_models.views.lobby.pet_system.promotion_model import PromoBonus as PromoBonus
from helpers import dependency as dependency
from pet_system_common.pet_constants import PET_SYSTEM_RESOURCE_TO_TEXT as PET_SYSTEM_RESOURCE_TO_TEXT
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from typing import Set as Set, Iterable as Iterable
from frameworks.wulf import Array as Array
from gui.pet_system.requester import BonusID as BonusID
from pet_system_common import BonusConfig as BonusConfig
BonusResource: Any
BonusNameToPromoStr: dict

class BonusItem(object):
    petController: Any
    @classmethod
    def getActiveBonus(cls):
        ...
    @classmethod
    def getAppliedBonusCount(cls):
        ...
    @classmethod
    def getBonusesPerDay(cls):
        ...
    @classmethod
    def getPetBonusConfig(cls):
        ...
    @classmethod
    def getPetBonuses(cls, petID):
        ...
    @classmethod
    def getBonusResource(cls, bonusID):
        ...
    @classmethod
    def getBonusName(cls, bonusID):
        ...
    @classmethod
    def getBonusValue(cls, bonusID):
        ...
    @classmethod
    def getAvailableBonuses(cls):
        ...
    @classmethod
    def packBonusModelData(cls, bonusIDs, bonusModelsArray):
        ...
