# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/pet_system/synergy_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/pet_system/synergy_helper.py
import typing
from collections import namedtuple
from helpers import dependency
from skeletons.gui.pet_system import IPetSystemController
if typing.TYPE_CHECKING:
    from typing import Optional, Tuple
    PetID = int
    Synergy = int
    SynergyLevel = int
SynergyProgress = namedtuple('SynergyProgress', ('cPoints', 'maxPoints'))

class SynergyItem(object):
    petController = dependency.descriptor(IPetSystemController)

    @classmethod
    def getSynergyLevels(cls, petID=None):
        petID = petID or cls.petController.getActivePet()
        synergyGroupID = cls.petController.getPetsConfig().getPetSynergyGroupID(petID)
        return cls.petController.getPetSynergyConfig().getSynergyLevels(synergyGroupID)

    @classmethod
    def getSynergyPoints(cls, petID=None):
        petID = petID or cls.petController.getActivePet()
        return cls.petController.requester.getSynergyPoints(petID)

    @classmethod
    def getSynergyLevel(cls, petID=None):
        petID = petID or cls.petController.getActivePet()
        return cls.petController.requester.getSynergyLevel(petID)

    @classmethod
    def getSynergyProgression(cls, petID=None):
        petID = petID or cls.petController.getActivePet()
        return SynergyProgress(cls.getSynergyPoints(petID), cls.getSynergyLevels(petID)[-1])

    @classmethod
    def isMaxSynergyLevel(cls, petID=None):
        petID = petID or cls.petController.getActivePet()
        return cls.getSynergyLevel(petID) >= len(cls.getSynergyLevels(petID)) - 1

    @classmethod
    def isFirstClickSynergyAvailable(cls, petID=None):
        petID = petID or cls.petController.getActivePet()
        return petID not in cls.petController.requester.getFirstClickedSynergyPets()
