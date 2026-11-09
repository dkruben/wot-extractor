# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/idle_crew_bonus.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/idle_crew_bonus.py
from enum import Enum
from frameworks.wulf import ViewModel

class IdleCrewBonusEnum(Enum):
    DISABLED = 'Disabled'
    ENABLED = 'Enabled'
    ACTIVEONCURRENTVEHICLE = 'ActiveOnCurrentVehicle'
    INCOMPATIBLEWITHCURRENTVEHICLE = 'IncompatibleWithCurrentVehicle'
    ACTIVEONANOTHERVEHICLE = 'ActiveOnAnotherVehicle'
    POSTPROGRESSIONREACHED = 'PostProgressionReached'
    INVISIBLE = 'Invisible'


class IdleCrewBonus(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(IdleCrewBonus, self).__init__(properties=properties, commands=commands)

    def getIdleCrewBonus(self):
        return IdleCrewBonusEnum(self._getString(0))

    def setIdleCrewBonus(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(IdleCrewBonus, self)._initialize()
        self._addStringProperty('IdleCrewBonus')
