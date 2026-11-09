# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/integrated_auction/tooltips/auction_event_banner_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/integrated_auction/tooltips/auction_event_banner_tooltip_model.py
from frameworks.wulf import ViewModel

class AuctionEventBannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(AuctionEventBannerTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsAvailable(self):
        return self._getBool(0)

    def setIsAvailable(self, value):
        self._setBool(0, value)

    def getTimerValue(self):
        return self._getNumber(1)

    def setTimerValue(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(AuctionEventBannerTooltipModel, self)._initialize()
        self._addBoolProperty('isAvailable', False)
        self._addNumberProperty('timerValue', 0)
