# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/tooltips/event.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getTypeBigIconPath as getTypeBigIconPath
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.vehicle import VehicleInfoTooltipData as VehicleInfoTooltipData, StatusBlockConstructor as StatusBlockConstructor, HeaderBlockConstructor as HeaderBlockConstructor, SimplifiedStatsBlockConstructor as SimplifiedStatsBlockConstructor, CommonStatsBlockConstructor as CommonStatsBlockConstructor
from gui.shared.tooltips.module import ModuleBlockTooltipData as ModuleBlockTooltipData, EffectsBlockConstructor as EffectsBlockConstructor, InventoryBlockConstructor as InventoryBlockConstructor, HeaderBlockConstructor as ModuleHeaderBlockConstructor
from gui.shared.tooltips.shell import ShellBlockToolTipData as ShellBlockToolTipData
from LSAccountEquipmentController import getLSConsumables as getLSConsumables

class EventVehicleInfoTooltipData(VehicleInfoTooltipData, IGlobalListener):
    item: Any
    def _getCrewIconBlock(self):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class EventHeaderBlockConstructor(HeaderBlockConstructor):
    def construct(self):
        ...

class EventModuleBlockTooltipData(ModuleBlockTooltipData):
    def _getHeaderBlockConstructor(self):
        ...
    def _getEffectsBlockConstructor(self):
        ...
    def _getInventoryBlockConstructor(self):
        ...

class EventModuleHeaderBlockConstructor(ModuleHeaderBlockConstructor):
    def _getCooldownSeconds(self):
        ...

class EventEffectsBlockConstructor(EffectsBlockConstructor):
    def _getOnUseStr(self, attribs, isRemovingStun, **kpiArgs):
        ...

class EventInventoryBlockConstructor(InventoryBlockConstructor):
    def _getInstalledVehicles(self, module, inventoryVehicles):
        ...

class EventShellBlockToolTipData(ShellBlockToolTipData):
    ...

class EventVehicleInfoTooltipDataDef(VehicleInfoTooltipData, IGlobalListener):
    item: Any
    def _packBlocks(self, *args, **kwargs):
        ...
