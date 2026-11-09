# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/tooltips/tooltip_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/tooltips/tooltip_builders.py
from __future__ import absolute_import
from gui.shared.tooltips import contexts, advanced
from gui.shared.tooltips.builders import DataBuilder, AdvancedDataBuilder
from last_stand.gui.ls_gui_constants import LS_RENT_VEHICLE_TOOLTIP, LS_ABILITY_TOOLTIP, LS_MAIN_SHELL, LS_CAROUSEL_VEHICLE_TOOLTIP
from last_stand.gui.scaleform.daapi.view.tooltips import event
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.daapi.view.tooltips.vehicle_items_builders import AdvancedShellBuilder
from last_stand.gui.shared.contexts import EventVehicleContext
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(LS_RENT_VEHICLE_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, event.EventVehicleInfoTooltipData(EventVehicleContext())),
     DataBuilder(LS_CAROUSEL_VEHICLE_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, event.EventVehicleInfoTooltipDataDef(EventVehicleContext())),
     AdvancedDataBuilder(LS_ABILITY_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, event.EventModuleBlockTooltipData(contexts.HangarContext()), advanced.HangarModuleAdvanced(contexts.HangarContext())),
     AdvancedShellBuilder(LS_MAIN_SHELL, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, event.EventShellBlockToolTipData(contexts.TechMainContext()), advanced.HangarShellAdvanced(contexts.TechMainContext())))
