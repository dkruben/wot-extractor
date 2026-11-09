# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/goodie_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from copy import deepcopy as deepcopy
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING, Type as Type
from goodies.GoodieConditions import MaxVehicleLevel as MaxVehicleLevel
from goodies.GoodieDefinition import GoodieDefinition as GoodieDefinition
from goodies.GoodieResources import Gold as Gold, Credits as Credits, Experience as Experience, CrewExperience as CrewExperience, FreeExperience as FreeExperience, FrontlineExperience as FrontlineExperience
from goodies.GoodieTargets import BuyPremiumAccount as BuyPremiumAccount, BuySlot as BuySlot, PostBattle as PostBattle, BuyGoldTankmen as BuyGoldTankmen, BuyVehicle as BuyVehicle, EpicMeta as EpicMeta, DemountOptionalDevice as DemountOptionalDevice, EpicPostBattle as EpicPostBattle, DropSkill as DropSkill, XpTransfer as XpTransfer, BuyPet as BuyPet
from goodies.goodie_multiple_resources import FreeXpCrewXpMultiResourceList as FreeXpCrewXpMultiResourceList, FreeXpMainXpMultiResourceList as FreeXpMainXpMultiResourceList
from goodies.Goodies import GoodieException as GoodieException
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from goodies.goodie_constants import GOODIE_TARGET_TYPE as GOODIE_TARGET_TYPE, GOODIE_CONDITION_TYPE as GOODIE_CONDITION_TYPE, GOODIE_RESOURCE_TYPE as GOODIE_RESOURCE_TYPE
from typing import Tuple as Tuple, Dict as Dict
from goodies.Goodies import Goodies as Goodies
from goodies.GoodieResources import GoodieResourceType as GoodieResourceType
GoodieData: Any
GoodieExpirationData: Any
_CONDITIONS: dict
_TARGETS: dict
RESOURCES: dict
RESOURCE_TO_GOODIE_LOOKUP: dict
GOODIE_CONDITION_TO_TEXT: dict
GOODIE_RESOURCE_TO_TEXT: dict
GOODIE_TARGET_TO_TEXT: dict
GOODIE_TEXT_TO_CONDITION: dict
GOODIE_TEXT_TO_RESOURCE: dict
GOODIE_TEXT_TO_TARGET: dict
CURRENCY_TO_RESOURCE_TYPE: dict
CURRENCY_TO_RESOURCE: dict

def loadDefinitions(d):
    ...
def getPriceWithDiscount(price, resourceData):
    ...
def getPremiumCost(premiumCosts, goodie):
    ...
def loadPdata(pdataGoodies, goodies, logID):
    ...
def calcDefaultPrice(default, actual):
    ...
def wipe(goodies, pdata, leaveGold):
    ...
