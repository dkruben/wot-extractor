# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/personal_reserves/personal_reserves_shared_model_utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from time import time as time
import typing as typing
from future.utils import iteritems as iteritems
from goodies.goodie_constants import GOODIE_RESOURCE_TYPE as GOODIE_RESOURCE_TYPE, GOODIE_STATE as GOODIE_STATE, BoosterCategory as BoosterCategory
from gui.goodies.goodie_items import Booster as Booster, getFullNameForBoosterIcon as getFullNameForBoosterIcon, BoosterUICommon as BoosterUICommon, BoostersType as BoostersType, getBoosterGuiType as getBoosterGuiType
from gui.impl.common.personal_reserves.personal_reserves_shared_constants import BOOST_CATEGORY_TO_RESERVE_TYPE_LOOKUP as BOOST_CATEGORY_TO_RESERVE_TYPE_LOOKUP, BOOSTER_STATE_TO_BOOSTER_MODEL_STATE as BOOSTER_STATE_TO_BOOSTER_MODEL_STATE, PREMIUM_BOOSTER_IDS as PREMIUM_BOOSTER_IDS, EVENT_BOOSTER_IDS as EVENT_BOOSTER_IDS, PERSONAL_RESOURCE_ORDER as PERSONAL_RESOURCE_ORDER
from gui.impl.gen.view_models.common.personal_reserves.booster_model import BoosterModel as BoosterModel, ReserveKind as ReserveKind
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import GroupCategory as GroupCategory, ReservesGroupModel as ReservesGroupModel
from gui.impl.lobby.personal_reserves.personal_reserves_utils import getGUIResourceOrder as getGUIResourceOrder, getNearestExpiryTimeAndAmountByGroup as getNearestExpiryTimeAndAmountByGroup, getTotalBoostersByResourceType as getTotalBoostersByResourceType, getNearestExpirationTimeAndCountForToday as getNearestExpirationTimeAndCountForToday, getTotalLimitedBoostersByResourceType as getTotalLimitedBoostersByResourceType
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers.time_utils import ONE_DAY as ONE_DAY, ONE_YEAR as ONE_YEAR, makeLocalServerTime as makeLocalServerTime
from typing import Dict as Dict, List as List, Iterable as Iterable, Optional as Optional, Union as Union
from skeletons.gui.game_control import IBoostersController as IBoostersController
from skeletons.gui.goodies import IBoostersStateProvider as IBoostersStateProvider, IGoodiesCache as IGoodiesCache
from frameworks.wulf import Array as Array
RESERVE_GROUP_CATEGORY_LOOKUP: dict
NO_FUTURE_GIVEN: Any

# base nao representavel no stub: namedtuple(...)
class BoosterModelData:
    def __new__(cls, resourceType, category, booster=None, depotCount=0, forcePremium=False, showHint=False):
        ...
    def validate(self, data):
        ...
    def replace(self, **kwargs):
        ...

def getPersonalBoosterModelDataByResourceType(cache, controller=None):
    ...
def addPersonalBoostersGroup(resourceType, boosterModelDataByType, groupArray):
    ...
def addEventGroup(groupArray, cache):
    ...
def addBoosterModel(boosterArray, resourceType, category, booster=None, depotCount=0, forcePremium=False, showHint=False):
    ...
def makeBonuses(booster):
    ...
def addToReserveArrayByCategory(reservesArray, boosters, category, cache, canAddEmpty=False):
    ...
def getReserveKind(boosterType):
    ...
def fillBoosterModelWithData(model, booster):
    ...
