# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/crew_skin_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/crew_skin_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import crew_skin
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

class CrewSkinTooltipBuilder(DataBuilder):
    __slots__ = ()

    def __init__(self, tooltipType, linkage):
        super(CrewSkinTooltipBuilder, self).__init__(tooltipType, linkage, crew_skin.CrewSkinTooltipDataBlock(contexts.CrewSkinContext()))

    def _buildData(self, _advanced, crewSkinID, *args, **kwargs):
        return super(CrewSkinTooltipBuilder, self)._buildData(_advanced, crewSkinID)


def getTooltipBuilders():
    return (
     CrewSkinTooltipBuilder(TOOLTIPS_CONSTANTS.CREW_SKIN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),)
