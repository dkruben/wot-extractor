# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/feature/processor.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/feature/processor.py
from __future__ import absolute_import
import BigWorld, logging
from gui.shared.gui_items.processors import Processor
_logger = logging.getLogger(__name__)

class AdventCalendarDoorsProcessor(Processor):

    def __init__(self, dayID, currency=''):
        super(AdventCalendarDoorsProcessor, self).__init__()
        self.__dayID = dayID
        self.__currency = currency

    def _errorHandler(self, code, errStr='', ctx=None):
        _logger.error('Failed to open door=%d, errorCode=%d, errorMsg=%s', self.__dayID, code, errStr)
        return super(AdventCalendarDoorsProcessor, self)._errorHandler(code, errStr, ctx)

    def _request(self, callback):
        _logger.debug('Make server request to open Advent door number: %d', self.__dayID)
        BigWorld.player().AdventCalendarAccountComponent.openAdventCalendarDoor(self.__dayID, self.__currency, (lambda code, errStr: self._response(code, callback, errStr)))
