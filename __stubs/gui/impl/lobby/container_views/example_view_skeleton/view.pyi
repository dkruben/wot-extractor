# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/container_views/example_view_skeleton/view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.lobby.container_views.base.components import ContainerBase as ContainerBase
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.container_views.example_view_skeleton.components import ExampleComponent as ExampleComponent
from gui.impl.lobby.container_views.example_view_skeleton.context import ExampleViewContext as ExampleViewContext
from gui.impl.lobby.container_views.example_view_skeleton.controller import ExampleInteractionController as ExampleInteractionController
from gui.impl.pub import ViewImpl as ViewImpl
from typing import Any as Any, List as List, Type as Type
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase

class ExampleContainerView(ContainerBase, ViewImpl):
    __layoutID: _Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    def _getComponents(self):
        ...
    def _getContext(self, *args, **kwargs):
        ...
    def _getInteractionControllerCls(self):
        ...
    def _fillViewModel(self, vm):
        ...
