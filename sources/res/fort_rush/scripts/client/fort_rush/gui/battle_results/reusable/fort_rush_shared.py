# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/battle_results/reusable/fort_rush_shared.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/battle_results/reusable/fort_rush_shared.py
from __future__ import absolute_import
from gui.battle_results.reusable.shared import VehicleSummarizeInfo, VehicleDetailedInfo, no_key_error

class FortRushVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__ = ('_fortRushScore', )

    @classmethod
    @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        info = super(FortRushVehicleDetailedInfo, cls).makeForVehicle(vehicleID, vehicle, player, vehicleRecords, critsRecords=critsRecords)
        info._fortRushScore = vehicleRecords['fortRush/scorePoints']
        return info

    @property
    def fortRushScore(self):
        return self._fortRushScore


class FortRushVehicleSummarizeInfo(VehicleSummarizeInfo):

    @property
    def fortRushScore(self):
        return self._accumulate('fortRushScore')
