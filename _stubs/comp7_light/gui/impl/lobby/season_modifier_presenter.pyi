# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/season_modifier_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7_light.gui.impl.gen.view_models.views.lobby.season_modifier_model import SeasonModifierModel as SeasonModifierModel
from comp7_light.gui.impl.lobby.tooltips.comp7_light_modifiers_domain_tooltip_view import Comp7LightModifiersDomainTooltipView as Comp7LightModifiersDomainTooltipView, COMP7_LIGHT_SEASON_MODIFIERS_DOMAIN as COMP7_LIGHT_SEASON_MODIFIERS_DOMAIN
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from gui.impl.gen import R as R
from skeletons.gui.game_control import IComp7LightController as IComp7LightController

# base nao representavel no stub: ViewComponent[...]
class SeasonModifierPresenter:
    __comp7LightController: Any
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
