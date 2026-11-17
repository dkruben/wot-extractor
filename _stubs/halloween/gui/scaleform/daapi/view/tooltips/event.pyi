# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/tooltips/event.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import FORCE_FINITE_SHELL_TAG as FORCE_FINITE_SHELL_TAG
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES as BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui import makeHtmlString as makeHtmlString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getTypeBigIconPath as getTypeBigIconPath
from gui.shared.items_parameters import params_helper as params_helper
from gui.shared.tooltips import formatters as formatters
from gui.shared.tooltips.vehicle import VehicleInfoTooltipData as VehicleInfoTooltipData, StatusBlockConstructor as StatusBlockConstructor, HeaderBlockConstructor as HeaderBlockConstructor, SimplifiedStatsBlockConstructor as SimplifiedStatsBlockConstructor
from gui.shared.tooltips.module import ModuleBlockTooltipData as ModuleBlockTooltipData, EffectsBlockConstructor as EffectsBlockConstructor, HeaderBlockConstructor as ModuleHeaderBlockConstructor
from gui.shared.tooltips.shell import ShellBlockToolTipData as ShellBlockToolTipData, CommonStatsBlockConstructor as CommonStatsBlockConstructor
from halloween.gui.scaleform.genConsts.HALLOWEEN_ICON_TEXT_FRAMES import HALLOWEEN_ICON_TEXT_FRAMES as HALLOWEEN_ICON_TEXT_FRAMES
from halloween.gui.scaleform.genConsts.HALLOWEEN_BLOCKS_TOOLTIP_TYPES import HALLOWEEN_BLOCKS_TOOLTIP_TYPES as HALLOWEEN_BLOCKS_TOOLTIP_TYPES
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import VehicleStates as VehicleStates
from halloween.gui.impl.lobby.hw_helpers import isDailyKeyQuestCompleted as isDailyKeyQuestCompleted, getVehicleState as getVehicleState
from gui.shared.tooltips.shell import HeaderBlockConstructor as ShellHeaderBlockConstructor
_TOOLTIP_MIN_WIDTH = 380

class EventVehicleInfoTooltipData(VehicleInfoTooltipData, IGlobalListener):
    item: Any
    def _getCrewIconBlock(self):
        ...
    def _packBlocks(self, *args, **kwargs):
        ...

class EventStatusBlockConstructor(StatusBlockConstructor):
    def construct(self):
        ...

class EventHeaderBlockConstructor(HeaderBlockConstructor):
    def construct(self):
        ...

class EventModuleBlockTooltipData(ModuleBlockTooltipData):
    def _getHeaderBlockConstructor(self):
        ...
    def _getEffectsBlockConstructor(self):
        ...

class EventModuleHeaderBlockConstructor(ModuleHeaderBlockConstructor):
    def _getCooldownSeconds(self):
        ...

class EventEffectsBlockConstructor(EffectsBlockConstructor):
    def _getOnUseStr(self, attribs, isRemovingStun, **kpiArgs):
        ...

class EventShellBlockToolTipData(ShellBlockToolTipData):
    item: Any
    def _packBlocks(self, *args, **kwargs):
        ...
