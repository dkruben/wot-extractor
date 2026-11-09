# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/day_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/day_tooltip_model.py
from comp7.gui.impl.gen.view_models.views.lobby.enums import Division, Rank, SeasonName
from frameworks.wulf import ViewModel

class DayTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(DayTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIndex(self):
        return self._getNumber(0)

    def setIndex(self, value):
        self._setNumber(0, value)

    def getIsQualification(self):
        return self._getBool(1)

    def setIsQualification(self, value):
        self._setBool(1, value)

    def getSeasonName(self):
        return SeasonName(self._getString(2))

    def setSeasonName(self, value):
        self._setString(2, value.value)

    def getDiff(self):
        return self._getNumber(3)

    def setDiff(self, value):
        self._setNumber(3, value)

    def getRank(self):
        return Rank(self._getNumber(4))

    def setRank(self, value):
        self._setNumber(4, value.value)

    def getDivision(self):
        return Division(self._getNumber(5))

    def setDivision(self, value):
        self._setNumber(5, value.value)

    def getHasBattles(self):
        return self._getBool(6)

    def setHasBattles(self, value):
        self._setBool(6, value)

    def getRatingPoints(self):
        return self._getNumber(7)

    def setRatingPoints(self, value):
        self._setNumber(7, value)

    def getRankInactivityPenalty(self):
        return self._getNumber(8)

    def setRankInactivityPenalty(self, value):
        self._setNumber(8, value)

    def getCurrentDayIndex(self):
        return self._getNumber(9)

    def setCurrentDayIndex(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(DayTooltipModel, self)._initialize()
        self._addNumberProperty('index', 0)
        self._addBoolProperty('isQualification', False)
        self._addStringProperty('seasonName')
        self._addNumberProperty('diff', 0)
        self._addNumberProperty('rank')
        self._addNumberProperty('division')
        self._addBoolProperty('hasBattles', False)
        self._addNumberProperty('ratingPoints', 0)
        self._addNumberProperty('rankInactivityPenalty', 0)
        self._addNumberProperty('currentDayIndex', 0)
