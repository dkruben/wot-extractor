# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/rage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/rage.py
from __future__ import absolute_import
import ResMgr
from items import vehicles
_CONFIG_FILE = 'scripts/item_defs/rage.xml'

class DamageSettings(object):

    def __init__(self, section):
        self.damageFactor = section['damageFactor'].asFloat
        self.pointsForKill = section['ragePointsForKill'].asFloat


class RageTeamOrSoloSettings(object):

    def __init__(self, section):
        self.vehicleDamageSettings = DamageSettings(section['vehicle'])
        self.equipmentDamageSettings = DamageSettings(section['equipment'])
        self.pointsForFlagPickup = section['ragePointsForFlagPickup'].asFloat
        self.pointsForFlagCapture = section['ragePointsForFlagCapture'].asFloat
        self.pointsForOneResource = section['ragePointsForOneResource'].asFloat
        self.deathPenalty = section['deathPenalty'].asFloat


RageTeamSettings = RageTeamOrSoloSettings
RageSoloSettings = RageTeamOrSoloSettings

class RageSettings(object):

    def __init__(self, section):
        self.pointsLimit = section['ragePointsLimit'].asFloat
        self.equipments = {}
        for subsection in section['equipments'].values():
            id = vehicles.g_cache.equipmentIDs()[subsection['name'].asString]
            equipment = vehicles.g_cache.equipments()[id]
            self.equipments[equipment.compactDescr] = subsection['costInRagePoints'].asFloat

        self.teamSettings = RageTeamSettings(section['team'])
        self.soloSettings = RageSoloSettings(section['solo'])

    def damageFactor(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.damageFactor

    def pointsForKill(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.pointsForKill

    def __getattr__(self, item):
        if item in ('pointsForFlagPickup', 'pointsForFlagCapture', 'pointsForOneResource',
                    'deathPenalty'):
            return (lambda isSolo: getattr(self.soloSettings, item) if isSolo else getattr(self.teamSettings, item))
        return super(RageSettings, self).__getattr__(item)


g_cache = None

def init():
    global g_cache
    section = ResMgr.openSection(_CONFIG_FILE)
    g_cache = RageSettings(section)
