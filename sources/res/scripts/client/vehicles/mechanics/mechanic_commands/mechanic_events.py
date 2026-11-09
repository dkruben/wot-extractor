# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/mechanic_commands/mechanic_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/mechanic_commands/mechanic_events.py
from __future__ import absolute_import
import typing, weakref
from events_containers.common.containers import ClientEventsContainer
from events_containers.components.common import ClientComponentEventsDebugger
from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsEventsLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand
    from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsComponent

class MechanicCommandsEvents(ClientEventsContainer, IMechanicCommandsEventsLogic):

    def __init__(self, component):
        super(MechanicCommandsEvents, self).__init__()
        self.__componentRef = weakref.ref(component)
        self.onMechanicCommand = self._createEvent()

    def destroy(self):
        self.__componentRef = None
        super(MechanicCommandsEvents, self).destroy()
        return

    def processMechanicCommand(self, command):
        self.onMechanicCommand(command)

    def _getComponent(self):
        if self.__componentRef is not None:
            return self.__componentRef()
        else:
            return

    def _createEventsDebugger(self):
        return MechanicCommandsEventsDebugger(self, self._getComponent())


class MechanicCommandsEventsDebugger(ClientComponentEventsDebugger):
    _EVENTS_DEBUG_PREFIX = 'MECHANIC_CMD'
