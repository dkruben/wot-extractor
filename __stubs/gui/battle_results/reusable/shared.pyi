# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/reusable/shared.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import operator as operator
from account_shared import getFairPlayViolationName as getFairPlayViolationName
from constants import DEATH_REASON_ALIVE as DEATH_REASON_ALIVE
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from dossiers2.ui import achievements as achievements, layouts as layouts
from dossiers2.ui.achievements import MARK_OF_MASTERY as MARK_OF_MASTERY
from gui.battle_results.reusable import sort_keys as sort_keys
from gui.shared.crits_mask_parser import CRIT_MASK_SUB_TYPES as CRIT_MASK_SUB_TYPES, critsParserGenerator as critsParserGenerator
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.gui_items.dossier import getAchievementFactory as getAchievementFactory
from items import vehicles as vehicles_core
from shared_utils import findFirst as findFirst

class ItemInfo(object):
    __slots__: tuple
    __wasInBattle: Any
    def __init__(self, wasInBattle=True):
        ...
    @property
    def wasInBattle(self):
        ...

class UnpackedInfo(object):
    __slots__: tuple
    __unpackedItemsIDs: Any
    def __init__(self):
        ...
    def getNumberOfUnpackedItems(self):
        ...
    def hasUnpackedItems(self):
        ...
    def _addUnpackedItemID(self, itemUniqueID):
        ...

class TeamBasesInfo(object):
    __slots__: tuple
    __capturePoints: Any
    __droppedCapturePoints: Any
    def __init__(self, capturePoints=0, droppedCapturePoints=0):
        ...
    @property
    def capturePoints(self):
        ...
    @property
    def droppedCapturePoints(self):
        ...

class _VehicleInfo(object):
    __slots__: tuple
    _vehicleID: Any
    _player: Any
    _deathReason: Any
    def __init__(self, vehicleID, player, deathReason=...):
        ...
    @property
    def vehicleID(self):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def killerID(self):
        ...
    @property
    def player(self):
        ...
    @property
    def deathReason(self):
        ...
    @property
    def achievementsIDs(self):
        ...
    @property
    def spotted(self):
        ...
    @property
    def piercings(self):
        ...
    @property
    def piercingsReceived(self):
        ...
    @property
    def damageDealt(self):
        ...
    @property
    def tdamageDealt(self):
        ...
    @property
    def sniperDamageDealt(self):
        ...
    @property
    def artilleryFortEquipDamageDealt(self):
        ...
    @property
    def kills(self):
        ...
    @property
    def tkills(self):
        ...
    @property
    def targetKills(self):
        ...
    @property
    def noDamageDirectHitsReceived(self):
        ...
    @property
    def damageBlockedByArmor(self):
        ...
    @property
    def rickochetsReceived(self):
        ...
    @property
    def damageAssistedTrack(self):
        ...
    @property
    def damageAssistedRadio(self):
        ...
    @property
    def damageAssisted(self):
        ...
    @property
    def damageAssistedStun(self):
        ...
    @property
    def stunNum(self):
        ...
    @property
    def stunDuration(self):
        ...
    @property
    def critsInfo(self):
        ...
    @property
    def critsCount(self):
        ...
    @property
    def shots(self):
        ...
    @property
    def explosionHits(self):
        ...
    @property
    def directHits(self):
        ...
    @property
    def directHitsReceived(self):
        ...
    @property
    def explosionHitsReceived(self):
        ...
    @property
    def damaged(self):
        ...
    @property
    def mileage(self):
        ...
    @property
    def capturePoints(self):
        ...
    @property
    def droppedCapturePoints(self):
        ...
    @property
    def xp(self):
        ...
    @property
    def xpForAttack(self):
        ...
    @property
    def xpForAssist(self):
        ...
    @property
    def xpOther(self):
        ...
    @property
    def xpPenalty(self):
        ...
    @property
    def isTeamKiller(self):
        ...
    @property
    def isKilledByTeamKiller(self):
        ...
    @property
    def deathCount(self):
        ...
    @property
    def rollouts(self):
        ...
    @property
    def respawns(self):
        ...
    @property
    def numDefended(self):
        ...
    @property
    def numRecovered(self):
        ...
    @property
    def numCaptured(self):
        ...
    @property
    def numDestroyed(self):
        ...
    @property
    def destructiblesDamageDealt(self):
        ...
    @property
    def equipmentDamageDealt(self):
        ...
    @property
    def equipmentDamageAssisted(self):
        ...
    def getOrderByClass(self):
        ...

class VehicleDetailedInfo(_VehicleInfo):
    __slots__: tuple
    _vehicle: Any
    _killerID: Any
    _achievementsIDs: Any
    _critsInfo: Any
    _spotted: Any
    _piercings: Any
    _piercingEnemyHits: Any
    _piercingsReceived: Any
    _damageBlockedByArmor: Any
    _rickochetsReceived: Any
    _noDamageDirectHitsReceived: Any
    _targetKills: Any
    _damageDealt: Any
    _tdamageDealt: Any
    _sniperDamageDealt: Any
    _artilleryFortEquipDamageDealt: Any
    _equipmentDamageDealt: Any
    _damageAssistedTrack: Any
    _damageAssistedRadio: Any
    _damageAssistedStun: Any
    _equipmentDamageAssisted: Any
    _stunNum: Any
    _stunDuration: Any
    _directHits: Any
    _directEnemyHits: Any
    _directHitsReceived: Any
    _explosionHits: Any
    _explosionHitsReceived: Any
    _shots: Any
    _kills: Any
    _tkills: Any
    _damaged: Any
    _mileage: Any
    _capturePoints: Any
    _droppedCapturePoints: Any
    _xp: Any
    _fire: Any
    _isTeamKiller: Any
    _rollouts: Any
    _respawns: Any
    _deathCount: Any
    _xpForAssist: Any
    _xpForAttack: Any
    _xpOther: Any
    _xpPenalty: Any
    _isKilledByTeamKiller: Any
    _numRecovered: Any
    _vehicleNumCaptured: Any
    _destructiblesNumDestroyed: Any
    _destructiblesDamageDealt: Any
    _numDefended: Any
    _achievedLevel: Any
    def __init__(self, vehicleID, vehicle, player, deathReason=...):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def killerID(self):
        ...
    @property
    def achievementsIDs(self):
        ...
    @property
    def spotted(self):
        ...
    @property
    def piercings(self):
        ...
    @property
    def piercingEnemyHits(self):
        ...
    @property
    def piercingsReceived(self):
        ...
    @property
    def damageDealt(self):
        ...
    @property
    def tdamageDealt(self):
        ...
    @property
    def sniperDamageDealt(self):
        ...
    @property
    def artilleryFortEquipDamageDealt(self):
        ...
    @property
    def equipmentDamageDealt(self):
        ...
    @property
    def targetKills(self):
        ...
    @property
    def noDamageDirectHitsReceived(self):
        ...
    @property
    def damageBlockedByArmor(self):
        ...
    @property
    def rickochetsReceived(self):
        ...
    @property
    def damageAssistedTrack(self):
        ...
    @property
    def damageAssistedRadio(self):
        ...
    @property
    def damageAssisted(self):
        ...
    @property
    def damageAssistedStun(self):
        ...
    @property
    def equipmentDamageAssisted(self):
        ...
    @property
    def stunNum(self):
        ...
    @property
    def stunDuration(self):
        ...
    @property
    def critsInfo(self):
        ...
    @property
    def critsCount(self):
        ...
    @property
    def shots(self):
        ...
    @property
    def explosionHits(self):
        ...
    @property
    def directHits(self):
        ...
    @property
    def directEnemyHits(self):
        ...
    @property
    def directHitsReceived(self):
        ...
    @property
    def explosionHitsReceived(self):
        ...
    @property
    def kills(self):
        ...
    @property
    def tkills(self):
        ...
    @property
    def damaged(self):
        ...
    @property
    def mileage(self):
        ...
    @property
    def capturePoints(self):
        ...
    @property
    def droppedCapturePoints(self):
        ...
    @property
    def xp(self):
        ...
    @property
    def isTeamKiller(self):
        ...
    @property
    def isKilledByTeamKiller(self):
        ...
    @property
    def deathCount(self):
        ...
    @property
    def rollouts(self):
        ...
    @property
    def respawns(self):
        ...
    @property
    def achievedLevel(self):
        ...
    @property
    def numDefended(self):
        ...
    @property
    def numRecovered(self):
        ...
    @property
    def numCaptured(self):
        ...
    @property
    def numDestroyed(self):
        ...
    @property
    def destructiblesDamageDealt(self):
        ...
    @property
    def xpForAssist(self):
        ...
    @property
    def xpForAttack(self):
        ...
    @property
    def xpOther(self):
        ...
    @property
    def xpPenalty(self):
        ...
    def haveInteractionDetails(self):
        ...
    @classmethod
    # decorador original: @no_key_error
    def makeForEnemy(cls, vehicleID, vehicle, player, detailsRecords, deathReason=..., isTeamKiller=False):
        ...
    @classmethod
    # decorador original: @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        ...
    @classmethod
    def _setSharedRecords(cls, info, records):
        ...

class VehicleSummarizeInfo(_VehicleInfo):
    __slots__: tuple
    __avatar: Any
    __vehicles: Any
    def __init__(self, vehicleID, player):
        ...
    @property
    def avatar(self):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def isTeamKiller(self):
        ...
    @property
    def isKilledByTeamKiller(self):
        ...
    @property
    def vehicles(self):
        ...
    @property
    def killerID(self):
        ...
    @property
    def deathReason(self):
        ...
    @property
    def achievementsIDs(self):
        ...
    @property
    def spotted(self):
        ...
    @property
    def piercings(self):
        ...
    @property
    def piercingEnemyHits(self):
        ...
    @property
    def piercingsReceived(self):
        ...
    @property
    def damageDealt(self):
        ...
    @property
    def tdamageDealt(self):
        ...
    @property
    def sniperDamageDealt(self):
        ...
    @property
    def artilleryFortEquipDamageDealt(self):
        ...
    @property
    def targetKills(self):
        ...
    @property
    def noDamageDirectHitsReceived(self):
        ...
    @property
    def damageBlockedByArmor(self):
        ...
    @property
    def rickochetsReceived(self):
        ...
    @property
    def damageAssistedTrack(self):
        ...
    @property
    def damageAssistedRadio(self):
        ...
    @property
    def damageAssisted(self):
        ...
    @property
    def damageAssistedStun(self):
        ...
    @property
    def stunNum(self):
        ...
    @property
    def stunDuration(self):
        ...
    @property
    def critsInfo(self):
        ...
    @property
    def critsCount(self):
        ...
    @property
    def shots(self):
        ...
    @property
    def explosionHits(self):
        ...
    @property
    def directHits(self):
        ...
    @property
    def directEnemyHits(self):
        ...
    @property
    def directHitsReceived(self):
        ...
    @property
    def explosionHitsReceived(self):
        ...
    @property
    def kills(self):
        ...
    @property
    def tkills(self):
        ...
    @property
    def damaged(self):
        ...
    @property
    def mileage(self):
        ...
    @property
    def capturePoints(self):
        ...
    @property
    def droppedCapturePoints(self):
        ...
    @property
    def xp(self):
        ...
    @property
    def xpForAttack(self):
        ...
    @property
    def xpForAssist(self):
        ...
    @property
    def xpOther(self):
        ...
    @property
    def xpPenalty(self):
        ...
    @property
    def deathCount(self):
        ...
    @property
    def rollouts(self):
        ...
    @property
    def respawns(self):
        ...
    @property
    def numDefended(self):
        ...
    @property
    def numRecovered(self):
        ...
    @property
    def numCaptured(self):
        ...
    @property
    def numDestroyed(self):
        ...
    @property
    def destructiblesDamageDealt(self):
        ...
    @property
    def equipmentDamageDealt(self):
        ...
    @property
    def equipmentDamageAssisted(self):
        ...
    def addVehicleInfo(self, info):
        ...
    def addAvatarInfo(self, avatar):
        ...
    def getVehiclesIterator(self):
        ...
    def getAchievements(self):
        ...
    def _getAtrributeGenerator(self, attr):
        ...
    def _findFirstNoZero(self, attr):
        ...
    def _findMaxInt(self, attr, start=0):
        ...
    def _collectToSet(self, attr):
        ...
    def _collectToDict(self, attr):
        ...
    def _accumulate(self, attr):
        ...

class FairplayViolationsInfo(object):
    __slots__: tuple
    _warningsMask: Any
    _penaltiesMask: Any
    _violationsMask: Any
    _penaltiesInPercent: Any
    def __init__(self, warningsMask=0, penaltiesMask=0, violationsMask=0, penaltiesInPercent=-100):
        ...
    def hasWarnings(self):
        ...
    def hasPenalties(self):
        ...
    def hasViolations(self):
        ...
    def getWarningName(self):
        ...
    def getPenaltyName(self):
        ...
    def getViolationName(self):
        ...
    def getPenaltyDetails(self):
        ...

def makeAchievementFromPersonal(results):
    ...
def makeMarkOfMasteryFromPersonal(results):
    ...
def makeCritsInfo(value):
    ...
def unionCritsInfo(destination, source):
    ...
def no_key_error(func):
    ...
