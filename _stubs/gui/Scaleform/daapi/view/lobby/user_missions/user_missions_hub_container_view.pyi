# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/user_missions/user_missions_hub_container_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import MISSIONS_PAGE as MISSIONS_PAGE
from account_helpers import AccountSettings as AccountSettings
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.lobby.user_missions import missions_group_packers as missions_group_packers
from gui.Scaleform.daapi.view.meta.UserMissionsHubContainerViewMeta import UserMissionsHubContainerViewMeta as UserMissionsHubContainerViewMeta
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.Scaleform.genConsts.USERMISSSIONS_ALIASES import USERMISSSIONS_ALIASES as USERMISSSIONS_ALIASES
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.tab_id import TabId as TabId
from gui.server_events.events_dispatcher import showMissionDetails as showMissionDetails, hideMissionDetails as hideMissionDetails
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import UserMissionsEvent as UserMissionsEvent, MissionsEvent as MissionsEvent
from gui.shared.formatters import text_styles as text_styles

class UserMissionsHubContainerView(UserMissionsHubContainerViewMeta):
    __tabID: Any
    __questId: Any
    __commonTabView: Any
    __eventID: Any
    __groupID: Any
    __showMissionDetails: Any
    __challengeID: Any
    __isFirstUpdate: Any
    __builder: Any
    __filterData: Any
    def __init__(self, ctx):
        ...
    def registerFlashComponent(self, component, alias, *args):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def resetFilters(self):
        ...
    def onClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __filterApplied(self):
        ...
    def __updateFilterLabel(self):
        ...
    def __onFilterChanged(self, event):
        ...
    def __onFilterClosed(self, _):
        ...
    def __onShowTab(self, resetFilters=False):
        ...
    def __showMission(self):
        ...
    def __onChangeTab(self, event):
        ...
    def __onChangeContentLayout(self, event):
        ...
    def __onTransitionToMission(self, event):
        ...
