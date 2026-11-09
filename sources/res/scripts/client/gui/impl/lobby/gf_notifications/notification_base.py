# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/gf_notifications/notification_base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/gf_notifications/notification_base.py
from gui.impl.pub import ViewImpl
from PlayerEvents import g_playerEvents
from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.lobby.gf_notifications.cache import getCache
from gui.prb_control.entities.base.listener import IPrbListener
from gui.shared import g_eventBus
from gui.shared.events import HidePopoverEvent

class NotificationBase(ViewImpl, IPrbListener):
    __slots__ = ('_isPopUp', '_linkageData')

    def __init__(self, resId, model, *args, **kwargs):
        settings = ViewSettings(resId)
        settings.model = model
        settings.flags = ViewFlags.VIEW
        self._isPopUp = args[0]
        self._linkageData = args[1]
        super(NotificationBase, self).__init__(settings)

    @property
    def linkageData(self):
        return self._linkageData

    def _onLoading(self, *args, **kwargs):
        super(NotificationBase, self)._onLoading(*args, **kwargs)
        self._update()

    def _update(self):
        raise NotImplementedError

    def _getEvents(self):
        events = super(NotificationBase, self)._getEvents()
        return events + (
         (
          g_playerEvents.onEnqueued, self.__updatePrebattleControls),
         (
          g_playerEvents.onDequeued, self.__updatePrebattleControls))

    def _finalize(self):
        self._isPopUp = None
        self._linkageData = None
        super(NotificationBase, self)._finalize()
        return

    def _getPayload(self):
        data = self._linkageData.toDict()
        return getCache().getPayload(data['gfDataID'])

    def _canNavigate(self):
        prbDispatcher = self.prbDispatcher
        if prbDispatcher is not None and prbDispatcher.getFunctionalState().isNavigationDisabled():
            return False
        else:
            return True

    def _closeNotificationCenter(self):
        if not self._isPopUp:
            g_eventBus.handleEvent(HidePopoverEvent(HidePopoverEvent.HIDE_POPOVER))

    def __updatePrebattleControls(self, *_):
        self._update()
