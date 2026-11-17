# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/shop/crew.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewvalues as viewvalues
import nations as nations
from gui import GUI_NATIONS as GUI_NATIONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME, VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria
from gui.shared.utils.requesters.ItemsRequester import PredicateCondition as PredicateCondition
from items.tankmen import TankmanDescr as TankmanDescr, generateCompactDescr as generateCompactDescr, getNationConfig as getNationConfig
from shared_utils import first as first
from web.web_client_api.common import TManGender as TManGender, TManLocation as TManLocation
from typing import Generator as Generator, Set as Set, Tuple as Tuple, Union as Union
from gui.server_events.recruit_helper import _BaseRecruitInfo as _BaseRecruitInfo
from items.components.tankmen_components import NationConfig as NationConfig, NationGroup as NationGroup
TManPassport: Any
_NEW_SKILL = 'new_skill'
_NEWBIE = 'newbie'
_UNDEFINED = 'undefined'
_EMPTY_STR = ''
_INVALID_VALUE = -1

class ShopCrewCriteria(object):
    PREMIUM: Any

class _ShopTankman(object):
    __tankman: Any
    def __init__(self, tankman):
        ...
    def __getattr__(self, name):
        ...
    @property
    def isPremium(self):
        ...
    @property
    def location(self):
        ...
    @property
    def roleID(self):
        ...
    @property
    def roleName(self):
        ...
    @property
    def role(self):
        ...
    @property
    def gender(self):
        ...
    @property
    def groupName(self):
        ...
    @property
    def nationName(self):
        ...
    @property
    def nationUserName(self):
        ...
    @property
    def rankID(self):
        ...
    @staticmethod
    def _getNationGroup(nationID, isPremium, groupID):
        ...

class _ShopRecruit(_ShopTankman):
    __R_CREW = R.strings.quests.bonuses.item
    @property
    def location(self):
        ...
    @property
    def roleID(self):
        ...
    @property
    def roleName(self):
        ...
    @property
    def roleUserName(self):
        ...
    @property
    def groupName(self):
        ...
    @property
    def nationID(self):
        ...
    @property
    def nationName(self):
        ...
    @property
    def nationUserName(self):
        ...
    @property
    def rankID(self):
        ...
    @property
    def rankUserName(self):
        ...
    @property
    def vehicleNativeDescr(self):
        ...
    @property
    def iconRank(self):
        ...
    @property
    def iconRole(self):
        ...
    @property
    def role(self):
        ...
    def __getNewbieStr(self):
        ...

def makeTankman(crewItem):
    ...
def _recruit(recruitInfo):
    ...
def _iterNationGroups(config, isPremium, groupName):
    ...
def _iterNationsConfigs():
    ...
def _makePassport(recruitInfo, nationGroup):
    ...
