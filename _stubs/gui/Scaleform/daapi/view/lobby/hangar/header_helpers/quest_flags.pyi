# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/quest_flags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewvalues as viewvalues
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.base_flags import IQuestsFlag as IQuestsFlag
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.flag_helpers import getActiveQuestLabel as getActiveQuestLabel, headerQuestFormatterVo as headerQuestFormatterVo, wrapQuestGroup as wrapQuestGroup, LabelState as LabelState
from gui.Scaleform.daapi.view.lobby.missions.regular.missions_page import setHideDoneFilter as setHideDoneFilter
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS as HANGAR_HEADER_QUESTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.server_events.events_constants import RANKED_DAILY_GROUP_ID as RANKED_DAILY_GROUP_ID
from gui.server_events.events_dispatcher import showMissionsElen as showMissionsElen, showMissionsMarathon as showMissionsMarathon, showMissionsCategories as showMissionsCategories, showMissionsMapboxProgression as showMissionsMapboxProgression
from gui.shared.formatters import icons as icons
from gui.shared.personality import ServicesLocator as ServicesLocator
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController, IMapboxController as IMapboxController, IMarathonEventsController as IMarathonEventsController, IQuestsController as IQuestsController, IRankedBattlesController as IRankedBattlesController
_logger: Any

class BaseQuestFlag(IQuestsFlag):
    __slots__: tuple
    _QUEST_TYPE = None
    @classmethod
    def isFlagSuitable(cls, questType):
        ...

class BattleQuestsFlag(BaseQuestFlag):
    __slots__: tuple
    _QUEST_TYPE = HANGAR_HEADER_QUESTS.QUEST_TYPE_COMMON
    _limitedUIController: Any
    _questController: Any
    @classmethod
    def formatQuests(cls, vehicle, params):
        ...
    @classmethod
    def showQuestsInfo(cls, questType, questID):
        ...
    @classmethod
    def _getLabelAndFlagType(cls, totalCount, completedQuests):
        ...
    @classmethod
    def _getQuests(cls, vehicle):
        ...

class MapboxQuestsFlag(BaseQuestFlag):
    __slots__: tuple
    _QUEST_TYPE = HANGAR_HEADER_QUESTS.QUEST_TYPE_MAPBOX
    __mapboxController: Any
    @classmethod
    def formatQuests(cls, vehicle, params):
        ...
    @classmethod
    def showQuestsInfo(cls, _, __):
        ...

class RankedQuestsFlag(BaseQuestFlag):
    __slots__: tuple
    _QUEST_TYPE = HANGAR_HEADER_QUESTS.QUEST_GROUP_RANKED_DAILY
    __rankedController: Any
    @classmethod
    def formatQuests(cls, vehicle, params):
        ...
    @classmethod
    def showQuestsInfo(cls, _, __):
        ...

class ElenQuestsFlag(BaseQuestFlag):
    __slots__: tuple
    _QUEST_TYPE = HANGAR_HEADER_QUESTS.QUEST_TYPE_EVENT
    __eventsController: Any
    __connectionMgr: Any
    @classmethod
    def formatQuests(cls, vehicle, params):
        ...
    @classmethod
    def showQuestsInfo(cls, questType, questID):
        ...

class MarathonQuestsFlag(BaseQuestFlag):
    __slots__: tuple
    _QUEST_TYPE = HANGAR_HEADER_QUESTS.QUEST_TYPE_MARATHON
    __marathonsCtrl: Any
    @classmethod
    def isFlagSuitable(cls, questType):
        ...
    @classmethod
    def formatQuests(cls, vehicle, params):
        ...
    @classmethod
    def showQuestsInfo(cls, questType, questID):
        ...
