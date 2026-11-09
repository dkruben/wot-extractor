# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/battle_results/reusable/ext_shared.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/battle_results/reusable/ext_shared.py
from __future__ import absolute_import
from gui.battle_results.reusable.shared import VehicleSummarizeInfo, VehicleDetailedInfo, no_key_error

class LSVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__ = ('_phase', '_phasesCount', '_effectivenessPoints', '_totalPoints',
                 '_teamFightPlace', '_respawnsCount', '_prevBestMissionsCount', '_completedDifficultyMissions',
                 '_obeliskPoints')

    @classmethod
    @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        info = super(LSVehicleDetailedInfo, cls).makeForVehicle(vehicleID, vehicle, player, vehicleRecords, critsRecords=critsRecords)
        info._phase = vehicleRecords.get('ls_phase', 0)
        info._phasesCount = vehicleRecords.get('ls_phasesCount', 0)
        effectivenessPoints, obeliskPoints = vehicleRecords['ls_progressPoints']
        info._effectivenessPoints = effectivenessPoints
        info._obeliskPoints = obeliskPoints
        info._totalPoints = sum(vehicleRecords['ls_progressPoints'])
        info._teamFightPlace = vehicleRecords['ls_teamFightPlace']
        info._respawnsCount = vehicleRecords['ls_respawnCount']
        info._prevBestMissionsCount = vehicleRecords.get('ls_prevBestMissionsCount', 0)
        info._completedDifficultyMissions = vehicleRecords.get('ls_completedDifficultyMissions', [])
        return info

    @property
    def prevBestMissionsCount(self):
        return self._prevBestMissionsCount

    @property
    def phase(self):
        return self._phase

    @property
    def phasesCount(self):
        return self._phasesCount

    @property
    def effectivenessPoints(self):
        return self._effectivenessPoints

    @property
    def obeliskPoints(self):
        return self._obeliskPoints

    @property
    def totalPoints(self):
        return self._totalPoints

    @property
    def teamContribution(self):
        return max(1, self._damageDealt)

    @property
    def teamFightPlace(self):
        return self._teamFightPlace

    @property
    def respawnsCount(self):
        return self._respawnsCount

    @property
    def completedDifficultyMissions(self):
        return self._completedDifficultyMissions


class LSVehicleSummarizeInfo(VehicleSummarizeInfo):

    @property
    def prevBestMissionsCount(self):
        return min(self._getAtrributeGenerator('prevBestMissionsCount'))

    @property
    def phase(self):
        return self._accumulate('phase')

    @property
    def phasesCount(self):
        return self._accumulate('phasesCount')

    @property
    def effectivenessPoints(self):
        return self._accumulate('effectivenessPoints')

    @property
    def obeliskPoints(self):
        return self._accumulate('obeliskPoints')

    @property
    def totalPoints(self):
        return self._accumulate('totalPoints')

    @property
    def teamContribution(self):
        return self._accumulate('teamContribution')

    @property
    def teamFightPlace(self):
        return self._accumulate('teamFightPlace')

    @property
    def respawnsCount(self):
        return self._accumulate('respawnsCount')

    @property
    def completedDifficultyMissions(self):
        return next(self._getAtrributeGenerator('completedDifficultyMissions'), [])
