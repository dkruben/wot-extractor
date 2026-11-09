# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pet_system_common/BonusConfig.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pet_system_common/BonusConfig.py
from __future__ import absolute_import
import typing
from pet_system_common.pet_constants import PetBonusesConsts as pc
if typing.TYPE_CHECKING:
    from typing import Dict

class BonusConfig(object):

    def __init__(self, config):
        self._config = config

    def getBonuses(self):
        return self._config

    def getBonusById(self, bonusID):
        return self._config.get(bonusID, {})

    def getBonusResources(self, bonusID):
        return self.getBonusById(bonusID).get(pc.BONUS_RESOURCE, pc.EMPTY_BONUS)
