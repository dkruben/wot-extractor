# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_matters/popovers/battle_matters_filter_popover_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import iteritems as iteritems
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.battle_matters.popovers.battle_matters_filter_popover_view_model import BattleMattersFilterPopoverViewModel as BattleMattersFilterPopoverViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.popovers.filter_control_view_model import FilterControlViewModel as FilterControlViewModel
from gui.impl.pub.view_impl import PopOverViewImpl as PopOverViewImpl
from gui.impl.gen import R as R

class BattleMattersFilterPopoverView(PopOverViewImpl):
    __slots__: tuple
    __filters: Any
    __updateCallback: Any
    def __init__(self, filtersDict=None, updateCallback=None):
        ...
    @property
    def viewModel(self):
        ...
    def onToggleFilter(self, event):
        ...
    def updateFilterFromOutside(self, changes):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _update(self):
        ...
    def _getEvents(self):
        ...
    def _changeVMValue(self, vm, valuesDict, valueName):
        ...
    def _updateFilter(self, changes):
        ...
