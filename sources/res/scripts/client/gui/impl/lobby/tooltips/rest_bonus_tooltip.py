# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tooltips/rest_bonus_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tooltips/rest_bonus_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tooltips.rest_bonus_tooltip_model import RestBonusTooltipModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from helpers import time_utils
from skeletons.gui.game_control import IRestBonusController
from skeletons.gui.shared import IItemsCache

class RestBonusTooltip(ViewImpl):
    __restBonusController = dependency.descriptor(IRestBonusController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.rest_bonus.tooltips.rest_bonus_tooltip())
        settings.model = RestBonusTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(RestBonusTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(RestBonusTooltip, self).getViewModel()

    def _onLoading(self, intCD, *args, **kwargs):
        super(RestBonusTooltip, self)._onLoading(*args, **kwargs)
        vehicle = self.__itemsCache.items.getItemByCD(intCD)
        with self.viewModel.transaction() as model:
            model.setMultiplier(self.__restBonusController.getActualXPFactor(vehicle))
            model.setResetTimestamp(time_utils.getTimestampFromUTC(time_utils.getTimeStructInLocal(self.__restBonusController.getDailyResetTime())))
            model.setEndTimestamp(self.__restBonusController.getRestBonusExpiryTime())
