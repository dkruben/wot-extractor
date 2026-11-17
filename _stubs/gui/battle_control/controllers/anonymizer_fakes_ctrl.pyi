# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/anonymizer_fakes_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
import BigWorld as BigWorld
import constants as constants
from avatar_helpers import getAvatarSessionID as getAvatarSessionID
from constants import BattleUserActions as BattleUserActions
from gui.anonymizer.battle_cooldown_manager import BattleCooldownManager as BattleCooldownManager
from gui.battle_control.battle_cache.cache_records import RelationsCacheRecord as RelationsCacheRecord
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.arena_info.interfaces import IAnonymizerFakesController as IAnonymizerFakesController
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from messenger.proto import proto_getter as proto_getter
from messenger.proto.entities import BattleUserEntity as BattleUserEntity, CurrentBattleUserEntity as CurrentBattleUserEntity
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_errors import ChatCoolDownError as ChatCoolDownError
from messenger.m_constants import USER_TAG as USER_TAG, PROTO_TYPE as PROTO_TYPE, UserEntityScope as UserEntityScope, USER_ACTION_ID as USER_ACTION_ID, CLIENT_ACTION_ID as CLIENT_ACTION_ID
from gui.battle_control.arena_info.arena_dp import ArenaDataProvider as ArenaDataProvider
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO as VehicleArenaInfoVO
_logger: Any
_ACTION_BY_TAG: dict
_CREATION_UPDATED_TAGS: tuple
_IGNORED_DEPS_TAGS: list
_IGNORE_TMP_DEPS_TAGS: list

class _RelationData(object):
    __slots__: tuple
    vehicleID: Any
    sessionID: Any
    databaseID: Any
    name: Any
    def __init__(self, vInfo):
        ...
    def isValid(self, avatarSessionID):
        ...

class AnonymizerFakesController(IAnonymizerFakesController):
    usersStorage: Any
    __slots__: tuple
    __arenaDP: Any
    __relationsCache: Any
    __cooldown: Any
    __fakeIDs: Any
    __mergedDBIDs: Any
    __avatarSessionID: Any
    __postProcs: Any
    def __init__(self, setup):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def getControllerID(self):
        ...
    def stopControl(self):
        ...
    def invalidateVehiclesInfo(self, arenaDP):
        ...
    def addVehicleInfo(self, vo, arenaDP):
        ...
    def updateVehiclesInfo(self, updated, arenaDP):
        ...
    def addBattleFriend(self, avatarSessionID):
        ...
    def removeBattleFriend(self, avatarSessionID):
        ...
    def addBattleIgnored(self, avatarSessionID):
        ...
    def removeBattleIgnored(self, avatarSessionID):
        ...
    def mute(self, avatarSessionID, name):
        ...
    def unmute(self, avatarSessionID):
        ...
    def addTmpIgnored(self, avatarSessionID, name):
        ...
    def removeTmpIgnored(self, avatarSessionID):
        ...
    def __addBattleFriend(self, user):
        ...
    def __addBattleIgnored(self, user):
        ...
    def __removeBattleIgnored(self, user):
        ...
    def __addBattleUser(self, vehicleData):
        ...
    def __buildBattleUser(self, vehicleData):
        ...
    def __clear(self):
        ...
    def __isCooldown(self, actionID):
        ...
    def __getAccDBID(self, avatarSessionID):
        ...
    def __modifyRelations(self, avatarSessionID, actionID):
        ...
    def __mergeRelations(self, vehicleData):
        ...
    def __notifyModification(self, vehicleData):
        ...
