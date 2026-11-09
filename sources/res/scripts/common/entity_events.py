# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/entity_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/entity_events.py
from __future__ import absolute_import
import typing, weakref
from events_handler import EventsHandler
from events_container import EventsContainer
from debug_utils import LOG_ERROR
from constants import IS_DEVELOPMENT
if typing.TYPE_CHECKING:
    import BigWorld
    from Event import SafeEvent

class EntityEventsCoreIntegration(EventsHandler):

    def __init__(self, entity):
        super(EntityEventsCoreIntegration, self).__init__()
        self.spaceID = entity.spaceID
        self.entityID = entity.id
        self.entityGO = entity.entityGameObject


class EntityEvents(EventsContainer):
    __slots__ = ('onDynComponentGroupAdded', 'onDynComponentGroupRemoved', '_entityRef')

    def __init__(self, entity=None):
        super(EntityEvents, self).__init__()
        self._entityRef = weakref.ref(entity) if entity else None
        self.onDynComponentGroupAdded = self._createEvent()
        self.onDynComponentGroupRemoved = self._createEvent()
        return

    def createEvent(self):
        return self._createEvent()

    def _createCoreIntegration(self):
        entity = self._entityRef() if self._entityRef else None
        if entity is None or entity.entityGameObject is None or not entity.entityGameObject.valid:
            LOG_ERROR('[EntityEvents] Could not create core integration. Entity is not ready or already destroyed.')
            return
        else:
            integration = self._createIntegrationInstance(entity)
            if integration is None:
                LOG_ERROR('[EntityEvents] Could not create core integration. Core integration object not provided.')
                return
            integration.subscribeTo(self, raiseException=IS_DEVELOPMENT)
            return integration

    def _createIntegrationInstance(self, entity):
        return
