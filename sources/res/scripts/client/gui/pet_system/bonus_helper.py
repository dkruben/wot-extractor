# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/pet_system/bonus_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/pet_system/bonus_helper.py
import typing
from collections import namedtuple
from gui.impl.gen.view_models.views.lobby.pet_system.pet_bonus_model import PetBonusModel
from gui.impl.gen.view_models.views.lobby.pet_system.promotion_model import PromoBonus
from helpers import dependency
from pet_system_common.pet_constants import PET_SYSTEM_RESOURCE_TO_TEXT
from skeletons.gui.pet_system import IPetSystemController
if typing.TYPE_CHECKING:
    from typing import Set, Iterable
    from frameworks.wulf import Array
    from gui.pet_system.requester import BonusID
    from pet_system_common import BonusConfig
BonusResource = namedtuple('Bonus', ('resourceType', 'resourceValue', 'isPercent'))
BonusNameToPromoStr = {'credits': (PromoBonus.CREDITS.value)}

class BonusItem(object):
    petController = dependency.descriptor(IPetSystemController)

    @classmethod
    def getActiveBonus(cls):
        return cls.petController.requester.getActiveBonus()

    @classmethod
    def getAppliedBonusCount(cls):
        return cls.petController.requester.getAppliedBonusCount()

    @classmethod
    def getBonusesPerDay(cls):
        return cls.petController.getGeneralConfig().bonusesPerDay

    @classmethod
    def getPetBonusConfig(cls):
        return cls.petController.getBonusConfig()

    @classmethod
    def getPetBonuses(cls, petID):
        return cls.petController.getPetsConfig().getPetUnlockedBonuses(petID)

    @classmethod
    def getBonusResource(cls, bonusID):
        resourceType, resourceValue, isPercent = cls.getPetBonusConfig().getBonusResources(bonusID)
        return BonusResource(resourceType, resourceValue, isPercent)

    @classmethod
    def getBonusName(cls, bonusID):
        resource = cls.getBonusResource(bonusID)
        return PET_SYSTEM_RESOURCE_TO_TEXT.get(resource.resourceType)

    @classmethod
    def getBonusValue(cls, bonusID):
        resource = cls.getBonusResource(bonusID)
        return resource.resourceValue

    @classmethod
    def getAvailableBonuses(cls):
        return cls.petController.getAvailableBonuses()

    @classmethod
    def packBonusModelData(cls, bonusIDs, bonusModelsArray):
        for bonusID in bonusIDs:
            model = PetBonusModel()
            model.setId(bonusID)
            model.setName(cls.getBonusName(bonusID) or '')
            model.setValue(str(cls.getBonusValue(bonusID)))
            bonusModelsArray.addViewModel(model)

        bonusModelsArray.invalidate()
