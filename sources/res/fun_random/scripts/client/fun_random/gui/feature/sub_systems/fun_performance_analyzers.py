# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_performance_analyzers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_performance_analyzers.py
from __future__ import absolute_import
import BigWorld
from gui.shared.utils.graphics import isLowPreset

class PerformanceGroup(object):
    LOW_RISK = 0
    MEDIUM_RISK = 1
    HIGH_RISK = 2


class IPerformanceAlertHandler(object):

    def analyze(self):
        raise NotImplementedError


class GraphicsPresetAnalyzerHandler(IPerformanceAlertHandler):
    __ALERT_LEVELS_KEYS = {(PerformanceGroup.HIGH_RISK): [
                                    'LOW'], 
       (PerformanceGroup.MEDIUM_RISK): [
                                      'MEDIUM']}

    def analyze(self):
        recommendedPresetIndex = BigWorld.detectGraphicsPresetFromSystemSettings()
        presetId = BigWorld.getSystemPerformancePresetIdFromName
        currentLevel = PerformanceGroup.LOW_RISK
        for level, alertNames in self.__ALERT_LEVELS_KEYS.items():
            if alertNames and any(recommendedPresetIndex == presetId(pName) for pName in alertNames) and level > currentLevel:
                currentLevel = level

        return currentLevel


class RenderPipelineAnalyzerHandler(IPerformanceAlertHandler):

    def analyze(self):
        if isLowPreset():
            return PerformanceGroup.MEDIUM_RISK
        return PerformanceGroup.LOW_RISK


class HighPerformanceGroupHandler(IPerformanceAlertHandler):

    def analyze(self):
        return PerformanceGroup.HIGH_RISK


class MediumPerformanceGroupHandler(IPerformanceAlertHandler):

    def analyze(self):
        return PerformanceGroup.MEDIUM_RISK
