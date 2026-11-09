# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/dyn_squad_functional.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
import Keys as Keys
import CommandMapping as CommandMapping
import Event as Event
import VOIP as VOIP
from constants import IS_CHINA as IS_CHINA
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.app_loader import sf_battle as sf_battle
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.prb_control import prbInvitesProperty as prbInvitesProperty
from gui.shared.SoundEffectsId import SoundEffectsId as SoundEffectsId
from gui.shared.utils.key_mapping import getKey as getKey, getReadableKey as getReadableKey
from helpers import dependency as dependency
from messenger.m_constants import USER_TAG as USER_TAG
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_messages import ClientActionMessage as ClientActionMessage
from messenger.proto.shared_messages import ACTION_MESSAGE_TYPE as ACTION_MESSAGE_TYPE
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.shared import g_eventBus as g_eventBus
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from skeletons.gui.game_control import IAnonymizerController as IAnonymizerController
from gui.impl.gen import R as R
from gui.impl import backport as backport
from typing import Sequence as TSequence, Tuple as TTuple
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO as VehicleArenaInfoVO
from gui.battle_control.arena_info.arena_dp import ArenaDataProvider as ArenaDataProvider
SQUAD_MEMBERS_COUNT = 2
FULL_SQUAD_MEMBERS_COUNT = 3
_R_DYN_SQUAD = R.strings.messenger.client.dynSquad
_DYN_SQUAD_PLATOON_JOINED = 'dyn_squad_platoon_joined'
_DYN_SQUAD_PLATOON_CREATED = 'dyn_squad_platoon_created'
_DYN_SQUAD_PLATOON_DISMISSED = 'dyn_squad_platoon_dismissed'
_DYN_SQUAD_BEEN_EXCLUDED_PLATOON = 'dyn_squad_been_excluded_platoon'
_DYN_SQUAD_LEFT_PLATOON = 'dyn_squad_left_platoon'
_DYN_SQUAD_ASSISTANCE_BEEN_REQUESTED = 'dyn_squad_assistance_been_requested'
_DYN_SQUAD_PLAYER_JOINED_PLATOON = 'dyn_squad_player_joined_platoon'

class DynSquadArenaController(object):
    _isBattleLoadingVisible: Any
    __sentOwnJoinMessage: Any
    __sentOwnCreateMessage: Any
    __sentEnemyCreatePlatoons: Any
    __sentAllyCreatePlatoons: Any
    __squadMembersAlly: Any
    __squadMembersEnemy: Any
    def __init__(self):
        ...
    # decorador original: @prbInvitesProperty
    def prbInvites(self):
        ...
    def __handleBattleLoading(self, event):
        ...
    def process(self, playerVehVO, arenaDP):
        ...
    def destroy(self):
        ...
    def _inviteReceived(self, invite):
        ...
    def _inviteSent(self, invite):
        ...
    def _squadCreatedImOwner(self, squadNum):
        ...
    def _squadCreatedImRecruit(self, squadNum):
        ...
    def _squadCreatedByAllies(self, squadNum):
        ...
    def _squadCreatedByEnemies(self, squadNum):
        ...
    def _iAmJoinedSquad(self, squadNum):
        ...
    def _someoneJoinedAlliedSquad(self, squadNum, receiver):
        ...
    def _someoneJoinedEnemySquad(self, squadNum, receiver):
        ...
    def _someoneJoinedMySquad(self, squadNum, receiver):
        ...
    def __onReceivedInviteModified(self, added, changed, deleted):
        ...
    def __onSentInviteListModified(self, added, changed, deleted):
        ...
    def __handleModifiedInvitesList(self, added, changed, deleted, inviteDataReceiver, callback):
        ...

class DYN_SQUAD_TYPE(object):
    OWN = 0
    ALLY = 1
    ENEMY = 2

class _DynSquadActionMessage(ClientActionMessage):
    __squadType: Any
    __squadNum: Any
    def __init__(self, message, squadType, squadNum):
        ...
    @property
    def squadType(self):
        ...
    @property
    def squadNum(self):
        ...

class DynSquadMessagesController(DynSquadArenaController):
    # decorador original: @dependency.replace_none_kwargs(...)
    def _inviteReceived(self, invite, ctrl=None):
        ...
    def _inviteSent(self, invite):
        ...
    def _squadCreatedImOwner(self, squadNum):
        ...
    def _squadCreatedImRecruit(self, squadNum):
        ...
    def _squadCreatedByAllies(self, squadNum):
        ...
    def _squadCreatedByEnemies(self, squadNum):
        ...
    def _iAmJoinedSquad(self, squadNum):
        ...
    def _someoneJoinedAlliedSquad(self, squadNum, receiver):
        ...
    def _someoneJoinedMySquad(self, squadNum, receiver):
        ...
    def __sendMessage(self, resource, **kwargs):
        ...
    def __getState(self, command):
        ...

class _DynSquadSoundsController(DynSquadArenaController):
    __slots__: tuple
    # decorador original: @sf_battle
    def app(self):
        ...
    def _squadCreatedImOwner(self, squadNum):
        ...
    def _squadCreatedImRecruit(self, squadNum):
        ...
    def _inviteReceived(self, invite):
        ...
    def _iAmJoinedSquad(self, squadNum):
        ...
    def _someoneJoinedMySquad(self, squadNum, receiver):
        ...
    def __playSound(self, sound):
        ...

class DynSquadFunctional(IArenaVehiclesController):
    __slots__: tuple
    __soundCtrl: Any
    __msgsCtrl: Any
    __eManager: Any
    __wasOwnSquadCreated: Any
    onDynSquadCreatedOrJoined: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def stopControl(self):
        ...
    def updateVehiclesInfo(self, updated, arenaDP):
        ...
    def __checkIfAccountCreatedOrJoinedDynSquad(self, playerVehVO, arenaDP):
        ...

def _getVIOPState(key):
    ...
