# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/tooltips/tooltip_builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow as DecoratedTooltipWindow
from gui.shared.tooltips import contexts as contexts, advanced as advanced, ToolTipBaseData as ToolTipBaseData
from gui.shared.tooltips.builders import DataBuilder as DataBuilder, AdvancedDataBuilder as AdvancedDataBuilder, TooltipWindowBuilder as TooltipWindowBuilder
from halloween.gui.halloween_gui_constants import HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP as HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP, HALLOWEEN_ABILITY_TOOLTIP as HALLOWEEN_ABILITY_TOOLTIP, HALLOWEEN_MAIN_SHELL as HALLOWEEN_MAIN_SHELL, HALLOWEEN_VEHICLE_FEATURE_TOOLTIP as HALLOWEEN_VEHICLE_FEATURE_TOOLTIP
from halloween.gui.impl.lobby.tooltips.vehicle_tooltip import VehicleTooltipView as VehicleTooltipView
from halloween.gui.scaleform.daapi.view.tooltips import event as event
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.daapi.view.tooltips.vehicle_items_builders import AdvancedShellBuilder as AdvancedShellBuilder
from halloween.gui.shared.contexts import EventVehicleContext as EventVehicleContext
__all__: tuple

class VehicleTooltipContentWindowData(ToolTipBaseData):
    def __init__(self, context):
        ...
    def getDisplayableData(self, vehicleCD, isQuestVisible=True, isStatusVisible=True, *_, **kwargs):
        ...

def getTooltipBuilders():
    ...
