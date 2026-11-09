# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_events/gun_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_events/gun_events.py
from __future__ import absolute_import
import typing, CGF, Vehicular

def postVehicularSingleShotEvent(spaceID, entityID, slotName, gunID):
    CGF.postEvent(spaceID, Vehicular.SingleShotEvent(entityID=entityID, slotName=slotName, gunID=gunID))


def postVehicularMultiShotEvent(spaceID, entityID, slotName, gunIDs):
    CGF.postEvent(spaceID, Vehicular.MultiShotEvent(entityID=entityID, slotName=slotName, gunIDs=gunIDs))


def postVehicularContinuousBurstEvent(spaceID, entityID, slotName, active):
    CGF.postEvent(spaceID, Vehicular.ContinuousBurstEvent(entityID=entityID, slotName=slotName, active=active))


def postVehicularFireRateChangedEvent(spaceID, entityID, slotName, shotsPerSec):
    CGF.postEvent(spaceID, Vehicular.FireRateChangedEvent(entityID=entityID, slotName=slotName, shotsPerSec=shotsPerSec))


def postVehicularVariablesChangedEvent(spaceID, entityID, slotName, varValueMap):
    CGF.postEvent(spaceID, Vehicular.VariablesChangedEvent(entityID=entityID, slotName=slotName, varValueMap=varValueMap))
