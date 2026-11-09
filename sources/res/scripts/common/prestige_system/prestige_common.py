# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/prestige_system/prestige_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/prestige_system/prestige_common.py
from __future__ import absolute_import
import typing
from constants import IS_CLIENT
from prestige_system import getCache, computePrestigeCache
if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional
PrestigeGrade = typing.NamedTuple('_PrestigeGrade', (
 (
  'level', int),
 (
  'prestigeMarkID', int),
 (
  'main', bool)))

class PrestigeConfig(object):

    class GradeKeys(object):
        LEVEL = 'level'
        MARK_ID = 'prestigeMarkID'
        MAIN = 'main'

    def __init__(self, config):
        self._config = config
        if IS_CLIENT:
            self.__cache = {}
            if self._config:
                computePrestigeCache(self._config, self.__cache)
        else:
            self.__cache = getCache()

    @property
    def isEnabled(self):
        return self._config.get('enabled', False)

    @property
    def prestigeCoefficient(self):
        return self._config.get('prestigeCoefficient', 0)

    @property
    def prestigePoints(self):
        return self.__cache.get('prestigePoints', {})

    @property
    def defaultMaxLevel(self):
        return self._config.get('default', {}).get('maxLevel', 0)

    @property
    def grades(self):
        return self._config.get('grades', [])

    def getSortedGrades(self, key=GradeKeys.LEVEL):
        return [PrestigeGrade(**g) for g in sorted(self.grades, key=(lambda v: v.get(key)))]

    def getSortedMainGrades(self, key=GradeKeys.LEVEL):
        return [PrestigeGrade(**g) for g in sorted(self.grades, key=(lambda v: v.get(key))) if g.get(self.GradeKeys.MAIN, False)]

    def getVehiclePoints(self, vehCD):
        return self.prestigePoints.get(vehCD)
