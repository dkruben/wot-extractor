# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/service_record/controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/service_record/controller.py
import typing
from Event import Event
from gui.impl.lobby.crew.container_vews.common.base_personal_case_controller import BasePersonalCaseController
from gui.impl.lobby.crew.container_vews.common.base_personal_case_events import BasePersonalCaseComponentViewEvents
from gui.shared.items_cache import CACHE_SYNC_REASON
if typing.TYPE_CHECKING:
    from typing import Callable, List, Tuple
    from gui.impl.lobby.container_views.base.events import ComponentEventsBase

class ServiceRecordInteractionController(BasePersonalCaseController):

    def _getEventsProvider(self):
        return BasePersonalCaseComponentViewEvents()

    def _getEvents(self):
        return super(ServiceRecordInteractionController, self)._getEvents() + [
         (
          self.itemsCache.onSyncCompleted, self._onCacheResync)]

    def _onCacheResync(self, reason, _):
        if reason in (CACHE_SYNC_REASON.STATS_RESYNC, CACHE_SYNC_REASON.SHOW_GUI):
            return
        else:
            tankman = self.itemsCache.items.getTankman(self.view.context.tankman.invID)
            if tankman is None:
                return
            self.onChangeTankman(tankman.invID)
            return

    def onChangeTankman(self, tankmanID):
        self.context.update(tankmanID)
        self.refresh()
