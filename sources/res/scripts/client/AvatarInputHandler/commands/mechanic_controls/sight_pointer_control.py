# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/sight_pointer_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/mechanic_controls/sight_pointer_control.py
from __future__ import absolute_import
import typing, CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from vehicles.mechanics.mechanic_helpers import getPlayerVehicleMechanicComponent
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicKey

class SightPointerActivationControl(InputHandlerCommand):

    def __init__(self, mechanic):
        self.__mechanic = mechanic

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if not isDown or not CommandMapping.g_instance.isFired(CommandMapping.CMD_CM_SPECIAL_ABILITY, key):
            return False
        mechanicComponent = getPlayerVehicleMechanicComponent(self.__mechanic)
        if mechanicComponent is not None:
            mechanicComponent.alternateOnState()
        return True


def createSightPointerActivationControl(mechanic, *_, **__):
    return SightPointerActivationControl(mechanic)
