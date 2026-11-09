# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pet_system_common/PetPromoConfig.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pet_system_common/PetPromoConfig.py
from __future__ import absolute_import
import typing
from pet_system_common.pet_constants import PetPromoConsts
if typing.TYPE_CHECKING:
    from typing import List, Dict, Iterable
INVALID_PET_NAME_ID = -1

class PromoSource(object):
    QUEST_PROGRESSION = 'quest_progression'
    SHOP = 'shop'
    ALL = (QUEST_PROGRESSION, SHOP)


class PetPromoConfig(object):

    def __init__(self, config):
        self._config = config

    def getPets(self):
        return self._config.get(PetPromoConsts.PETS, {})

    def isEnabled(self):
        return self._config.get(PetPromoConsts.IS_ENABLED, False)

    def getUrl(self, petID):
        return self.getPets().get(petID, {}).get(PetPromoConsts.URL, '')

    def getSources(self, petID):
        return self.getPets().get(petID, {}).get(PetPromoConsts.SOURCES, set())

    def getShopUrl(self, petID):
        return self.getPets().get(petID, {}).get(PetPromoConsts.SHOP_URL, '')

    def getAvailablePets(self, unlockedPetsIDs):
        return [petID for petID in self.getPets() if petID not in unlockedPetsIDs]
