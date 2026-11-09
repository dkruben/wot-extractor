# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/events_containers/components/life_cycle/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/events_containers/components/life_cycle/__init__.py
from __future__ import absolute_import
import typing
from events_containers.common.container_wrappers import activateEventsContainer
from events_containers.components.life_cycle.events import ComponentLifeCycleEvents
from events_containers.components.life_cycle.interfaces import ILifeCycleComponent, IComponentLifeCycleEvents, IComponentLifeCycleListener, IComponentLifeCycleListenerLogic
__all__ = ('ILifeCycleComponent', 'IComponentLifeCycleEvents', 'IComponentLifeCycleListener',
           'IComponentLifeCycleListenerLogic', 'ComponentLifeCycleEvents', 'isLifeCycleComponent',
           'createComponentLifeCycleEvents')

def isLifeCycleComponent(component):
    return isinstance(component, ILifeCycleComponent)


@activateEventsContainer()
def createComponentLifeCycleEvents(component, **_):
    return ComponentLifeCycleEvents(component)
