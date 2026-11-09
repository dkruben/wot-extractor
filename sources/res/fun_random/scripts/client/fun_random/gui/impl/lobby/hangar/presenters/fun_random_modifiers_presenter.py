# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_modifiers_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_modifiers_presenter.py
from __future__ import absolute_import
from battle_modifiers.gui.impl.lobby.hangar.presenters.modifiers_presenter import ModifiersPresenter
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from fun_random.gui.impl.lobby.tooltips.fun_random_domain_tooltip_view import FunRandomDomainTooltipView
from gui.impl.gen import R

class FunRandomModifiersPresenter(ModifiersPresenter, FunSubModesWatcher):

    @hasDesiredSubMode()
    def getModifiersDataProvider(self):
        return self.getDesiredSubMode().getModifiersDataProvider()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.battle_modifiers.lobby.tooltips.ModifiersDomainTooltipView():
            modifiersDomain = event.getArgument('modifiersDomain')
            return FunRandomDomainTooltipView(modifiersDomain)
        return super(FunRandomModifiersPresenter, self).createToolTipContent(event, contentID)

    def _onLoading(self, *args, **kwargs):
        super(FunRandomModifiersPresenter, self)._onLoading(*args, **kwargs)
        self.startSubSettingsListening(self._updateData, desiredOnly=True)
        self.startSubSelectionListening(self._updateData)

    def _finalize(self):
        self.stopSubSelectionListening(self._updateData)
        self.stopSubSettingsListening(self._updateData, desiredOnly=True)
        super(FunRandomModifiersPresenter, self)._finalize()

    def _updateData(self, *_):
        super(FunRandomModifiersPresenter, self)._updateData()
