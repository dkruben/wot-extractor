# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/shop_button_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/shop_button_tooltip_view.py
from __future__ import absolute_import
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.shop_button_tooltip_view_model import ShopButtonTooltipViewModel
from frameworks.wulf import ViewFlags, ViewSettings
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class ShopButtonTooltipView(ViewImpl):

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.battle_royale.mono.lobby.tooltips.shop_button())
        settings.flags = ViewFlags.VIEW
        settings.model = ShopButtonTooltipViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(ShopButtonTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ShopButtonTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ShopButtonTooltipView, self)._onLoading(args, kwargs)
        with self.viewModel.transaction() as tx:
            setEventInfo(tx.eventInfo)
