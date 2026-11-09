# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/fortifications_builder.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/fortifications_builder.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import fortifications
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.DIRECT_MODULE, TOOLTIPS_CONSTANTS.REF_SYS_DIRECTS_UI, fortifications.ToolTipRefSysDirects(contexts.FortificationContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.FORT_SORTIE_SLOT, TOOLTIPS_CONSTANTS.SUITABLE_VEHICLE_UI, fortifications.FortificationsSlotToolTipData(contexts.FortificationContext())))
