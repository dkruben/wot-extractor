# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/wheeled_dash/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/generic_mechanics/wheeled_dash/__init__.py
from __future__ import absolute_import
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.mechanics.generic_mechanics.wheeled_dash.mechanic_interfaces import IWheeledDashListenerLogic, IWheeledDashEvents
from vehicles.mechanics.generic_mechanics.wheeled_dash.mechanic_events import WheeledDashMiscEvents
__all__ = ('IWheeledDashListenerLogic', 'IWheeledDashEvents', 'createWheeledDashMiscEvents')

@activateEventsContainer()
def createWheeledDashMiscEvents():
    return WheeledDashMiscEvents()
