# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_quest_award_screen.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import personal_missions as pm
from adisp import adisp_async as adisp_async
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui import SystemMessages as SystemMessages
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getDetailedMissionData as getDetailedMissionData, getHtmlAwardSheetIcon as getHtmlAwardSheetIcon
from gui.Scaleform.daapi.view.meta.PersonalMissionsQuestAwardScreenMeta import PersonalMissionsQuestAwardScreenMeta as PersonalMissionsQuestAwardScreenMeta
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as _PM
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.events_dispatcher import showTankwomanAward as showTankwomanAward
from gui.server_events.events_helpers import MISSIONS_STATES as MISSIONS_STATES
from gui.server_events.pm_constants import SOUNDS as SOUNDS
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import PersonalMissionsEvent as PersonalMissionsEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getTypeShortUserName as getTypeShortUserName
from gui.shared.gui_items.processors import quests as quests_proc
from gui.shared.utils import toUpper as toUpper
from gui.shared.utils.decorators import adisp_process as adisp_process
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
_OPERATION_ID_TO_UI_BACKGROUND: dict

class PersonalMissionsQuestAwardScreen(PersonalMissionsQuestAwardScreenMeta):
    _eventsCache: Any
    _quest: Any
    _ctx: Any
    _proxyEvent: Any
    _awardListReturned: Any
    _operation: Any
    _mainReward: Any
    _addReward: Any
    _isAwardListUsed: Any
    _nextQuest: Any
    def __init__(self, ctx):
        ...
    def closeView(self):
        ...
    def onContinueBtnClick(self):
        ...
    def onNextQuestLinkClick(self):
        ...
    def onOkBtnClick(self):
        ...
    def onRecruitBtnClick(self):
        ...
    def onNextQuestBtnClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __fireNextQuestSelected(self):
        ...
    def __fireOnClose(self):
        ...
    # decorador original: @adisp_process(...)
    def _processMission(self, quest):
        ...
    def __setData(self):
        ...
    def __packNextQuestTitleSection(self, isFinal):
        ...
    def __packButtonsSection(self, isFinal):
        ...
    def __packQuestConditions(self, detailedData):
        ...
    def __packAwards(self, detailedData):
        ...
    # decorador original: @adisp_process(...)
    def __tryGetAward(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process(...)
    def __getPersonalMissionAward(self, callback):
        ...

def _getNextMissionInOperationByID(questID):
    ...
