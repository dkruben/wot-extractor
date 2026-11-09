# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/tooltips/compensation_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_model import LootBoxCompensationTooltipModel as LootBoxCompensationTooltipModel
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl

class CompensationTooltipContent(ViewImpl):
    __slots__: tuple
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...

class CrewSkinsCompensationTooltipContent(CompensationTooltipContent):
    __slots__: tuple
    def _initialize(self, *args, **kwargs):
        ...

class VehicleCompensationTooltipContent(CompensationTooltipContent):
    __slots__: tuple
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
