# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/entry_point_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/entry_point_tooltip.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.lootbox_system.tooltips.entry_point_tooltip_view_model import EntryPointTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from helpers.time_utils import getServerUTCTime
from skeletons.gui.game_control import ILootBoxSystemController

class EntryPointTooltip(ViewImpl):
    __slots__ = ('__eventName', )
    __lootBoxes = dependency.descriptor(ILootBoxSystemController)

    def __init__(self, eventName):
        settings = ViewSettings(R.views.mono.lootbox.tooltips.entry_point())
        settings.model = EntryPointTooltipViewModel()
        super(EntryPointTooltip, self).__init__(settings)
        self.__eventName = eventName

    @property
    def viewModel(self):
        return super(EntryPointTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(EntryPointTooltip, self)._onLoading(*args, **kwargs)
        self.__updateState()

    def _getEvents(self):
        return (
         (
          self.__lootBoxes.onStatusChanged, self.__onLootBoxesStatusChanged),)

    def __onLootBoxesStatusChanged(self):
        self.__updateState()

    def __updateState(self):
        with self.viewModel.transaction() as vmTx:
            vmTx.setEventName(self.__eventName)
            vmTx.setIsEnabled(self.__lootBoxes.isLootBoxesAvailable)
            vmTx.setEventExpireTime(self.__getEventExpireTime())

    def __getEventExpireTime(self):
        _, finish = self.__lootBoxes.getActiveTime(self.__eventName)
        return finish - getServerUTCTime()
