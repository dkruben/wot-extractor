# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/missions_tab_bar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from frameworks.wulf import ViewFlags as ViewFlags
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.impl.gen import R as R
from gui.impl.gen.view_models.ui_kit.side_bar_tab_model import SideBarTabModel as SideBarTabModel
from gui.impl.gen.view_models.views.missions.missions_tab_bar_view_model import MissionsTabBarViewModel as MissionsTabBarViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers.i18n import makeString as _ms
_logger: Any

class MissionsTabBarComponent(InjectComponentAdaptor):
    def setTabs(self, tabs):
        ...
    def setOnTabSelectionChangedCallback(self, callback):
        ...
    def _makeInjectView(self):
        ...

class MissionsTabBarView(ViewImpl):
    __slots__: tuple
    __tabsData: Any
    __onTabSelectionChangedCallback: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def setTabs(self, tabs):
        ...
    def setOnTabSelectionChangedCallback(self, callback):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def __onTabSelectionChanged(self, args=None):
        ...
