# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/base/squad/mixins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/base/squad/mixins.py
from gui.prb_control.entities.base.squad.components import SquadRestrictionsProvider

class SquadRestrictionsMixin(object):

    def __init__(self):
        self.__squadRestrictionsProvider = self._createSquadRestrictionsProvider()

    def initRestrictedRoleDataProvider(self, unit):
        self.__squadRestrictionsProvider.init(unit)

    def finiRestrictedRoleDataProvider(self):
        self.__squadRestrictionsProvider.fini()

    def isSquadRestrictionValid(self):
        return self.__squadRestrictionsProvider.isValid()

    def isVehicleSuitableForSquad(self, vehicle):
        hasSlot, _ = self.__squadRestrictionsProvider.hasSlotForVehicle(vehicle, ignoreOwnVehiclesInUnit=True)
        return hasSlot

    def hasSlotForVehicle(self, vehicle):
        return self.__squadRestrictionsProvider.hasSlotForVehicle(vehicle)

    @property
    def squadRestrictions(self):
        raise NotImplementedError

    @classmethod
    def _createSquadRestrictionsProvider(cls):
        return SquadRestrictionsProvider()
