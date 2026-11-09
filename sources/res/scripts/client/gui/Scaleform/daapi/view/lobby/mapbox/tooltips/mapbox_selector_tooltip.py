# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_selector_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/mapbox/tooltips/mapbox_selector_tooltip.py
from __future__ import absolute_import
from gui import makeHtmlString
from gui.impl.gen import R
from gui.impl import backport
from gui.mapbox.mapbox_helpers import getTillTimeString
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES
from gui.Scaleform.daapi.view.lobby.formatters import tooltips
from gui.shared.formatters import text_styles
from gui.shared.formatters.ranges import toRomanRangeString
from gui.shared.tooltips import formatters, TOOLTIP_TYPE
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency
from skeletons.gui.game_control import IMapboxController

class MapboxSelectorTooltip(BlocksTooltipData):
    __mapboxCtrl = dependency.descriptor(IMapboxController)
    __BODY_TEMPLATE_PATH = 'html_templates:lobby/tooltips/battle_type_selector'
    __BODY_TEMPLATE_KEY = SELECTOR_BATTLE_TYPES.MAPBOX

    def __init__(self, context):
        super(MapboxSelectorTooltip, self).__init__(context, TOOLTIP_TYPE.MAPBOX_SELECTOR_INFO)
        self._setWidth(320)

    def _packBlocks(self, *args):
        items = []
        items.append(self.__packMainBlock())
        if self.__mapboxCtrl.isFrozen() or not self.__mapboxCtrl.isEnabled():
            items.append(self.__packFrozenBlock())
        else:
            actualSeason = self.__mapboxCtrl.getCurrentSeason() or self.__mapboxCtrl.getNextSeason()
            seasonIsStarted = self.__mapboxCtrl.getCurrentSeason() is not None
            timeStrGetter = getTillTimeString if seasonIsStarted else backport.getDateTimeFormat
            items += tooltips.getScheduleBlock(self.__mapboxCtrl, SELECTOR_BATTLE_TYPES.MAPBOX, actualSeason, seasonIsStarted, timeStrGetter)
        return items

    def __packMainBlock(self):
        header = backport.text(R.strings.tooltips.battleTypes.mapbox.header())
        body = makeHtmlString(self.__BODY_TEMPLATE_PATH, self.__BODY_TEMPLATE_KEY, ctx={'range': (toRomanRangeString(self.__mapboxCtrl.getModeSettings().levels))})
        return formatters.packTitleDescBlock(title=text_styles.middleTitle(header), desc=text_styles.main(body))

    def __packFrozenBlock(self):
        return formatters.packTextBlockData(text=text_styles.main(backport.text(R.strings.tooltips.battleTypes.mapbox.frozen.body())))
