# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/tooltips/editing_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.achievements.tooltips.editing_tooltip_view_model import EditingTooltipViewModel as EditingTooltipViewModel, TooltipType as TooltipType
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class EditingTooltip(ViewImpl):
    __lobbyContext: Any
    __tooltipType: Any
    def __init__(self, tooltipType):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __getTooltipType(self):
        ...
