# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tooltips/rest_bonus_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tooltips.rest_bonus_tooltip_model import RestBonusTooltipModel as RestBonusTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from skeletons.gui.game_control import IRestBonusController as IRestBonusController
from skeletons.gui.shared import IItemsCache as IItemsCache

class RestBonusTooltip(ViewImpl):
    __restBonusController: Any
    __itemsCache: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, intCD, *args, **kwargs):
        ...
