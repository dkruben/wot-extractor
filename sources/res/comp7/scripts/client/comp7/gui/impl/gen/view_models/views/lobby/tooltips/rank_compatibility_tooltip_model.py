# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/rank_compatibility_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/rank_compatibility_tooltip_model.py
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from frameworks.wulf import ViewModel

class RankCompatibilityTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RankCompatibilityTooltipModel, self).__init__(properties=properties, commands=commands)

    def getSeasonName(self):
        return SeasonName(self._getString(0))

    def setSeasonName(self, value):
        self._setString(0, value.value)

    def getSquadSize(self):
        return self._getNumber(1)

    def setSquadSize(self, value):
        self._setNumber(1, value)

    def getRankRangeRestriction(self):
        return self._getNumber(2)

    def setRankRangeRestriction(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(RankCompatibilityTooltipModel, self)._initialize()
        self._addStringProperty('seasonName')
        self._addNumberProperty('squadSize', 0)
        self._addNumberProperty('rankRangeRestriction', 0)
