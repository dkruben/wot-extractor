# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/tooltips/crew_roles_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/tooltips/crew_roles_tooltip_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.tooltips.crew_member_model import CrewMemberModel

class CrewRolesTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CrewRolesTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)

    def getCrew(self):
        return self._getArray(1)

    def setCrew(self, value):
        self._setArray(1, value)

    @staticmethod
    def getCrewType():
        return CrewMemberModel

    def _initialize(self):
        super(CrewRolesTooltipViewModel, self)._initialize()
        self._addStringProperty('vehicleName', '')
        self._addArrayProperty('crew', Array())
