# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/components/component_wrappers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/components/component_wrappers.py
from __future__ import absolute_import
import typing
from functools import wraps
import BigWorld
if typing.TYPE_CHECKING:
    from Avatar import PlayerAvatar

def ifAppearanceReady(method):

    @wraps(method)
    def wrapper(vehicleComponent, *args, **kwargs):
        if vehicleComponent.isAppearanceReady():
            method(vehicleComponent, *args, **kwargs)

    return wrapper


def ifPlayerVehicle(method):

    @wraps(method)
    def wrapper(vehicleComponent, *args, **kwargs):
        player = BigWorld.player()
        if vehicleComponent.isPlayerVehicle(player):
            method(vehicleComponent, player, *args, **kwargs)

    return wrapper


def ifObservedVehicle(method):

    @wraps(method)
    def wrapper(vehicleComponent, *args, **kwargs):
        player = BigWorld.player()
        vehicle = None if player is None else player.getVehicleAttached()
        if vehicleComponent.isObservedVehicle(player, vehicle):
            method(vehicleComponent, player, vehicle, *args, **kwargs)
        return

    return wrapper
