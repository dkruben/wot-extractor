# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/shop_button_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/shop_button_tooltip_view_model.py
from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel

class ShopButtonTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ShopButtonTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def eventInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getEventInfoType():
        return BattleRoyaleEventModel

    def _initialize(self):
        super(ShopButtonTooltipViewModel, self)._initialize()
        self._addViewModelProperty('eventInfo', BattleRoyaleEventModel())
