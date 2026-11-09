# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/prestige/prestige_level_grades_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel as PrestigeEmblemModel
from gui.impl.gen.view_models.views.lobby.prestige.tooltips.elite_level_grades_tooltip_model import EliteLevelGradesTooltipModel as EliteLevelGradesTooltipModel
from gui.prestige.prestige_helpers import getVehiclePrestige as getVehiclePrestige, fillPrestigeEmblemModel as fillPrestigeEmblemModel, getSortedGrades as getSortedGrades
from gui.impl.pub import ViewImpl as ViewImpl

class PrestigeLevelGradesTooltipView(ViewImpl):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, vehIntCD, *args, **kwargs):
        ...
