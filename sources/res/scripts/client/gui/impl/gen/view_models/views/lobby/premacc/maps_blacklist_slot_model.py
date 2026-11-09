# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/premacc/maps_blacklist_slot_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/maps_blacklist_slot_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class MapStateEnum(Enum):
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE = 'active'
    MAPS_BLACKLIST_SLOT_STATE_CHANGE = 'change'
    MAPS_BLACKLIST_SLOT_STATE_DISABLED = 'disabled'
    MAPS_BLACKLIST_SLOT_STATE_COOLDOWN = 'cooldown'
    MAPS_BLACKLIST_SLOT_STATE_SELECTED = 'selected'
    MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER = 'active_no_hover'


class SlotTypeEnum(Enum):
    NONE = 'none'
    PREMIUM = 'premium'
    WOTPLUS = 'wotplus'


class MapsBlacklistSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(MapsBlacklistSlotModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return MapStateEnum(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def getMapId(self):
        return self._getString(1)

    def setMapId(self, value):
        self._setString(1, value)

    def getSeasonId(self):
        return self._getNumber(2)

    def setSeasonId(self, value):
        self._setNumber(2, value)

    def getCooldownTime(self):
        return self._getNumber(3)

    def setCooldownTime(self, value):
        self._setNumber(3, value)

    def getFiltered(self):
        return self._getBool(4)

    def setFiltered(self, value):
        self._setBool(4, value)

    def getSlotType(self):
        return SlotTypeEnum(self._getString(5))

    def setSlotType(self, value):
        self._setString(5, value.value)

    def _initialize(self):
        super(MapsBlacklistSlotModel, self)._initialize()
        self._addStringProperty('state')
        self._addStringProperty('mapId', '')
        self._addNumberProperty('seasonId', 0)
        self._addNumberProperty('cooldownTime', 0)
        self._addBoolProperty('filtered', True)
        self._addStringProperty('slotType', SlotTypeEnum.NONE.value)
