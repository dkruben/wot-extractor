# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/platoon_config.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from enum import Enum as Enum
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE, QUEUE_TYPE as QUEUE_TYPE, BATTLE_MODE_VEHICLE_TAGS as BATTLE_MODE_VEHICLE_TAGS, BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC as BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC
from gui.impl.gen import R as R
from gui.impl.lobby.platoon.view.platoon_members_view import MembersWindow as MembersWindow
from gui.impl.lobby.platoon.view.platoon_members_view import SquadMembersView as SquadMembersView, EventMembersView as EventMembersView, EpicMembersView as EpicMembersView, BattleRoyaleMembersView as BattleRoyaleMembersView, MapboxMembersView as MapboxMembersView
from gui.impl.lobby.platoon.view.platoon_search_view import SearchWindow as SearchWindow, SearchView as SearchView
from gui.impl.lobby.platoon.view.platoon_selection_view import SelectionWindow as SelectionWindow
from gui.impl.lobby.platoon.view.platoon_welcome_view import WelcomeView as WelcomeView
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from soft_exception import SoftException as SoftException
_logger: Any
SquadInfo: Any
Position: Any
PlatoonLayout: Any
PrbEntityInfo: Any
DEFAULT_LAYOUTS_KEY = 'default'
ePlatoonLayouts: dict
PLATOON_VIEW_BY_PRB_TYPE: dict
QUEUE_TYPE_TO_PREBATTLE_ACTION_NAME: dict
PRB_TYPE_TO_WELCOME_VIEW_CONTENT_FACTORY: dict
PRB_TYPE_TO_SEARCH_VIEW_CONTENT_FACTORY: dict
RANDOM_VEHICLE_CRITERIA: Any
PREBATTLE_TYPE_TO_VEH_CRITERIA: dict

class EPlatoonLayout(Enum):
    WELCOME = 0
    SEARCH = 1
    MEMBER = 2

def buildCurrentLayouts(prbType=...):
    ...
def addPlatoonViewByPrbType(prbType, platoonView, personality):
    ...
def addPlatoonWelcomeViewByPrbType(prbType, welcomeView, personality):
    ...
def addPlatoonSearchViewByPrbType(prbType, searchView, personality):
    ...
def addQueueTypeToPrbSquadActionName(queueType, prbSquadActionName, personality):
    ...
def addPlatoonLayoutData(prbType, layoutsData, personality):
    ...
