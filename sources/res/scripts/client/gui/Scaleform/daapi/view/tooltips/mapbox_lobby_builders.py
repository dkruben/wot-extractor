# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/mapbox_lobby_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/mapbox_lobby_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder
from gui.Scaleform.daapi.view.lobby.mapbox.tooltips.mapbox_selector_tooltip import MapboxSelectorTooltip
from gui.Scaleform.daapi.view.lobby.mapbox.tooltips.mapbox_progression_tooltip import MapboxProgressionTooltip
from gui.Scaleform.daapi.view.lobby.mapbox.tooltips.mapbox_calendar_tooltip import MapboxCalendarTooltip
from gui.Scaleform.daapi.view.lobby.mapbox.tooltips.mapbox_calendar_day_tooltip import MapboxCalendarDayTooltip
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.MAPBOX_SELECTOR_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, MapboxSelectorTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.MAPBOX_PROGRESSION_PREVIEW, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, MapboxProgressionTooltip(contexts.QuestContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.MAPBOX_CALENDAR, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, MapboxCalendarTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.MAPBOX_CALENDAR_DAY, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, MapboxCalendarDayTooltip(contexts.ToolTipContext(None))))
