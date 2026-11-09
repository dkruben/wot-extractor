# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/commands/mechanic_controls/nitro_control.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/commands/mechanic_controls/nitro_control.py
from __future__ import absolute_import
import typing, logging, BigWorld, CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicles.mechanics.mechanic_helpers import getPlayerVehicleMechanicComponent
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicKey
_logger = logging.getLogger(__name__)
CLICK_THRESHOLD = 0.75

class NitroActivationControl(InputHandlerCommand):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, mechanic):
        self.__mechanic = mechanic
        self.__startTime = BigWorld.time()
        self.__stopTime = BigWorld.time()

    def __alternateNitro(self):
        mechanicComponent = getPlayerVehicleMechanicComponent(self.__mechanic)
        if mechanicComponent:
            mechanicComponent.alternateOnState()

    def __cancelNitro(self):
        mechanicComponent = getPlayerVehicleMechanicComponent(self.__mechanic)
        if mechanicComponent:
            mechanicComponent.tryDeactivate()

    def handleKeyEvent(self, isDown, key, mods, event=None):
        mechanicCmd = CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION
        if not CommandMapping.g_instance.isFired(mechanicCmd, key):
            return False
        if isDown:
            self.__startTime = BigWorld.time()
        else:
            self.__stopTime = BigWorld.time()
        if not isDown and abs(self.__stopTime - self.__startTime) < CLICK_THRESHOLD:
            return False
        if isDown:
            self.__alternateNitro()
        else:
            self.__cancelNitro()
        return True


def createNitroActivationControl(mechanic, *_, **__):
    return NitroActivationControl(mechanic)
