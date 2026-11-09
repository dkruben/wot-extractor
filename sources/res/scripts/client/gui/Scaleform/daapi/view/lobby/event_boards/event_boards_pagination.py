# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_pagination.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_pagination.py
from __future__ import absolute_import
import Event
from gui.Scaleform.daapi.view.meta.PaginationMeta import PaginationMeta
from gui.shared.formatters import text_styles

class EventBoardsPagination(PaginationMeta):

    def __init__(self):
        super(EventBoardsPagination, self).__init__()
        self.onStepPage = Event.Event()

    def showPage(self, direction):
        self.onStepPage(direction)

    def updatePage(self, page, pagesAmount):
        self.as_setPageS(('{} / {}').format(text_styles.highTitle(page), pagesAmount))
        self.as_setEnabledS(page > 1, page < pagesAmount)
