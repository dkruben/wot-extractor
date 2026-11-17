# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/mission_details_container_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.missions import missions_helper as missions_helper
from gui.Scaleform.daapi.view.lobby.user_missions.missions_group_packers import getGroupPackerByContextID as getGroupPackerByContextID
from gui.Scaleform.daapi.view.meta.MissionDetailsContainerViewMeta import MissionDetailsContainerViewMeta as MissionDetailsContainerViewMeta
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as QUESTS_ALIASES
from gui.server_events.events_helpers import isDailyQuest as isDailyQuest, isPremium as isPremium
from gui.server_events.formatters import parseComplexToken as parseComplexToken
from gui.server_events.events_constants import BATTLE_ROYALE_GROUPS_ID as BATTLE_ROYALE_GROUPS_ID
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class MissionDetailsContainerView(LobbySubView, MissionDetailsContainerViewMeta):
    eventsCache: Any
    __battleRoyaleController: Any
    __showDQInMissionsTab = False
    __ctx: Any
    __groupPacker: Any
    __quests: Any
    __datailedList: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def requestMissionData(self, index):
        ...
    def onTokenBuyClick(self, tokenId, questId):
        ...
    def onChangePage(self, eventID):
        ...
    @classmethod
    def setShowDQInMissionsTab(cls, value):
        ...
    def _populate(self):
        ...
    def _invalidate(self, ctx=None):
        ...
    def _dispose(self):
        ...
    # decorador original: @wg_async
    def __setData(self, needDemand=True, *_):
        ...
    def __handleDetailsClose(self, _):
        ...
    def __getQuests(self, groupID):
        ...
    def __isQuestInvalid(self, eventID):
        ...
