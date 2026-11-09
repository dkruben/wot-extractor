# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ArtilleryEquipment.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ArtilleryEquipment.py
from __future__ import absolute_import
import math_utils, BigWorld

class ArtilleryEquipment(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        launchDir = math_utils.createRotationMatrix((self.__dict__['yaw'], self.__dict__['pitch'], 0)).applyToAxis(2)
        launchDir.normalise()
        self.__launchVelocity = launchDir * self.speed

    @property
    def launchVelocity(self):
        return self.__launchVelocity
