# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_map_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import operator as operator
from future.utils import viewvalues as viewvalues
import WWISE as WWISE
import SoundGroups as SoundGroups
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getPersonalMissionAwardsFormatter as getPersonalMissionAwardsFormatter, getMapRegionTooltipData as getMapRegionTooltipData
from gui.Scaleform.daapi.view.meta.PersonalMissionsMapViewMeta import PersonalMissionsMapViewMeta as PersonalMissionsMapViewMeta
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.awards_formatters import COMPLETION_TOKENS_SIZES as COMPLETION_TOKENS_SIZES
from gui.server_events.events_dispatcher import showPersonalMissionDetails as showPersonalMissionDetails
from gui.server_events.events_helpers import AwardSheetPresenter as AwardSheetPresenter
from gui.server_events.personal_missions_navigation import PersonalMissionsNavigation as PersonalMissionsNavigation
from gui.server_events.pm_constants import SOUNDS as SOUNDS
from helpers.i18n import makeString as _ms
from personal_missions import PM_BRANCH as PM_BRANCH
from shared_utils import findFirst as findFirst, first as first
_MAIN_AWARD_TEXT: dict
HT_CHAIN_ID = 2
OPERATION_ID_T55A = 3
OPERATION_ID_OBJECT_260 = 4
MAIN_AWARD_TEXT_ID_HULL = 6
_MAIN_AWARD_TEXT_PM2: dict
ALLIANCE_CHAIN_ID = 3
OPERATION_ID_CHIMERA = 6
OPERATION_ID_OBJECT_279 = 7
MAIN_AWARD_TEXT_PM2_ID_HULL = 5

class PersonalMissionsMapView(PersonalMissionsMapViewMeta, PersonalMissionsNavigation):
    def onRegionClick(self, questID):
        ...
    def refresh(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getQuestsData(self, chainID, quests):
        ...
    def __getQuestStatusData(self, chainID, quest):
        ...
    def __getFinalQuestAwardsVO(self, quest):
        ...
