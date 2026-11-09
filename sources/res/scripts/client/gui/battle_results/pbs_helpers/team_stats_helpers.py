# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_results/pbs_helpers/team_stats_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_results/pbs_helpers/team_stats_helpers.py
import typing
from gui.battle_results.pbs_helpers.common import isPersonalBattleResult
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo
    from gui.battle_results.reusable.shared import VehicleSummarizeInfo
    from gui.battle_results.stats_ctrl import BattleResults

def isNotPersonalBattleResult(summarizeInfo, battleResults):
    return not isPersonalBattleResult(summarizeInfo, battleResults)


def hasStunEfficiency(summarizeInfo, _):
    return summarizeInfo.stunNum > 0


def hasArtilleryStrike(summarizeInfo, _):
    return summarizeInfo.artilleryFortEquipDamageDealt > 0


def getStatsParamValue(summarizeInfo, fields, _):
    return (getattr(summarizeInfo, field) for field in fields)


def getMileageValue(summarizeInfo, fields, _):
    return (getattr(summarizeInfo, field) / 1000.0 for field in fields)


def getPlayerContextMenuArgs(reusable, databaseID, vehicleCD):
    playerInfo = reusable.players.getPlayerInfo(databaseID)
    return {'dbID': databaseID, 
       'userName': (playerInfo.realName), 
       'clanAbbrev': (playerInfo.clanAbbrev), 
       'isAlly': (playerInfo.team == reusable.getPersonalTeam()), 
       'vehicleCD': vehicleCD, 
       'wasInBattle': True, 
       'clientArenaIdx': (reusable.arenaUniqueID), 
       'arenaType': (reusable.common.arenaGuiType)}
