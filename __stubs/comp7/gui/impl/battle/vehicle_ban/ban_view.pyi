# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
import SoundGroups as SoundGroups
from ReplayEvents import g_replayEvents as g_replayEvents
from comp7.gui.battle_control.arena_info.arena_vos import Comp7Keys as Comp7Keys
from comp7.gui.battle_control.arena_info.vos_collections import Comp7SortKey as Comp7SortKey
from comp7.gui.impl.battle.tooltips.ban_show_tooltip import BanShowTooltip as BanShowTooltip
from comp7.gui.impl.battle.vehicle_ban.ban_helpers import convertVehicleCD as convertVehicleCD, fillComp7VehicleModel as fillComp7VehicleModel, fillBanProgressionModel as fillBanProgressionModel, getOwnDatabaseID as getOwnDatabaseID
from comp7.gui.impl.gen.view_models.views.battle.ban_view_model import BanViewModel as BanViewModel
from comp7.gui.impl.gen.view_models.views.battle.comp7_vehicle_model import Comp7VehicleModel as Comp7VehicleModel
from comp7.gui.impl.gen.view_models.views.battle.constants import Constants as Constants
from comp7.gui.impl.gen.view_models.views.battle.player_model import PlayerModel as PlayerModel
from comp7.gui.impl.gen.view_models.views.lobby.enums import Division as Division, Rank as Rank, SeasonName as SeasonName
from comp7_core.gui.battle_control.controllers.sound_ctrls.comp7_battle_sounds import BAN_VIEW_SOUND_SPACE as BAN_VIEW_SOUND_SPACE
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from comp7_core_constants import ArenaPrebattlePhase as ArenaPrebattlePhase
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import GUI_NATIONS as GUI_NATIONS
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.window_impl import WindowImpl as WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from messenger.m_constants import USER_ACTION_ID as USER_ACTION_ID, UserEntityScope as UserEntityScope
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from typing import Optional as Optional, Tuple as Tuple
from frameworks.wulf import Array as Array
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO as VehicleArenaInfoVO
from messenger.proto.entities import UserEntity as UserEntity
SOUND_NAME = 'comp_7_bans_choice_confirm'

class BanView(ViewImpl, BattleGUIKeyHandler):
    __slots__: tuple
    _COMMON_SOUND_SPACE = BAN_VIEW_SOUND_SPACE
    __comp7Controller: Any
    __sessionProvider: Any
    __appLoader: Any
    __usersStorage: Any
    __muteActions: set
    __selectionTimer: Any
    def __init__(self):
        ...
    def handleEscKey(self, isDown):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def _battleApp(self):
        ...
    def _initialize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __updateData(self, *_):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updatePhaseData(self, model=None):
        ...
    def __setVehicles(self, viewModel):
        ...
    def __fillPlayerModel(self, vehicleInfo, vehicleCDToBan, isConfirmed, playerModel=None):
        ...
    def __setPlayers(self, viewModel):
        ...
    def __onPlayerSpeaking(self, accountDBID, isSpeaking):
        ...
    def __onUserActionReceived(self, actionID, user, shadowMode):
        ...
    def __onChatAction(self, playerDBID, isMuted, isIgnored):
        ...
    def __onClose(self):
        ...
    # decorador original: @args2params(...)
    def __onSelect(self, vehicleCD):
        ...
    # decorador original: @args2params(...)
    def __onConfirm(self, vehicleCD):
        ...
    def __onPollServerTime(self):
        ...
    def __onBanPhaseUpdated(self):
        ...
    def __onStatusUpdated(self, status):
        ...
    def __onConfigChanged(self):
        ...
    def __getVehicleBanCtrl(self):
        ...
    def __getPlayerBanState(self, playerDatabaseID):
        ...
    def __setSelectionAvailable(self):
        ...
    def __onReplayTimeWarp(self):
        ...
    @staticmethod
    def __playSound():
        ...
    def __destroyWindow(self):
        ...

class BanViewWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, parent=None):
        ...
