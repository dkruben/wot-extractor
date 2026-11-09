# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pet_system_common/PetSynergyConfig.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pet_system_common/PetSynergyConfig.py
from __future__ import absolute_import
import typing
from pet_system_common.pet_constants import PetSynergyConsts as pc
if typing.TYPE_CHECKING:
    from typing import Dict

class PetSynergyConfig(object):

    def __init__(self, config):
        self._config = config

    def getSynergyById(self, synergyId):
        return self._config.get(synergyId, {})

    def getSynergyLevels(self, synergyId):
        return self.getSynergyById(synergyId).get(pc.SYNERGY_LEVELS, tuple())

    def getSynergyPoints(self, synergyPointType):
        return self._config.get(pc.POINTS, {}).get(synergyPointType, 0)

    def getSynergeyDecayDays(self):
        return self._config.get(pc.DECAY_DAYS, 0)

    def getSynergyDecayPoints(self):
        return self._config.get(pc.DECAY_POINTS, 0)
