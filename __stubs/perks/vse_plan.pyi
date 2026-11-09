# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/perks/vse_plan.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import VSE as VSE
from constants import IS_CELLAPP as IS_CELLAPP
from items import perks as perks
from visual_script.misc import ASPECT as ASPECT
from functools import wraps as wraps
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG_DEV as LOG_DEBUG_DEV, LOG_WARNING as LOG_WARNING
from typing import TYPE_CHECKING as TYPE_CHECKING
from visual_script.contexts.perks_context import PerkContext as PerkContext

class PlanStatus:
    DEFAULT = 0
    LOAD = 1
    START = 2

class VsePlan(object):
    _PLAN_PATH = 'vscript/plans/{}.xml'
    _PLAN_ID_PREFIX = 'abilityPerks/perk_'
    _owner: Any
    _ownerId: Any
    scopeId: Any
    perkId: Any
    _level: Any
    _planId: Any
    _isPlanLoaded: Any
    _isAutoStart: Any
    _plan: Any
    _context: Any
    _contextCreator: Any
    _usedEvents: Any
    __callback: Any
    _contextArgs: Any
    _isPlanStarted: Any
    _status: Any
    def __init__(self, owner, scopeId, level, perkId, onReadyCallback, contextArgs):
        ...
    @property
    def hasContext(self):
        ...
    @property
    def usedEvents(self):
        ...
    @property
    def isPlanLoaded(self):
        ...
    @property
    def isPlanStarted(self):
        ...
    @property
    def status(self):
        ...
    def load(self, contextCreator, isAutoStart=False):
        ...
    # decorador original: @callOnValidState
    def setInputParam(self, paramName, paramValue):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    # decorador original: @callOnValidState
    def triggerVSPlanEvent(self, event):
        ...
    def destroy(self):
        ...
    def setContextArgs(self, contextArgs):
        ...
    def _onPlanPreLoaded(self, future=None):
        ...
    def _clearCallBack(self):
        ...
    def __setStatus(self, value):
        ...

def callOnValidState(f):
    ...
