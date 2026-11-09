# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pet_system_common/EventConfig.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pet_system_common/EventConfig.py
from __future__ import absolute_import
import typing
from pet_system_common.pet_constants import PetEventsConsts as pc, PetEventTypeConsts as eventTypes
if typing.TYPE_CHECKING:
    from typing import Dict

class EventConfig(object):

    def __init__(self, config):
        self._config = config

    def getEvents(self):
        return self._config

    def getEventById(self, eventID):
        return self._config.get(eventID, {})

    def getEventType(self, eventID):
        return self.getEventById(eventID).get(pc.EVENT_TYPE, eventTypes.BASIC)

    def getEventRewardID(self, eventID):
        return self.getEventById(eventID).get(pc.EVENT_REWARD, 0)
