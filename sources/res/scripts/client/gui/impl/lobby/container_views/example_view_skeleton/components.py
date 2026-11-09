# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/container_views/example_view_skeleton/components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/container_views/example_view_skeleton/components.py
import typing
from gui.impl.lobby.container_views.base.components import ComponentBase
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Tuple
    from frameworks.wulf import ViewModel, ViewStatus
    from frameworks.wulf.gui_constants import ShowingStatus

class ExampleComponent(ComponentBase):

    def _getViewModel(self, vm):
        return vm.exampleComponent

    def _getEvents(self):
        return super(ExampleComponent, self)._getEvents() + (
         (
          self.viewModel.onMouseEnter, self._onMouseEnter),
         (
          self.viewModel.onMouseLeave, self._onMouseLeave))

    def _fillViewModel(self, vm):
        pass

    def _onLoading(self, *args, **kwargs):
        pass

    def _onLoaded(self, *args, **kwargs):
        pass

    def _initialize(self, *args, **kwargs):
        pass

    def _finalize(self):
        pass

    def _onReady(self):
        pass

    def _onShown(self):
        pass

    def _onHidden(self):
        pass

    def _onFocus(self, focused):
        pass

    def _swapStates(self, oldStatus, newStatus):
        pass

    def _swapShowingStates(self, oldStatus, newStatus):
        pass

    def _subscribe(self):
        pass

    def _unsubscribe(self):
        pass

    def _onMouseEnter(self):
        self.events.onMouseEnter(self)

    def _onMouseLeave(self):
        self.events.onMouseLeave(self)
