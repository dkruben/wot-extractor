# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/crew_header_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/crew_header_tooltip_view_model.py
from gui.impl.gen.view_models.views.lobby.crew.idle_crew_bonus import IdleCrewBonus

class CrewHeaderTooltipViewModel(IdleCrewBonus):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CrewHeaderTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getBonusXpPerFiveMinutes(self):
        return self._getNumber(1)

    def setBonusXpPerFiveMinutes(self, value):
        self._setNumber(1, value)

    def getVehicleName(self):
        return self._getString(2)

    def setVehicleName(self, value):
        self._setString(2, value)

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)

    def getVehicleLvl(self):
        return self._getString(4)

    def setVehicleLvl(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(CrewHeaderTooltipViewModel, self)._initialize()
        self._addNumberProperty('bonusXpPerFiveMinutes', 50)
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('vehicleType', '')
        self._addStringProperty('vehicleLvl', '')
