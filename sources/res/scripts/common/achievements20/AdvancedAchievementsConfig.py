# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/achievements20/AdvancedAchievementsConfig.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/achievements20/AdvancedAchievementsConfig.py
from __future__ import absolute_import
from typing import TYPE_CHECKING
from achievements20.settings import AdvancedAchievementsConst
if TYPE_CHECKING:
    from typing import Optional

class AdvancedAchievementsConfig(object):
    __slots__ = ('_config', )

    def __init__(self, config):
        self._config = config

    def isAdvancedAchievementEnabled(self):
        return self._config[AdvancedAchievementsConst.ENABLED]

    def isVehicleAchievementsEnabled(self):
        return self.isAdvancedAchievementEnabled() and self._config[AdvancedAchievementsConst.VEHICLE_ACHIEVEMENTS_ENABLED]

    def isCustomizationAchievementsEnabled(self):
        return self.isAdvancedAchievementEnabled() and self._config[AdvancedAchievementsConst.CUSTOMIZATION_ACHIEVEMENTS_ENABLED]

    def getExcludedVehicles(self):
        return self._config[AdvancedAchievementsConst.EXCLUDED_VEHICLES]

    def getExcludedCustomizations(self):
        return self._config[AdvancedAchievementsConst.EXCLUDED_CUSTOMIZATIONS]
