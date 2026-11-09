# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/mechanic_commands/mechanic_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/mechanic_commands/mechanic_interfaces.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand

class IMechanicCommandsComponent(object):

    @property
    def commandsEvents(self):
        raise NotImplementedError


class IMechanicCommandsEventsLogic(object):
    onMechanicCommand = None

    def processMechanicCommand(self, command):
        raise NotImplementedError


class IMechanicCommandsEvents(IClientEventsContainer, IMechanicCommandsEventsLogic):
    pass


class IMechanicCommandsListenerLogic(object):

    def onMechanicCommand(self, command):
        pass


class IMechanicCommandsListener(IClientEventsContainerListener, IMechanicCommandsListenerLogic):
    pass
