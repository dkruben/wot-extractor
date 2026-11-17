# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/vehicle_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewSettings as ViewSettings
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.shared.tooltips import advanced as advanced, contexts as contexts, vehicle as vehicle, vehicle_roles as vehicle_roles, ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips.builders import DataBuilder as DataBuilder, DefaultFormatBuilder as DefaultFormatBuilder, AdvancedDataBuilder as AdvancedDataBuilder, TooltipWindowBuilder as TooltipWindowBuilder, AdvancedTooltipWindowBuilder as AdvancedTooltipWindowBuilder
__all__: tuple

class InventoryVehicleBuilder(DataBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, linkage):
        ...
    def _buildData(self, _advanced, intCD, *args, **kwargs):
        ...

class VehicleCompensationBuilder(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, data, *args, **kwargs):
        ...

def getTooltipBuilders():
    ...
