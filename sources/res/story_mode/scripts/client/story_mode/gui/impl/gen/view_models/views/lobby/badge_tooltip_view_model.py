# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/badge_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/badge_tooltip_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BadgeTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BadgeTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getImage(self):
        return self._getResource(1)

    def setImage(self, value):
        self._setResource(1, value)

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)

    def getPlayerName(self):
        return self._getString(3)

    def setPlayerName(self, value):
        self._setString(3, value)

    def getVehicleIcon(self):
        return self._getString(4)

    def setVehicleIcon(self, value):
        self._setString(4, value)

    def getVehicleLevel(self):
        return self._getString(5)

    def setVehicleLevel(self, value):
        self._setString(5, value)

    def getSmallBadgeIcon(self):
        return self._getResource(6)

    def setSmallBadgeIcon(self, value):
        self._setResource(6, value)

    def _initialize(self):
        super(BadgeTooltipViewModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addResourceProperty('image', R.invalid())
        self._addStringProperty('description', '')
        self._addStringProperty('playerName', '')
        self._addStringProperty('vehicleIcon', '')
        self._addStringProperty('vehicleLevel', '')
        self._addResourceProperty('smallBadgeIcon', R.invalid())
