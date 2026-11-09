# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/hangar_header.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import constants as constants
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui import g_guiResetters as g_guiResetters
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.flag_constants import QuestFlagTypes as QuestFlagTypes
from gui.Scaleform.daapi.view.meta.HangarHeaderMeta import HangarHeaderMeta as HangarHeaderMeta
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.battle_pass.battle_pass_helpers import getSupportedArenaBonusTypeFor as getSupportedArenaBonusTypeFor
from gui.event_boards.listener import IEventBoardsListener as IEventBoardsListener
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.event_boards_controllers import IEventBoardController as IEventBoardController
from skeletons.gui.game_control import IHangarGuiController as IHangarGuiController, IMarathonEventsController as IMarathonEventsController, IRankedBattlesController as IRankedBattlesController, IBattleRoyaleController as IBattleRoyaleController, IMapboxController as IMapboxController, ILimitedUIController as ILimitedUIController, ILiveOpsWebEventsController as ILiveOpsWebEventsController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from typing import Optional as Optional
_logger: Any
_SCREEN_WIDTH_FOR_MARATHON_GROUP = 1300

class ActiveWidgets(object):
    LEFT = 1
    CENTER = 2
    RIGHT = 3
    __widgets: Any
    def __init__(self):
        ...
    def update(self, position, alias):
        ...

class HangarHeader(HangarHeaderMeta, IGlobalListener, IEventBoardsListener):
    __slots__: tuple
    __battleMattersController: Any
    __battleRoyaleController: Any
    _eventsCache: Any
    _eventsController: Any
    __hangarGuiCtrl: Any
    __limitedUIController: Any
    __liveOpsWebEventsController: Any
    __lobbyContext: Any
    __mapboxCtrl: Any
    _marathonsCtrl: Any
    __rankedController: Any
    _currentVehicle: Any
    __screenWidth: Any
    __activeWidgets: Any
    def __init__(self):
        ...
    def onQuestBtnClick(self, questType, questID):
        ...
    def onUpdateHangarFlag(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def update(self, *_):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _makeHeaderVO(self):
        ...
    def __onChangeScreenResolution(self):
        ...
    def __onBattleMattersStateChanged(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __getCurentArenaBonusType(self):
        ...
    def __updateWidget(self):
        ...
    def __updateVOHeader(self, *_):
        ...
    def __updateRightWidget(self, *_):
        ...
    def __updateBattleMattersEntryPoint(self, *_):
        ...
