# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/mission_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from debug_utils import LOG_ERROR as LOG_ERROR
from frameworks.wulf.view.view import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from story_mode.gui.impl.gen.view_models.views.lobby.mission_selection_tooltip_model import MissionSelectionTooltipModel as MissionSelectionTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import Vehicle as Vehicle

class MissionTooltip(ViewImpl):
    _vehicle: Any
    def __init__(self, vehicle):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
