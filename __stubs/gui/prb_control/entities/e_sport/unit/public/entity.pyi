# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/e_sport/unit/public/entity.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import account_helpers as account_helpers
from UnitBase import UNIT_BROWSER_TYPE as UNIT_BROWSER_TYPE
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE
from gui.prb_control.entities.e_sport.unit.entity import ESportBrowserEntity as ESportBrowserEntity, ESportEntity as ESportEntity, ESportEntryPoint as ESportEntryPoint, ESportBrowserEntryPoint as ESportBrowserEntryPoint
from gui.prb_control.entities.e_sport.unit.public.actions_validator import ESportActionsValidator as ESportActionsValidator
from gui.prb_control.entities.e_sport.unit.public.requester import UnitsListRequester as UnitsListRequester
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.prb_control.items import SelectResult as SelectResult
from gui.prb_control.items.unit_items import DynamicRosterSettings as DynamicRosterSettings
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME

class PublicDynamicRosterSettings(DynamicRosterSettings):
    def _extractSettings(self, unit):
        ...

class PublicBrowserEntryPoint(ESportBrowserEntryPoint):
    def __init__(self):
        ...

class PublicEntryPoint(ESportEntryPoint):
    ...

class PublicBrowserEntity(ESportBrowserEntity):
    __listReq: Any
    def __init__(self):
        ...
    def init(self, ctx=None):
        ...
    def fini(self, ctx=None, woEvents=False):
        ...
    def getBrowser(self):
        ...
    def doSelectAction(self, action):
        ...

class PublicEntity(ESportEntity):
    _rosterSettings: Any
    def __init__(self):
        ...
    def getQueueType(self):
        ...
    def doSelectAction(self, action):
        ...
    def unit_onUnitPlayerRoleChanged(self, playerID, prevRoleFlags, nextRoleFlags):
        ...
    def _createRosterSettings(self):
        ...
    def _createActionsValidator(self):
        ...
