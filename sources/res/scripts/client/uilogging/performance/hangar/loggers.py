# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/performance/hangar/loggers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/performance/hangar/loggers.py
from __future__ import absolute_import
import logging, typing
from future.utils import viewitems
import BigWorld
from uilogging.base.logger import _BaseLogger as Logger, createPartnerID
from uilogging.constants import DEFAULT_LOGGER_NAME
from uilogging.performance.hangar.constants import Features, Groups, LogActions
from uilogging.helpers import getClientSessionID
from wotdecorators import noexcept
if typing.TYPE_CHECKING:
    from uilogging.types import GroupType, PartnerIdType
_logger = logging.getLogger(DEFAULT_LOGGER_NAME)

class _BaseHangarMetricsLogger(Logger):
    __slots__ = ()

    def __init__(self, group):
        super(_BaseHangarMetricsLogger, self).__init__(Features.METRICS, group)

    @noexcept
    def log(self, data, partnerID=None, sessionID=''):
        if not isinstance(data, dict):
            _logger.error('Wrong metrics data type: [dict != %s].', type(data))
            return
        if data:
            super(_BaseHangarMetricsLogger, self)._log(LogActions.SPACE_DISPOSED, partnerID=partnerID, session_id=sessionID, **data)


class _HangarSpaceMetricsLogger(_BaseHangarMetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(_HangarSpaceMetricsLogger, self).__init__(Groups.SPACE)

    def log(self, data, partnerID=None, sessionID=''):
        if not isinstance(data, dict):
            _logger.error('Wrong metrics data type: [dict != %s].', type(data))
            return
        if data:
            super(_HangarSpaceMetricsLogger, self).log(data, partnerID=partnerID, sessionID=sessionID)


class _HangarViewsMetricsLogger(_BaseHangarMetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(_HangarViewsMetricsLogger, self).__init__(Groups.VIEWS)

    def log(self, data, partnerID=None, sessionID=''):
        if not isinstance(data, list):
            _logger.error('Wrong views metrics data type: [list != %s].', type(data))
            return
        for viewData in data:
            super(_HangarViewsMetricsLogger, self).log(viewData, partnerID=partnerID, sessionID=sessionID)


class HangarMetricsLogger(object):
    __slots__ = ('_loggers', '_defaultLogger')

    def __init__(self):
        self._loggers = {(Groups.SPACE.value): (_HangarSpaceMetricsLogger()), 
           (Groups.VIEWS.value): (_HangarViewsMetricsLogger())}
        self._defaultLogger = self._loggers[Groups.SPACE.value]

    def initialize(self):
        self._defaultLogger.ensureSession()

    @noexcept
    def log(self):
        _logger.debug('Hangar performance metrics requested.')
        if not self._defaultLogger.disabled or BigWorld.wg_debugLogging():
            data = BigWorld.wg_getHangarStatistics()
        if self._defaultLogger.disabled:
            return
        if not data:
            _logger.debug('Hangar performance metrics are empty.')
            return
        diff = set(data) ^ set(self._loggers)
        if diff:
            _logger.error('Difference in loggers and received metrics groups: %s.', diff)
            return
        partnerID = createPartnerID()
        clientSessionID = getClientSessionID()
        for group, stats in viewitems(data):
            self._loggers[group].log(stats, partnerID=partnerID, sessionID=clientSessionID)
