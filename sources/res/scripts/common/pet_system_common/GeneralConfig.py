# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pet_system_common/GeneralConfig.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pet_system_common/GeneralConfig.py
from __future__ import absolute_import
import typing
from pet_system_common.pet_constants import PetSystemGeneralConsts as pc
if typing.TYPE_CHECKING:
    from typing import Dict

class GeneralConfig(object):

    def __init__(self, config):
        self._config = config

    @property
    def isEnabled(self):
        return self._config.get(pc.ENABLED, False)

    @property
    def eventsPerDay(self):
        return self._config.get(pc.EVENT_PER_DAY, 0)

    @property
    def eventsMinBattles(self):
        return self._config.get(pc.EVENT_MIN_BATTLES, 0)

    @property
    def eventsMaxBattles(self):
        return self._config.get(pc.EVENT_MAX_BATTLES, 0)

    @property
    def bonusesPerDay(self):
        return self._config.get(pc.BONUSES_PER_DAY, 0)

    @property
    def showCaseEnabled(self):
        return self._config.get(pc.SHOW_CASE_ENABLED, False)
