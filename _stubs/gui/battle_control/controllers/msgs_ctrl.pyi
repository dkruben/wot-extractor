# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/msgs_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
from helpers import dependency as dependency
import BattleReplay as BattleReplay
import Event as Event
from ReplayEvents import g_replayEvents as g_replayEvents
from constants import ATTACK_REASON_INDICES as _AR_INDICES
from gui.battle_control.arena_info.arena_vos import EPIC_BATTLE_KEYS as EPIC_BATTLE_KEYS
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from items.battle_royale import isSpawnedBot as isSpawnedBot, isHunterBot as isHunterBot
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_ATTACK_REASON_CODE: dict
_PLAYER_KILL_ENEMY_SOUND = 'enemy_killed_by_player'
_PLAYER_KILL_ALLY_SOUND = 'ally_killed_by_player'
_ALLY_KILLED_SOUND = 'ally_killed_by_enemy'
_ENEMY_KILLED_SOUND = 'enemy_killed_by_ally'

class _ENTITY_TYPE(object):
    UNKNOWN = 'unknown'
    SELF = 'self'
    ALLY = 'ally'
    ENEMY = 'enemy'
    SUICIDE = 'suicide'

class BattleMessagesController(IBattleController):
    __slots__: tuple
    _battleCtx: Any
    _arenaDP: Any
    _arenaVisitor: Any
    _eManager: Any
    onShowVehicleMessageByCode: Any
    onShowVehicleMessageByKey: Any
    onShowVehicleErrorByKey: Any
    onShowPlayerMessageByCode: Any
    onShowPlayerMessageByKey: Any
    onShowDestructibleEntityMessageByCode: Any
    _attackReasonCodes: Any
    _buffer: Any
    _isUIPopulated: Any
    __specEntityStringByCode: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def showDestructibleEntityDestroyedMessage(self, avatar, destructibleID, attackerID):
        ...
    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        ...
    def showVehicleDamageInfo(self, avatar, code, targetID, entityID, extra, equipmentID, ignoreMessages=False):
        ...
    def showVehicleMessage(self, key, args=None):
        ...
    def showVehicleError(self, key, args=None):
        ...
    def showAllyHitMessage(self, vehicleID=None):
        ...
    def _getAttackReasonCodes(self, reason):
        ...
    def _getEntityType(self, avatar, entityID):
        ...
    def __getEntityString(self, avatar, entityID, code):
        ...
    def __getEntityStringDeathZone(self, avatar, entityID, code):
        ...
    def __getDamageInfo(self, avatar, code, entityID, targetID):
        ...
    def __getKillInfo(self, avatar, targetID, attackerID, reason):
        ...
    def __initSpecEntityStringFuncsByCode(self):
        ...
    def onUIPopulated(self):
        ...

class BattleMessagesPlayer(BattleMessagesController):
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        ...
    def showDestructibleEntityDestroyedMessage(self, avatar, destructibleID, attackerID):
        ...
    def showVehicleDamageInfo(self, avatar, code, targetID, entityID, extra, equipmentID, ignoreMessages=False):
        ...
    def showVehicleMessage(self, key, args=None):
        ...
    def showVehicleError(self, key, args=None):
        ...
    def showAllyHitMessage(self, vehicleID=None):
        ...
    def showInfoMessage(self, key, withBuffer=False, args=None):
        ...
    def __onWatcherNotify(self, message, args):
        ...

class EpicBattleMessagesPlayer(BattleMessagesPlayer):
    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        ...
    def _messageIsAllowedInEpicBattle(self, targetID, attackerID):
        ...

class EpicBattleMessagesController(BattleMessagesController):
    def __init__(self, setup):
        ...
    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        ...
    def _messageIsAllowedInEpicBattle(self, targetID, attackerID):
        ...

class _BRBattleMessagesMixin(object):
    _battleCtx = None
    def _getEntityType(self, avatar, entityID):
        ...
    def _playerChangedTeam(self):
        ...

class BattleRoyaleBattleMessagesController(_BRBattleMessagesMixin, BattleMessagesController):
    def showAllyHitMessage(self, vehicleID=None):
        ...
    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        ...

class BattleRoyaleBattleMessagesPlayer(_BRBattleMessagesMixin, BattleMessagesPlayer):
    def showAllyHitMessage(self, vehicleID=None):
        ...
    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _isHideVehicleKilledMsg(vehicleID, battleSessionProvider=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getSpawnedBotMsgData(vehicleID, battleSessionProvider=None):
    ...
def createBattleMessagesCtrl(setup):
    ...
