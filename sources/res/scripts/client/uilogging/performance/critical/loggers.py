# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/performance/critical/loggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/performance/critical/loggers.py
from __future__ import absolute_import
import logging, BigWorld
from uilogging.base.logger import _BaseLogger as Logger
from uilogging.constants import DEFAULT_LOGGER_NAME
from uilogging.performance.critical.constants import Features, Groups, LogActions
from uilogging.helpers import getClientSessionID
from wotdecorators import noexcept
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class MemoryCriticalLogger(Logger):
    __slots__ = ()

    def __init__(self):
        super(MemoryCriticalLogger, self).__init__(Features.MEMORY_CRITICAL, Groups.EVENT)

    def initialize(self):
        self.ensureSession()

    @noexcept
    def log(self, sessionStartedAt=0):
        _logger.debug('Critical memory metrics requested.')
        if not self.disabled or BigWorld.wg_debugLogging():
            data = BigWorld.collectLastMemoryCriticalEvent()
        if self.disabled:
            return
        self.ensureSession()
        sessionID = getClientSessionID()
        if data:
            self._logImmediately(LogActions.MEMORY_CRITICAL_EVENT, session_id=sessionID, started_at=sessionStartedAt, **data)
        else:
            _logger.error('Memory critical metrics are empty')
