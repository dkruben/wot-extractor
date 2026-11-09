# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_coin_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_pass/tooltips/battle_pass_coin_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view_model import BattlePassCoinTooltipViewModel
from gui.impl.pub import ViewImpl

class BattlePassCoinTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.mono.battle_pass.tooltips.bpcoin())
        settings.model = BattlePassCoinTooltipViewModel()
        super(BattlePassCoinTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(BattlePassCoinTooltipView, self).getViewModel()
