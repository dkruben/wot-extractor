# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineRespawnViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineRespawnViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FrontlineRespawnViewMeta(BaseDAAPIComponent):

    def onLocationSelected(self, pointIdx):
        self._printOverrideError('onLocationSelected')

    def onRespawnBtnClick(self):
        self._printOverrideError('onRespawnBtnClick')

    def onDeploymentReady(self):
        self._printOverrideError('onDeploymentReady')

    def as_updateTimerS(self, timeIsOver, mainTimer):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(timeIsOver, mainTimer)

    def as_updateAutoTimerS(self, timeIsOver, mainTimer):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAutoTimer(timeIsOver, mainTimer)

    def as_resetRespawnStateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetRespawnState()

    def as_setSelectedLocationS(self, pointIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedLocation(pointIdx)

    def as_setLaneStateS(self, laneId, value, blockReasonText):
        if self._isDAAPIInited():
            return self.flashObject.as_setLaneState(laneId, value, blockReasonText)

    def as_setMapDimensionsS(self, mapWidth, mapHeight):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapDimensions(mapWidth, mapHeight)

    def as_setRespawnLocationsS(self, locations):
        if self._isDAAPIInited():
            return self.flashObject.as_setRespawnLocations(locations)

    def as_handleAsReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleAsReplay()
