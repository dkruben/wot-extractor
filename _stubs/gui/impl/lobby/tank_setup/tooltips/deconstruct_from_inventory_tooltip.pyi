# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/tooltips/deconstruct_from_inventory_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.tank_setup.tooltips.deconstruct_from_inventory_tooltip_model import DeconstructFromInventoryTooltipModel as DeconstructFromInventoryTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R

class DeconstructFromInventoryTooltip(ViewImpl):
    __slots__: tuple
    equipmentName: Any
    equipmentAmount: Any
    def __init__(self, equipmentName, equipmentAmount, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
