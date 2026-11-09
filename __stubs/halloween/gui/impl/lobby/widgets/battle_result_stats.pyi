# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/battle_result_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from adisp import adisp_process as adisp_process
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowStatus as WindowStatus
from gui.impl.backport import createContextMenuData as createContextMenuData, BackportContextMenuWindow as BackportContextMenuWindow
from gui.prb_control import prbInvitesProperty as prbInvitesProperty
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from halloween.gui.impl.gen.view_models.views.common.stat_column_settings_model import ColumnEnum as ColumnEnum
from halloween.gui.impl.gen.view_models.views.battle.event_stats_view_model import EventStatsViewModel as EventStatsViewModel
from halloween.gui.impl.gen.view_models.views.common.base_team_member_model import TeamMemberBanType as TeamMemberBanType
from halloween.gui.impl.gen.view_models.views.battle.event_stats_team_member_model import EventStatsTeamMemberModel as EventStatsTeamMemberModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from halloween.gui.scaleform.genConsts.HALLOWEEN_CM_HANDLER_TYPE import HALLOWEEN_CM_HANDLER_TYPE as HALLOWEEN_CM_HANDLER_TYPE
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from helpers import dependency as dependency
from messenger.m_constants import UserEntityScope as UserEntityScope, USER_TAG as USER_TAG, PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.entities import SharedUserEntity as SharedUserEntity
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from messenger.proto.entities import ClanInfo as UserClanInfo
from gui.prb_control.settings import PRB_INVITE_STATE as PRB_INVITE_STATE
from halloween.gui.halloween_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from halloween_common.halloween_constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
_CHECK_FRIEND_TIMEOUT = 5.0
_DEFAULT_CONTEXT_MENU_PLAYER_ID = -1
_logger: Any

class BattleResultStats(ViewImpl, IGlobalListener, CallbackDelayer):
    battleResults: Any
    platoonCtrl: Any
    hwController: Any
    lobbyContext: Any
    usersStorage: Any
    __arenaUniqueID: Any
    __contextMenuWindow: Any
    __totalVO: Any
    __uiLogger: Any
    def __init__(self, totalVO, arenaUniqueID, flags=..., *args, **kwargs):
        ...
    def createContextMenu(self, event):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    # decorador original: @prbInvitesProperty
    def prbInvites(self):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onUserActionReceived(self, _, user, __):
        ...
    def _onUserStatusUpdated(self, user):
        ...
    def _addEventListeners(self):
        ...
    def _removeEventListeners(self):
        ...
    def _sendFriendRequest(self, args=None):
        ...
    # decorador original: @adisp_process
    def _sendPlatoonInvitation(self, args):
        ...
    def _removeFromBlacklist(self, args=None):
        ...
    def _onSentInviteListModified(self, added, changed, deleted):
        ...
    def _onMembersSquadUpdate(self):
        ...
    def __onStatusChangedContextMenu(self, windowStatus):
        ...
    def __isFriend(self, dbID):
        ...
    def __isRequestFriendSent(self, dbID):
        ...
    def __isRequestSquadSent(self, dbID):
        ...
    def __isPlayerInSquad(self, dbID):
        ...
    def __isPlayerInIgnoreList(self, dbID):
        ...
    def __canCreateSquad(self):
        ...
    def __checkUserStatusUpdate(self, user):
        ...
    def __setStatusPlatoonRequestSent(self, dbID, state):
        ...
    def __checkFriendOnDelay(self, dbID):
        ...
    def __setColumns(self, model=None):
        ...
    def __makeTeamMemberModel(self, idx, playerVO):
        ...
    def __fillViewModel(self, model):
        ...
    def __updateView(self):
        ...
