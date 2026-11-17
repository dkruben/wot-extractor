# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/battle_queue/battle_queue.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
import MusicControllerWWISE as MusicControllerWWISE
import constants as constants
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_DEBUG as LOG_DEBUG
from frameworks.wulf import WindowLayer as WindowLayer
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import getClanTag as getClanTag
from gui.Scaleform.daapi.view.lobby.rally import vo_converters as vo_converters
from gui.Scaleform.daapi.view.meta.BattleQueueMeta import BattleQueueMeta as BattleQueueMeta
from gui.Scaleform.daapi.view.meta.BattleStrongholdsQueueMeta import BattleStrongholdsQueueMeta as BattleStrongholdsQueueMeta
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES as ITEM_TYPES
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control import prb_getters as prb_getters, prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME, getTypeBigIconPath as getTypeBigIconPath
from gui.shared.image_helper import getTextureLinkByID as getTextureLinkByID, ImagesFetchCoordinator as ImagesFetchCoordinator
from gui.shared.system_factory import registerBattleQueueProvider as registerBattleQueueProvider, collectBattleQueueProvider as collectBattleQueueProvider
from gui.shared.view_helpers import ClanEmblemsHelper as ClanEmblemsHelper
from gui.sounds.ambients import BattleQueueEnv as BattleQueueEnv
from helpers import dependency as dependency, i18n as i18n, time_utils as time_utils, int2roman as int2roman
from helpers.i18n import makeString as makeString
from helpers.time_utils import getCurrentTimestamp as getCurrentTimestamp
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
TYPES_ORDERED: tuple
_LONG_WAITING_LEVELS: tuple
_HTMLTEMP_PLAYERSLABEL = 'html_templates:lobby/queue/playersLabel'

class QueueProvider(object):
    _proxy: Any
    _queueType: Any
    _queueCallback: Any
    def __init__(self, proxy, qType=...):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def getQueueType(self):
        ...
    def requestQueueInfo(self):
        ...
    def processQueueInfo(self, qInfo):
        ...
    def needAdditionalInfo(self):
        ...
    def additionalInfo(self):
        ...
    def getAdditionalParams(self):
        ...
    def getTitle(self, guiType):
        ...
    def getIconPath(self, iconLabel):
        ...
    def getTankInfoLabel(self):
        ...
    def getTankIcon(self, vehicle):
        ...
    def getTankName(self, vehicle):
        ...
    def getLayoutStr(self):
        ...
    def forceStart(self):
        ...
    def _doRequestQueueInfo(self, currPlayer):
        ...
    def _getRequestQueueInfoParams(self):
        ...

class RandomQueueProvider(QueueProvider):
    _needAdditionalInfo: Any
    def __init__(self, proxy, qType=...):
        ...
    def processQueueInfo(self, qInfo):
        ...
    def needAdditionalInfo(self):
        ...
    def additionalInfo(self):
        ...
    @staticmethod
    def _isStartButtonDisplayed(vClasses):
        ...
    def _createCommonPlayerString(self, playerCount):
        ...

class _EventQueueProvider(RandomQueueProvider):
    ...

class _RankedQueueProvider(RandomQueueProvider):
    ...

class _MapboxQueueProvider(RandomQueueProvider):
    ...

class _WinbackQueueProvider(RandomQueueProvider):
    __winbackController: Any
    def getLayoutStr(self):
        ...
    def getTitle(self, guiType):
        ...
    def getAdditionalParams(self):
        ...

class BattleQueue(BattleQueueMeta, LobbySubView):
    __sound_env__ = BattleQueueEnv
    __createTime: Any
    __timerCallback: Any
    __provider: Any
    _blur: Any
    def __init__(self, **kwargs):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def onEscape(self):
        ...
    def startClick(self):
        ...
    def exitClick(self):
        ...
    def onStartBattle(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __updateClientState(self):
        ...
    def __stopUpdateScreen(self):
        ...
    def __updateQueueInfo(self):
        ...
    def __updateTimer(self):
        ...
    def _getProvider(self):
        ...
    def _onHideExternals(self, _):
        ...
    def _onShowExternals(self, _):
        ...

class BattleStrongholdsQueue(BattleStrongholdsQueueMeta, LobbySubView, ClanEmblemsHelper, IGlobalListener):
    __sound_env__ = BattleQueueEnv
    itemsCache: Any
    ANIMATION_DEFAULT_DURATION = 5
    __timerCallback: Any
    __startAnimationTime: Any
    __animationDuration: Any
    __groups: Any
    __battleQueueVO: Any
    __imagesFetchCoordinator: Any
    _blur: Any
    def __init__(self, **kwargs):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def exitClick(self):
        ...
    def onClanEmblem32x32Received(self, clanDbID, emblem):
        ...
    def onEscape(self):
        ...
    def onStartBattle(self):
        ...
    def onStrongholdMaintenance(self, state):
        ...
    def onUnitFlagsChanged(self, flags, timeLeft):
        ...
    def onUpdateHeader(self, header, isFirstBattle, isUnitFreezed):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getBattleQueueVO(self):
        ...
    def __requestClanIcon(self):
        ...
    def __getTitle(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __parseClanData(self, clanData, serviceLeaguesEnabled, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __parseGroupsData(self, groupsData, callback):
        ...
    # decorador original: @adisp_process
    def __onMatchmakingInfo(self, response):
        ...
    def __stopUpdateScreen(self):
        ...
    def __onMatchmakingTimerChanged(self, event):
        ...
    @staticmethod
    def __showBattleRoom():
        ...
    def _onHideExternals(self, _):
        ...
    def _onShowExternals(self, _):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def needShowLongWaitingWarning(lobbyContext=None):
    ...
def _providerFactory(proxy, qType):
    ...
