# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/persistent_data_cache_common/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/persistent_data_cache_common/common.py
from __future__ import absolute_import
import typing, time, logging
from contextlib import contextmanager
LOGGER_NAME = 'PersistentDataCache'
DEFAULT_SAVING_TIMEOUT = 120.0

def getLogger(*names):
    return logging.getLogger(('{}').format(('.').join((LOGGER_NAME,) + names)))


_logger = getLogger('Metrics')

class MeasureExecutionTime(object):
    __slots__ = ('_logger', '_metricName', '_totalTime')

    def __init__(self, metricName, logger=None):
        self._logger = logger or _logger
        self._metricName = metricName
        self._totalTime = 0.0

    def printTotalTime(self, reset=True):
        self._logger.debug('%s total time: %s', self._createMetricName(), self._totalTime)
        if reset:
            self._totalTime = 0.0

    @contextmanager
    def start(self, section=''):
        startTime = time.time()
        try:
            yield
        finally:
            endTime = time.time() - startTime
            self._totalTime += endTime
            self._logger.debug('%s executed in %s seconds.', self._createMetricName(section), endTime)

    def _createMetricName(self, section=''):
        if section:
            return (self._metricName, section)
        return (self._metricName,)

    def __call__(self, func, section=''):

        def wrapper(*args, **kwargs):
            startTime = time.time()
            result = func(*args, **kwargs)
            endTime = time.time() - startTime
            self._totalTime += endTime
            self._logger.debug('%s executed in %s seconds.', self._createMetricName(section), endTime)
            return result

        return wrapper
