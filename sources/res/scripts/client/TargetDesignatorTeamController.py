# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/TargetDesignatorTeamController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/TargetDesignatorTeamController.py
from __future__ import absolute_import
import logging, typing
from Math import Vector3
from chat_commands_consts import LocationMarkerSubType
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from typing import Set, Optional, Tuple
    from gui.battle_control.controllers.feedback_adaptor import BattleFeedbackAdaptor
    ClientMarkers = Set[Tuple[(int, int, Vector3, int, int)]]
_debug = logging.getLogger(__name__).debug
_UNSPOTTED_MARKER_HIT = LocationMarkerSubType.TARGET_DESIGNATOR_UNSPOTTED_MARKER_HIT

class TargetDesignatorTeamController(DynamicScriptComponent):
    session = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(TargetDesignatorTeamController, self).__init__()
        self.__markers = set()
        self.set_unspottedMarkers(None)
        return

    def onDestroy(self):
        super(TargetDesignatorTeamController, self).onDestroy()
        self.__updateMarkers(self.__markers, set())

    def set_unspottedMarkers(self, oldMarkers):
        oldMarkers = self.__markers
        self.__markers = newMarkers = set()
        for marker in self.unspottedMarkers:
            targetID = marker.targetID
            creatorID = marker.creatorID
            x, y, z, w = marker.point
            hitPoint = Vector3(x, y, z)
            hitMarkerID = hash(hitPoint)
            newMarkers.add((hitMarkerID, targetID, hitPoint, _UNSPOTTED_MARKER_HIT, creatorID))

        self.__updateMarkers(oldMarkers, newMarkers)

    def __updateMarkers(self, oldMarkers, newMarkers):
        feedback = self.session.shared.feedback
        markersToRemove = oldMarkers - newMarkers
        _debug('markersToRemove=%s', markersToRemove)
        for marker in markersToRemove:
            markerID = marker[0]
            feedback.onStaticMarkerRemoved(markerID)

        markersToAdd = newMarkers - oldMarkers
        _debug('markersToAdd=%s', markersToAdd)
        for markerID, targetID, point, subType, creatorID in markersToAdd:
            feedback.onStaticMarkerAdded(markerID, targetID, point, subType)
