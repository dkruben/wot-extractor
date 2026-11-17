# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/personal_missions_operations.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import operator as operator
from future.utils import viewitems as viewitems
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.missions import missions_helper as missions_helper
from gui.Scaleform.daapi.view.meta.PersonalMissionOperationsMeta import PersonalMissionOperationsMeta as PersonalMissionOperationsMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES as PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.personal_missions_navigation import PersonalMissionsNavigation as PersonalMissionsNavigation
from gui.server_events.pm_constants import PERSONAL_MISSIONS_SOUND_SPACE as PERSONAL_MISSIONS_SOUND_SPACE, SOUNDS as SOUNDS
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showHangar as showHangar
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES

class PersonalMissionOperations(LobbySubView, PersonalMissionOperationsMeta, PersonalMissionsNavigation):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SOUND_SPACE
    __backAlias: Any
    def __init__(self, ctx):
        ...
    def showInfo(self):
        ...
    def onOperationClick(self, pmType, operationID):
        ...
    def closeView(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __update(self):
        ...
    def __onQuestsUpdated(self, *args):
        ...
    def __setTitle(self):
        ...
    def __formatImageState(self, state):
        ...
    def _onSettingsChanged(self, diff):
        ...
