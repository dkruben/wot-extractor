# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/web_client_api/ui/barracks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from past.builtins import basestring as basestring
from gui.Scaleform.genConsts.BARRACKS_CONSTANTS import BARRACKS_CONSTANTS as BARRACKS_CONSTANTS
from gui.shared import event_dispatcher as shared_events
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from items import ITEM_TYPES as ITEM_TYPES, parseIntCompactDescr as parseIntCompactDescr
from items.vehicles import VEHICLE_CLASS_TAGS as VEHICLE_CLASS_TAGS
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.web_client_api import Field as Field, W2CSchema as W2CSchema, WebCommandException as WebCommandException, w2c as w2c
from web.web_client_api.common import TManLocation as TManLocation
_logger: Any
_ALL = 'all'
_LOCATION: dict
_VEHICLE_CLASSES: Any
_TANKMAN_ROLES: Any

class _BarracksTabSchema(W2CSchema):
    location: Any
    tank_type: Any
    role: Any

class BarracksWebApiMixin(object):
    __itemsCache: Any
    # decorador original: @w2c(...)
    def openBarracks(self, cmd):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _isValidTankmanLocation(_, data, itemsCache=None):
    ...
def _isValidTankType(_, data):
    ...
def _isValidTankmanRole(_, data):
    ...
def _isValidParam(data, paramName, checkList):
    ...
def _isOverParam(data, field):
    ...
def _makeCriteria(intCD):
    ...
