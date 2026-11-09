# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/lobby_state_machine/resource_mapping.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/lobby_state_machine/resource_mapping.py
from __future__ import absolute_import
import logging, typing
from gui.impl import backport
from gui.lobby_state_machine.states import LobbyState
_logger = logging.getLogger(__name__)
_RESOURCE_LAYOUT_TO_STATE_ID_MAPPING = {}
_STATE_ID_TO_RESOURCE_ID_MAPPING = {}

def mappedToResourceId(resourceAccessor):

    def decorator(stateCls):
        resourceId = resourceAccessor()
        resourceLayout = backport.layout(resourceId)
        existingResIdMapping = _STATE_ID_TO_RESOURCE_ID_MAPPING.get(stateCls.STATE_ID)
        _RESOURCE_LAYOUT_TO_STATE_ID_MAPPING[resourceLayout] = stateCls.STATE_ID
        _STATE_ID_TO_RESOURCE_ID_MAPPING[stateCls.STATE_ID] = resourceId
        _logger.info('%s was mapped to %s (0x%x)', stateCls.STATE_ID, resourceLayout, resourceId)
        return stateCls

    return decorator


def stateIdToResId(stateId):
    return _STATE_ID_TO_RESOURCE_ID_MAPPING.get(stateId)


def stateIdToResLayout(stateId):
    resId = _STATE_ID_TO_RESOURCE_ID_MAPPING.get(stateId)
    if resId is None:
        return resId
    else:
        return backport.layout(resId)


def resIdToStateId(resId):
    return resLayoutToStateId(backport.layout(resId))


def resLayoutToStateId(resLayout):
    return _RESOURCE_LAYOUT_TO_STATE_ID_MAPPING.get(resLayout)
