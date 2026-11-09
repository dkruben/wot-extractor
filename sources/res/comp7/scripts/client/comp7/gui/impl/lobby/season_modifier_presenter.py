# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/season_modifier_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/season_modifier_presenter.py
from __future__ import absolute_import
from comp7.gui.impl.gen.view_models.views.lobby.season_modifier_model import SeasonModifierModel
from comp7_core.gui.impl.lobby.tooltips.comp7_core_modifiers_tooltip_view import Comp7CoreModifiersTooltipView
from gui.impl.pub.view_component import ViewComponent
from helpers import dependency
from gui.impl.gen import R
from skeletons.gui.game_control import IComp7Controller
from comp7.constants import COMP7_SEASON_MODIFIERS_DOMAIN

class SeasonModifierPresenter(ViewComponent[SeasonModifierModel]):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self):
        super(SeasonModifierPresenter, self).__init__(model=SeasonModifierModel)

    def _onLoading(self, *args, **kwargs):
        super(SeasonModifierPresenter, self)._onLoading(*args, **kwargs)
        self.__updateData()

    @property
    def viewModel(self):
        return super(SeasonModifierPresenter, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.battle_modifiers.lobby.tooltips.ModifiersDomainTooltipView():
            return Comp7CoreModifiersTooltipView(COMP7_SEASON_MODIFIERS_DOMAIN)
        return super(SeasonModifierPresenter, self).createToolTipContent(event, contentID)

    def _getEvents(self):
        return (
         (
          self.__comp7Controller.onBanUpdated, self.__updateData),
         (
          self.__comp7Controller.onQualificationStateUpdated, self.__updateData),
         (
          self.__comp7Controller.onStatusUpdated, self.__updateData),
         (
          self.__comp7Controller.onModeConfigChanged, self.__updateData))

    def __updateData(self, _=None):
        self.viewModel.setEnabled(self.__comp7Controller.isBattleModifiersAvailable())
