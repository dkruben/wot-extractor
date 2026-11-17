# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/vehicle_items_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.tooltips import contexts as contexts, TOOLTIP_COMPONENT as TOOLTIP_COMPONENT
from gui.shared.tooltips import module as module
from gui.shared.tooltips import shell as shell, advanced as advanced
from gui.shared.tooltips.builders import DataBuilder as DataBuilder, AdvancedDataBuilder as AdvancedDataBuilder, AdvancedComplexBuilder as AdvancedComplexBuilder
__all__: tuple

class InventoryModuleBuilder(AdvancedDataBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, linkage):
        ...
    def _buildData(self, _advanced, intCD, *args, **kwargs):
        ...

class ShopModuleBuilder(AdvancedDataBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, linkage):
        ...
    def _buildData(self, _advanced, intCD, *args, **kwargs):
        ...

class TechTreeModuleBuilder(AdvancedDataBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, linkage):
        ...
    def _buildData(self, _advanced, node, parentCD, *args, **kwargs):
        ...

class ModuleDataBuilder(AdvancedDataBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, linkage):
        ...
    def _buildData(self, _advanced, intCD, buyPrice=None, inventoryCount=0, vehicleCount=0, slotIdx=0, eqs=None, *args):
        ...

class ShellBuilder(DataBuilder):
    __slots__: tuple
    def _buildData(self, _advanced, intCD, *args, **kwargs):
        ...

class AdvancedShellBuilder(AdvancedDataBuilder):
    __slots__: tuple
    def _buildData(self, _advanced, intCD, *args, **kwargs):
        ...

def _advancedBlockCondition(context):
    ...
def _shellAdvancedBlockCondition(context):
    ...
def _nationChangeShellAdvancedBlockCondition(context):
    ...
def _armorInspectorShellAdvancedBlockCondition(context):
    ...
def getTooltipBuilders():
    ...
