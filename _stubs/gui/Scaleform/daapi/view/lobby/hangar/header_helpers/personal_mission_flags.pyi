# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/personal_mission_flags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import nations as nations
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.base_flags import IQuestsFlag as IQuestsFlag
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.flag_helpers import LabelState as LabelState, headerQuestFormatterVo as headerQuestFormatterVo, wrapQuestGroup as wrapQuestGroup
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS as HANGAR_HEADER_QUESTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.server_events.events_dispatcher import showPersonalMission as showPersonalMission, showPersonalMissionOperationsPage as showPersonalMissionOperationsPage, showPersonalMissionsOperationsMap as showPersonalMissionsOperationsMap
from gui.shared.formatters import icons as icons
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
QUEST_TYPE_BY_PM_BRANCH: dict
HANGAR_HEADER_QUESTS_TO_PM_BRANCH: dict
TOOLTIPS_HANGAR_HEADER_PM: dict
TOOLTIPS_HANGAR_HEADER_PM2: dict

class WIDGET_PM_STATE(object):
    DISABLED = 0
    BRANCH_DISABLED = 2
    OPERATION_DISABLED = 4
    MISSION_DISABLED = 8
    UNAVAILABLE = 16
    LOW_LEVEL = 32
    NO_VEHICLE = 64
    DONE = 128
    DONE_LOCKED_NEXT: Any
    DONE_LOW_NEXT: Any
    COMPLETED = 256
    COMPLETED_LOCKED_NEXT: Any
    COMPLETED_LOW_NEXT: Any
    AVAILABLE = 512
    IN_PROGRESS = 1024
    ON_PAUSE = 2048

class PersonalMissionsFlag(IQuestsFlag):
    __slots__: tuple
    __eventsCache: Any
    __lobbyContext: Any
    __limitedUIController: Any
    @classmethod
    def isFlagSuitable(cls, questType):
        ...
    @classmethod
    def formatQuests(cls, vehicle, params):
        ...
    @classmethod
    def showQuestsInfo(cls, questType, questID):
        ...
    @classmethod
    def __showAvailablePMOperation(cls, branch):
        ...

def _findPersonalMissionsState(eventsCache, vehicle, branch):
    ...
def _getPersonalMissionsIcon(vehicle, branch, active):
    ...
def _getPersonalMissionsTooltip(branch, key):
    ...
