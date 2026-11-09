# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/conversion_confirm_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/conversion_confirm_view.py
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.conversion_confirm_view_model import ConversionConfirmViewModel
from gui.impl.lobby.crew.base_crew_view import BaseCrewSubView
from gui.impl.lobby.crew.filter.data_providers import JunkTankmenDataProvider
from gui.impl.lobby.crew.tooltips.conversion_tooltip import ConversionTooltip
from gui.impl.pub import WindowImpl
from gui.shared.event_dispatcher import showJunkTankmen
from gui.shared.gui_items.items_actions import factory
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from PlayerEvents import g_playerEvents

class ConversionConfirmView(BaseCrewSubView):
    itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = ('__dataProvider', '__tooltipData')

    def __init__(self, layoutID=R.views.lobby.crew.ConversionConfirmView(), *args, **kwargs):
        super(ConversionConfirmView, self).__init__(ViewSettings(layoutID, flags=ViewFlags.VIEW, model=ConversionConfirmViewModel(), args=args, kwargs=kwargs))
        self.__dataProvider = JunkTankmenDataProvider()
        self.__tooltipData = {}

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.crew.tooltips.ConversionTooltip():
            tooltipId = event.getArgument('tooltipId')
            books = self.__tooltipData.get(tooltipId, [])
            return ConversionTooltip(books, title=R.strings.tooltips.conversion.notReceived.header(), description=R.strings.tooltips.conversion.notReceived.body())
        return super(ConversionConfirmView, self).createToolTipContent(event, contentID)

    @property
    def viewModel(self):
        return super(ConversionConfirmView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ConversionConfirmView, self)._onLoading(*args, **kwargs)
        self.__dataProvider.update()

    def _getEvents(self):
        return (
         (
          self.viewModel.onCancel, self._onCancel),
         (
          self.viewModel.onClose, self._onClose),
         (
          self.viewModel.onConfirm, self._onConfirm),
         (
          self.viewModel.onShowTankman, self._onShowTankman),
         (
          self.__dataProvider.onDataChanged, self.__onUpdate),
         (
          g_playerEvents.onDisconnected, self.__onDisconnected))

    def __onDisconnected(self):
        self.destroyWindow()

    def _onCancel(self):
        self.destroyWindow()

    def _onClose(self):
        self.destroyWindow()

    def _onShowTankman(self):
        showJunkTankmen()

    def _onConfirm(self):
        factory.doAction(factory.CONVERT_JUNK_TANKMEN)
        self.destroyWindow()

    def __onUpdate(self):
        items = self.__dataProvider.items()
        with self.viewModel.transaction() as tx:
            rewards = tx.getRewards()
            rewards.clear()
            tx.setTankmanAmount(len(items))


class ConversionConfirmWindow(WindowImpl):

    def __init__(self):
        super(ConversionConfirmWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, layer=WindowLayer.TOP_WINDOW, content=ConversionConfirmView())
