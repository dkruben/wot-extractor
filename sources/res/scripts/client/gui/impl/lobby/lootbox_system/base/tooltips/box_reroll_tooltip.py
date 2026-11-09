# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/box_reroll_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/box_reroll_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from frameworks.wulf.view.array import fillIntsArray
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.lootbox_system.tooltips.box_reroll_tooltip_model import BoxRerollTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from shared_utils import first
from skeletons.gui.game_control import ILootBoxSystemController

class BoxRerollTooltip(ViewImpl):
    __lootBoxes = dependency.descriptor(ILootBoxSystemController)

    def __init__(self, boxCategory, eventName):
        settings = ViewSettings(R.views.mono.lootbox.tooltips.reroll())
        settings.model = BoxRerollTooltipModel()
        super(BoxRerollTooltip, self).__init__(settings)
        self.__boxCategory = boxCategory
        self.__eventName = eventName

    @property
    def viewModel(self):
        return super(BoxRerollTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(BoxRerollTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel as model:

            def isCompatibleBox(b):
                return b.getType() == self.__eventName and b.getCategory() == self.__boxCategory and b.isEnabled()

            box = first(self.__lootBoxes.getBoxes(self.__eventName, isCompatibleBox))
            model.setEventName(self.__eventName)
            currency = box.getRerollCurrency()
            model.setCurrency(currency)
            pricesArray = model.getPrices()
            fillIntsArray(box.getRerollPrices(), pricesArray)
            rerollAttempts = self.__lootBoxes.getBoxInfo(box.getID())['rerollAttempts']
            model.setRerollAttempts(rerollAttempts)
