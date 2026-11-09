# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/wheeled_dash/mechanic_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/generic_mechanics/wheeled_dash/mechanic_events.py
from __future__ import absolute_import
from events_containers.common.containers import ClientEventsContainer, ClientEventsContainerDebugger
from vehicles.mechanics.generic_mechanics.wheeled_dash.mechanic_interfaces import IWheeledDashEventsLogic

class WheeledDashMiscEvents(ClientEventsContainer, IWheeledDashEventsLogic):

    def __init__(self):
        super(WheeledDashMiscEvents, self).__init__()
        self.onImpulseStarted = self._createEvent()

    def _createEventsDebugger(self):
        return WheeledDashMiscEventsDebugger(self)


class WheeledDashMiscEventsDebugger(ClientEventsContainerDebugger):
    IGNORED_EVENTS = ClientEventsContainerDebugger.IGNORED_EVENTS + ('onImpulseStarted', )
    _EVENTS_DEBUG_PREFIX = 'WHEELED_DASH_MISC'
