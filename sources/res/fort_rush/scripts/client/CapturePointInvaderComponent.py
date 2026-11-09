# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/CapturePointInvaderComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/CapturePointInvaderComponent.py
from __future__ import absolute_import
import logging
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from fort_rush.gui.shared.events import CaptureInvaderEvent
from script_component.DynamicScriptComponent import DynamicScriptComponent
_logger = logging.getLogger(__name__)

class CapturePointInvaderComponent(DynamicScriptComponent):

    def _onAvatarReady(self):
        vehicleID = self.entity.id
        baseName = (self.capturablePointName or '').upper()
        _logger.debug('[FORT_RUSH][INVADER] added vehicleID=%s base=%s', vehicleID, baseName)
        g_eventBus.handleEvent(CaptureInvaderEvent(CaptureInvaderEvent.INVADER_ADDED, vehicleID, baseName), EVENT_BUS_SCOPE.BATTLE)

    def onDestroy(self):
        vehicleID = self.entity.id
        baseName = (self.capturablePointName or '').upper()
        _logger.debug('[FORT_RUSH][INVADER] removed vehicleID=%s base=%s', vehicleID, baseName)
        g_eventBus.handleEvent(CaptureInvaderEvent(CaptureInvaderEvent.INVADER_REMOVED, vehicleID, baseName), EVENT_BUS_SCOPE.BATTLE)
        super(CapturePointInvaderComponent, self).onDestroy()
