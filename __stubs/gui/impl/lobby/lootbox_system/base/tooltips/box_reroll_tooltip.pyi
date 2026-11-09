# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/box_reroll_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.tooltips.box_reroll_tooltip_model import BoxRerollTooltipModel as BoxRerollTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController

class BoxRerollTooltip(ViewImpl):
    __lootBoxes: Any
    __boxCategory: Any
    __eventName: Any
    def __init__(self, boxCategory, eventName):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
