# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/tooltips/crew_book.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/tooltips/crew_book.py
from __future__ import absolute_import
from gui.shared.formatters import text_styles
from gui.shared.tooltips import TOOLTIP_TYPE, formatters
from gui.shared.tooltips.common import BlocksTooltipData

class CrewBookTooltipDataBlock(BlocksTooltipData):

    def __init__(self, context):
        super(CrewBookTooltipDataBlock, self).__init__(context, TOOLTIP_TYPE.CREW_BOOK)
        self._setContentMargin(bottom=8)
        self._setWidth(320)

    def _packBlocks(self, *args, **kwargs):
        items = super(CrewBookTooltipDataBlock, self)._packBlocks()
        item = self.context.buildItem(*args, **kwargs)
        block = []
        block.append(formatters.packTextBlockData(text=text_styles.highTitle(item.userName)))
        block.append(formatters.packTextBlockData(text=text_styles.main(item.fullDescription)))
        items.append(formatters.packBuildUpBlockData(block))
        return items
