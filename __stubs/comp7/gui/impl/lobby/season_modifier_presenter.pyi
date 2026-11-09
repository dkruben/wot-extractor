# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/season_modifier_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.gen.view_models.views.lobby.season_modifier_model import SeasonModifierModel as SeasonModifierModel
from comp7_core.gui.impl.lobby.tooltips.comp7_core_modifiers_tooltip_view import Comp7CoreModifiersTooltipView as Comp7CoreModifiersTooltipView
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from gui.impl.gen import R as R
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7.constants import COMP7_SEASON_MODIFIERS_DOMAIN as COMP7_SEASON_MODIFIERS_DOMAIN

# base nao representavel no stub: ViewComponent[...]
class SeasonModifierPresenter:
    __comp7Controller: Any
    def __init__(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def __updateData(self, _=None):
        ...
