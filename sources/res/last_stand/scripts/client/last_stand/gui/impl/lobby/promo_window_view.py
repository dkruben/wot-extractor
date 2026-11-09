# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/promo_window_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/promo_window_view.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from frameworks.wulf import ViewSettings, WindowFlags, ViewFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from last_stand.gui.impl.gen.view_models.views.lobby.promo_window_view_model import PromoWindowViewModel
from last_stand.gui.impl.lobby.base_view import BaseView
from last_stand.gui.ls_account_settings import AccountSettingsKeys
from helpers import dependency
from last_stand.skeletons.ls_artefacts_controller import ILSArtefactsController
from last_stand.skeletons.ls_controller import ILSController

class PromoWindowView(BaseView):
    lsArtifactsCtrl = dependency.descriptor(ILSArtefactsController)
    __lsCtrl = dependency.descriptor(ILSController)
    __slots__ = ()
    layoutID = R.views.last_stand.mono.lobby.promo_view()

    def __init__(self, layoutID=None):
        settings = ViewSettings(layoutID or self.layoutID, ViewFlags.VIEW, PromoWindowViewModel())
        super(PromoWindowView, self).__init__(settings)

    @property
    def isHiddenMenu(self):
        return self.lsCtrl.isEventPrb()

    @property
    def viewModel(self):
        return super(PromoWindowView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(PromoWindowView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            model.setStartDate(self.__lsCtrl.getModeSettings().startDate)
            model.setEndDate(self.__lsCtrl.getModeSettings().endDate)
            model.setRegularArtefactsLength(self.lsArtifactsCtrl.getArtefactsCount())

    def _subscribe(self):
        super(PromoWindowView, self)._subscribe()
        self.viewModel.onClose += self._onClose

    def _unsubscribe(self):
        super(PromoWindowView, self)._unsubscribe()
        self.viewModel.onClose -= self._onClose

    def _onClose(self):
        settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)
        settings[AccountSettingsKeys.PROMO_SCREEN_SHOWED] = True
        AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)
        self.destroyWindow()


class PromoWindow(LobbyNotificationWindow):

    def __init__(self, layoutID, parent=None):
        super(PromoWindow, self).__init__(wndFlags=WindowFlags.WINDOW_FULLSCREEN | WindowFlags.WINDOW, content=PromoWindowView(layoutID=layoutID), parent=parent, layer=WindowLayer.TOP_WINDOW)
