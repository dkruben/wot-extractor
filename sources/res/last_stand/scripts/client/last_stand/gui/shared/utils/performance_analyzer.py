# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/shared/utils/performance_analyzer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/shared/utils/performance_analyzer.py
from __future__ import absolute_import
import logging, typing
from future.utils import viewitems
from enum import IntEnum
from helpers.statistics import HARDWARE_SCORE_PARAMS
import BigWorld
from gui.shared.utils.graphics import getGraphicsEngineValue
if typing.TYPE_CHECKING:
    from typing import Optional, Dict
_logger = logging.getLogger(__name__)

class LimitType(IntEnum):
    SYSTEM_DATA = 0
    HARDWARE_PARAMS = 1


class PerformanceGroup(object):
    LOW_RISK = 0
    MEDIUM_RISK = 1
    HIGH_RISK = 2


DEFAULT_PERFORMANCE_GROUP_LIMITS = {(PerformanceGroup.HIGH_RISK): [{(LimitType.SYSTEM_DATA): {'osBit': 1, 'graphicsEngine': 0}}, {(LimitType.HARDWARE_PARAMS): {(HARDWARE_SCORE_PARAMS.PARAM_GPU_MEMORY): 490}}, {(LimitType.SYSTEM_DATA): {'graphicsEngine': 0}, (LimitType.HARDWARE_PARAMS): {(HARDWARE_SCORE_PARAMS.PARAM_RAM): 2900}}], (PerformanceGroup.MEDIUM_RISK): [{(LimitType.HARDWARE_PARAMS): {(HARDWARE_SCORE_PARAMS.PARAM_GPU_SCORE): 300}}, {(LimitType.HARDWARE_PARAMS): {(HARDWARE_SCORE_PARAMS.PARAM_CPU_SCORE): 50000}}]}

class PerformanceAnalyzerMixin(object):
    __performanceGroup = None

    def __init__(self, *args, **kwargs):
        super(PerformanceAnalyzerMixin, self).__init__(*args, **kwargs)
        self.__performanceGroup = None
        self.__lastLimitMap = None
        return

    def getPerformanceGroup(self, groupLimitMap=None, defaultGroup=PerformanceGroup.LOW_RISK):
        limitMap = groupLimitMap or DEFAULT_PERFORMANCE_GROUP_LIMITS
        if limitMap != self.__lastLimitMap:
            self.__lastLimitMap = limitMap
            self.__performanceGroup = None
        if not self.__performanceGroup:
            self.__analyzeClientSystem(limitMap, defaultGroup)
            _logger.debug('Current performance group %s, self=%s', self.__performanceGroup, self)
        return self.__performanceGroup

    def __analyzeClientSystem(self, groupLimitMap, defaultGroup):
        stats = BigWorld.wg_getClientStatistics()
        stats['graphicsEngine'] = getGraphicsEngineValue()
        self.__performanceGroup = defaultGroup
        for groupName, conditions in viewitems(groupLimitMap):
            for currentLimit in conditions:
                condValid = True
                systemStats = currentLimit.get(LimitType.SYSTEM_DATA, {})
                for key, limit in viewitems(systemStats):
                    currValue = stats.get(key, None)
                    if currValue is None or currValue != limit:
                        condValid = False

                hardwareParams = currentLimit.get(LimitType.HARDWARE_PARAMS, {})
                for key, limit in viewitems(hardwareParams):
                    currValue = BigWorld.getAutoDetectGraphicsSettingsScore(key)
                    if currValue >= limit:
                        condValid = False

                if condValid:
                    self.__performanceGroup = groupName

        return
