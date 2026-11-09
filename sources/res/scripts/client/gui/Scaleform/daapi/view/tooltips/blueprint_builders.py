# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/blueprint_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/blueprint_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import blueprint
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.BLUEPRINT_INFO, TOOLTIPS_CONSTANTS.BLUEPRINT_UI, blueprint.VehicleBlueprintTooltipData(contexts.BlueprintContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_INFO, TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_UI, blueprint.BlueprintFragmentTooltipData(contexts.BlueprintContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BLUEPRINT_EMPTY_SLOT_INFO, TOOLTIPS_CONSTANTS.BLUEPRINT_EMPTY_SLOT_UI, blueprint.BlueprintEmptySlotTooltipData(contexts.BlueprintContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BLUEPRINT_CONVERT_INFO, TOOLTIPS_CONSTANTS.BLUEPRINT_EMPTY_SLOT_UI, blueprint.ConvertInfoBlueprintTooltipData(contexts.BlueprintContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BLUEPRINT_RANDOM_INFO, TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_UI, blueprint.BlueprintFragmentRandomTooltipData(contexts.BlueprintContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BLUEPRINT_RANDOM_NATIONAL_INFO, TOOLTIPS_CONSTANTS.BLUEPRINT_FRAGMENT_UI, blueprint.BlueprintFragmentRandomNationalTooltipData(contexts.BlueprintContext())))
