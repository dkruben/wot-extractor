# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_common/cgf_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_common/cgf_helpers.py
from __future__ import absolute_import
import typing, CGF
from constants import IS_EDITOR, IS_CGF_DUMP
if IS_EDITOR or IS_CGF_DUMP:

    class Vehicle(object):
        pass


else:
    from Vehicle import Vehicle

def getVehicleEntityByVehicleGameObject(vehicleGameObject):
    return vehicleGameObject.findWrite(Vehicle)


def tryActivateGameObject(gameObject):
    if not gameObject:
        return
    gameObject.activate()


def tryDeactivateGameObject(gameObject):
    if not gameObject:
        return
    gameObject.deactivate()
