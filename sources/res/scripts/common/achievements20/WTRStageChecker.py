# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/achievements20/WTRStageChecker.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/achievements20/WTRStageChecker.py
from __future__ import absolute_import
from bisect import bisect_right

class WTRStageChecker(object):
    __slots__ = [
     '_flatStages', '_stagesRatingsCache']

    def __init__(self, wtrStages):
        self._flatStages = [(groupIndex + 1, stageIndex + 1, startRating) for groupIndex, group in enumerate(wtrStages) for stageIndex, startRating in enumerate(group)]
        self._stagesRatingsCache = tuple(wtrStage[2] for wtrStage in self._flatStages)

    def getStage(self, wtr):
        index = bisect_right(self._stagesRatingsCache, wtr) - 1
        if index < 0:
            return None
        else:
            return self._flatStages[index]
