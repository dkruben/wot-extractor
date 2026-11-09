# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/vehicle_menu_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/vehicle_menu_model.py
from frameworks.wulf import Map, ViewModel

class VehicleMenuModel(ViewModel):
    __slots__ = ('onNavigate', )
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    WARNING = 'warning'
    CRITICAL = 'critical'
    UNAVAILABLE = 'unavailable'
    PRO_BOOST_TOOLTIP_LOCKED = 'locked'
    PRO_BOOST_TOOLTIP_ACTIVE = 'active'
    PRO_BOOST_TOOLTIP_LOCKED_ACTIVE = 'lockedActive'
    PRO_BOOST_TOOLTIP_INCOMPATIBLE_VEHICLE = 'incompatibleVehicle'
    PRO_BOOST_TOOLTIP_INCOMPATIBLE_MODE = 'incompatibleMode'
    BATTLE_NEEDED = 'battleNeeded'
    CREW_MEMBERS_RETIRED = 'crewMembersRetired'

    def __init__(self, properties=1, commands=1):
        super(VehicleMenuModel, self).__init__(properties=properties, commands=commands)

    def getMenuEntries(self):
        return self._getMap(0)

    def setMenuEntries(self, value):
        self._setMap(0, value)

    @staticmethod
    def getMenuEntriesType():
        return (int, unicode)

    def _initialize(self):
        super(VehicleMenuModel, self)._initialize()
        self._addMapProperty('menuEntries', Map(int, unicode))
        self.onNavigate = self._addCommand('onNavigate')
