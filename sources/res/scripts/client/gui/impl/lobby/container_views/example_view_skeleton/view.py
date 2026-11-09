# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/container_views/example_view_skeleton/view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/container_views/example_view_skeleton/view.py
import typing
from frameworks.wulf import ViewModel
from gui.impl.lobby.container_views.base.components import ContainerBase
from gui.impl.lobby.container_views.base.controllers import InteractionController
from gui.impl.lobby.container_views.example_view_skeleton.components import ExampleComponent
from gui.impl.lobby.container_views.example_view_skeleton.context import ExampleViewContext
from gui.impl.lobby.container_views.example_view_skeleton.controller import ExampleInteractionController
from gui.impl.pub import ViewImpl
if typing.TYPE_CHECKING:
    from typing import Any, List, Type
    from gui.impl.lobby.container_views.base.components import ComponentBase

class ExampleContainerView(ContainerBase, ViewImpl):

    def __init__(self, layoutID, *args, **kwargs):
        self.__layoutID = layoutID
        super(ExampleContainerView, self).__init__(*args, **kwargs)

    def _getComponents(self):
        return [
         ExampleComponent(key='someKey', parent=self)]

    def _getContext(self, *args, **kwargs):
        return ExampleViewContext(kwargs.get('tankmanID'))

    def _getInteractionControllerCls(self):
        return ExampleInteractionController

    def _fillViewModel(self, vm):
        pass
