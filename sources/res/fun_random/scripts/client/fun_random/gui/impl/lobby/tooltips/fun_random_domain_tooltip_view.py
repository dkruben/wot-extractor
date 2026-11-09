# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_domain_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_domain_tooltip_view.py
from __future__ import absolute_import
from battle_modifiers.gui.impl.lobby.tooltips.modifiers_domain_tooltip_view import ModifiersDomainTooltipView
from fun_random.gui.feature.util.fun_mixins import FunSubModeHolder
from fun_random.gui.feature.util.fun_wrappers import hasHoldingSubMode

class FunRandomDomainTooltipView(ModifiersDomainTooltipView, FunSubModeHolder):

    @hasHoldingSubMode()
    def getModifiersDataProvider(self):
        return self.getHoldingSubMode().getModifiersDataProvider()

    def _onLoading(self, subModeID=None):
        self.catchSubMode(subModeID or self._funRandomCtrl.subModesHolder.getDesiredSubModeID())
        super(FunRandomDomainTooltipView, self)._onLoading()

    def _finalize(self):
        super(FunRandomDomainTooltipView, self)._finalize()
        self.releaseSubMode()
