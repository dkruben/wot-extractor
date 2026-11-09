# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/pet_system/fullscreen_event_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/pet_system/fullscreen_event_view.py
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.pet_system.fullscreen_event_view_model import FullscreenEventViewModel
from gui.impl.lobby.pet_system.event_view import PetEvent
from gui.impl.pub import WindowImpl
from frameworks.wulf import WindowFlags

class FullscreenEventView(PetEvent):
    LAYOUT_ID = R.views.mono.pet_system.fullscreen_event_view()

    def __init__(self, ctx):
        super(FullscreenEventView, self).__init__(FullscreenEventViewModel, ctx)

    @property
    def viewModel(self):
        return super(FullscreenEventView, self).getViewModel()

    def _updateData(self):
        with self.getViewModel().transaction() as tx:
            eventID = self._ctx.get('eventID')
            tx.setEventId(eventID)
            self._updateRewards()

    def _getEvents(self):
        events = super(FullscreenEventView, self)._getEvents()
        return events + (
         (
          self.viewModel.onClose, self._onClose),)


class FullscreenEventViewWindow(WindowImpl):

    def __init__(self, layer, **kwargs):
        super(FullscreenEventViewWindow, self).__init__(content=FullscreenEventView(**kwargs), wndFlags=WindowFlags.WINDOW_FULLSCREEN, layer=layer)
