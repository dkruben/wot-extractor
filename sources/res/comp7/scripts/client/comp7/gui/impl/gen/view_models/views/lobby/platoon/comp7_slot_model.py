# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/platoon/comp7_slot_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/platoon/comp7_slot_model.py
from comp7.gui.impl.gen.view_models.views.lobby.platoon.platoon_rank_data import PlatoonRankData
from gui.impl.gen.view_models.views.lobby.platoon.slot_model import SlotModel

class Comp7SlotModel(SlotModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(Comp7SlotModel, self).__init__(properties=properties, commands=commands)

    @property
    def rankData(self):
        return self._getViewModel(12)

    @staticmethod
    def getRankDataType():
        return PlatoonRankData

    def getIsWaiting(self):
        return self._getBool(13)

    def setIsWaiting(self, value):
        self._setBool(13, value)

    def _initialize(self):
        super(Comp7SlotModel, self)._initialize()
        self._addViewModelProperty('rankData', PlatoonRankData())
        self._addBoolProperty('isWaiting', False)
