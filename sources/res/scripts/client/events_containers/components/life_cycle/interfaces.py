# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/events_containers/components/life_cycle/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/events_containers/components/life_cycle/interfaces.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener

class ILifeCycleComponent(object):

    @property
    def lifeCycleEvents(self):
        raise NotImplementedError

    def getComponentParams(self):
        return


class IComponentLifeCycleEventsLogic(object):
    onComponentAvatarReady = None
    onComponentParamsCollected = None
    onComponentAppearanceReady = None
    onComponentAppearanceReset = None
    onComponentDestroyed = None

    def processComponentAvatarReady(self):
        raise NotImplementedError

    def processAppearanceReady(self):
        raise NotImplementedError

    def processAppearanceReset(self):
        raise NotImplementedError

    def processParamsCollected(self):
        raise NotImplementedError


class IComponentLifeCycleEvents(IClientEventsContainer, IComponentLifeCycleEventsLogic):
    pass


class IComponentLifeCycleListenerLogic(object):

    def onComponentAvatarReady(self, component):
        pass

    def onComponentParamsCollected(self, params):
        pass

    def onComponentAppearanceReady(self, component):
        pass

    def onComponentAppearanceReset(self, component):
        pass

    def onComponentDestroyed(self, component):
        pass


class IComponentLifeCycleListener(IClientEventsContainerListener, IComponentLifeCycleListenerLogic):
    pass
