# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/hub_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import OrderedDict as OrderedDict
from account_helpers.AccountSettings import Winback as Winback
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.hub.hub_view_model import HubViewModel as HubViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tab_model import TabModel as TabModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.tab_id import TabId as TabId
from gui.impl.lobby.user_missions.hub.tabs.basic.basic_missions_tab import BasicMissionsTab as BasicMissionsTab
from gui.impl.lobby.user_missions.hub.tabs.challenges.challenge_missions_tab import ChallengeMissionsTab as ChallengeMissionsTab
from gui.impl.lobby.user_missions.hub.update_children_mixin import UpdateChildrenMixin as UpdateChildrenMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared import g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showWinbackIntroView as showWinbackIntroView
from gui.shared.events import UserMissionsEvent as UserMissionsEvent
from gui.shared.system_factory import collectDynamicUmgIntroPresenters as collectDynamicUmgIntroPresenters
from gui.winback.winback_helpers import getWinbackSetting as getWinbackSetting, setWinbackSetting as setWinbackSetting
from helpers import dependency as dependency
from skeletons.gui.game_control import IWinbackController as IWinbackController
from typing import Optional as Optional
TABS: Any

class DailyTabs(object):
    QUESTS = 0
    PREMIUM_MISSIONS = 1

# base nao representavel no stub: ViewComponent[...]
class HubView:
    __winbackController: Any
    __tabID: Any
    __questId: Any
    __challengeId: Any
    __isFirstLayoutUpdate: Any
    __createdTabs: Any
    def __init__(self, tabID, questId, challengeId):
        ...
    @property
    def viewModel(self):
        ...
    def getTabView(self, tabID):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __update(self, *_):
        ...
    def __showWinbackIntroScreen(self):
        ...
    def __isWinbackIntroShown(self):
        ...
    def _updateTabs(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getChildComponents(self):
        ...
    def __createTab(self, tabID, title):
        ...
    def __updateTab(self, tabID, challengeID=None):
        ...
    def __changeTab(self, tabID, challengeID=None):
        ...
    def __onTabChange(self, args):
        ...
    def __onContentLayoutChanged(self, args):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def __onTransitionToMission(self, event):
        ...
