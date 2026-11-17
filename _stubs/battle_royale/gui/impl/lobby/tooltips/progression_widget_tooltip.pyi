# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/progression_widget_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo as setEventInfo
from battle_royale.gui.impl.gen.view_models.views.lobby.views.widget.progression_model import ProgressionModel as ProgressionModel, ProgressionStatus as ProgressionStatus
from battle_royale.gui.shared.tooltips.helper import fillProgressionPointsTableModel as fillProgressionPointsTableModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class ProgressionWidgetTooltipView(ViewImpl):
    __battleRoyale: Any
    __brProgression: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
