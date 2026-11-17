# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/store/actions_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from operator import methodcaller as methodcaller
from gui.Scaleform.daapi.view.lobby.store.action_composer import ActionComposer as ActionComposer
from gui.Scaleform.daapi.view.lobby.store.actions_helpers import getActionInfoData as getActionInfoData, getAnnouncedActionInfo as getAnnouncedActionInfo
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.server_events.settings import visitEventGUI as visitEventGUI
from helpers import i18n as i18n
from shared_utils import findFirst as findFirst
_INTERSECTED_ACTIONS_LIST: set
_pl = _ACTIONS_PRIORITY_LEVEL
_ACTIONS_PRIORITY_MAPPING: dict
_ltf = _LAYOUT_TEMPLATE_FIELDS
_FORMATING_FIELDS: tuple

class ACTIONS_SIZE(object):
    HERO = 'hero'
    NORMAL = 'normal'
    SMALL = 'small'
    COMING_SOON = 'coming_soon'

class _ACTIONS_PRIORITY_LEVEL(object):
    PRIORITY_1 = 1
    PRIORITY_2 = 2
    PRIORITY_3 = 3
    PRIORITY_4 = 4
    ALL_VISIBLE: tuple

class _VISIBLE_CARDS(object):
    ACTIONS = 'actions'
    ANNOUNCED = 'announced'

class _LAYOUT_TEMPLATE_FIELDS(object):
    TITLE = 'title'
    CARDS = 'cards'
    HEROCARD = 'heroCard'
    COLUMNLEFT = 'columnLeft'
    COLUMNRIGHT = 'columnRight'
    COMINGSOON = 'comingSoon'
    EMPTY = 'empty'
    INFO = 'info'
    BTNLABEL = 'btnLabel'

class ActionCardFormatter(object):
    __slots__: tuple
    discount: Any
    def __init__(self):
        ...
    def format(self, discount):
        ...
    def _packGui(self):
        ...
    def _getHeaderData(self):
        ...
    def _getTableData(self):
        ...
    def _getExtras(self):
        ...
    def _getDescription(self):
        ...

class HeroCardFormatter(ActionCardFormatter):
    def _getExtras(self, *args, **kwargs):
        ...
    def _getDescription(self):
        ...
    def _packGui(self):
        ...

class NormalCardFormatter(ActionCardFormatter):
    def _getHeaderData(self):
        ...
    def _getExtras(self, *args, **kwargs):
        ...

class SmallCardFormatter(ActionCardFormatter):
    def _getHeaderData(self):
        ...
    def _getExtras(self, *args, **kwargs):
        ...

class ComingSoonCardFormatter(ActionCardFormatter):
    def _getHeaderData(self):
        ...
    def _getExtras(self, *args, **kwargs):
        ...

class ActionsBuilder(object):
    __formatters: Any
    __visibleCards: Any
    def __init__(self):
        ...
    @classmethod
    def getAllVisibleDiscounts(cls, actions, entities, announced, sorting=False):
        ...
    def createLayoutTemplate(self, allCards):
        ...
    def getSuitableFormatter(self, discount):
        ...
    def format(self, actions, entities, announced):
        ...
    def markVisited(self, actionID):
        ...
    def __setVisualPriority(self, items, priority):
        ...

def getAllActionsInfoIterator(actions, entities):
    ...
def _dumpLayoutSkeleton():
    ...
def getActiveActions(eventsCache):
    ...
def getNewActiveActions(eventsCache):
    ...
def _getNewActiveActionsCounter(eventsCache):
    ...
