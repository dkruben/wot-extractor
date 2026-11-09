# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_first_entry_award_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from operator import attrgetter as attrgetter
from future.utils import viewvalues as viewvalues
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.meta.PersonalMissionFirstEntryAwardViewMeta import PersonalMissionFirstEntryAwardViewMeta as PersonalMissionFirstEntryAwardViewMeta
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.settings import BADGES_ICONS as BADGES_ICONS, getBadgeIconPath as getBadgeIconPath
from gui.server_events.finders import getQuestsByTokenAndBonus as getQuestsByTokenAndBonus, pmTokenDetector as pmTokenDetector, badgeBonusFinder as badgeBonusFinder
from gui.server_events.personal_missions_navigation import PersonalMissionsNavigation as PersonalMissionsNavigation
from gui.server_events.pm_constants import SOUNDS as SOUNDS, PERSONAL_MISSIONS_SOUND_SPACE as PERSONAL_MISSIONS_SOUND_SPACE, PM_TUTOR_FIELDS as PM_TUTOR_FIELDS
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.shared.event_dispatcher import showPersonalMissionCampaignSelectorWindow as showPersonalMissionCampaignSelectorWindow
from helpers import dependency as dependency
from helpers.i18n import makeString as makeString
from shared_utils import first as first
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class PersonalMissionFirstEntryAwardView(LobbySubView, PersonalMissionsNavigation, PersonalMissionFirstEntryAwardViewMeta):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SOUND_SPACE
    __BADGE_ICON_SIZES: Any
    def bigBtnClicked(self):
        ...
    def onEscapePress(self):
        ...
    def closeView(self):
        ...
    def _populate(self):
        ...
    def __getAwards(self, operations):
        ...

def _wrapBadgeAward(title, badgeID, imageSize):
    ...
