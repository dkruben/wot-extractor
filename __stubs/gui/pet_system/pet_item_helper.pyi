# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/pet_system/pet_item_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.promotion_model import PromoBonus as PromoBonus
from gui.pet_system.bonus_helper import BonusItem as BonusItem, BonusNameToPromoStr as BonusNameToPromoStr
from gui.pet_system.constants import PET_NAME_FORMAT as PET_NAME_FORMAT
from shared_utils import first as first
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from helpers import dependency as dependency
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
from typing import Optional as Optional
from gui.pet_system.requester import PetID as PetID

class PetItem(object):
    petController: Any
    lobbyContext: Any
    @classmethod
    def getActivePetID(cls):
        ...
    @classmethod
    def getPetsConfig(cls):
        ...
    @classmethod
    def getDefaultNameId(cls, petId=None):
        ...
    @classmethod
    def getCurrentNameId(cls, petId=None):
        ...
    @classmethod
    def getIsDefaultNameLocked(cls, petId):
        ...
    @classmethod
    def getPetType(cls, petId=None):
        ...
    @classmethod
    def getPetBreed(cls, petId=None):
        ...
    @classmethod
    def getPetName(cls, nameID):
        ...

class PromoPetItem(PetItem):
    @classmethod
    def getPetsPromoConfig(cls):
        ...
    @classmethod
    def getCurrentNameId(cls, petId=None):
        ...
    @classmethod
    def getPromoUrl(cls, petId):
        ...
    @classmethod
    def getPromoShopUrl(cls, petId):
        ...
    @classmethod
    def getPetBenefits(cls, petID):
        ...
