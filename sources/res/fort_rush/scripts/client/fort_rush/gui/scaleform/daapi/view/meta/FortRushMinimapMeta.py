# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/meta/FortRushMinimapMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/meta/FortRushMinimapMeta.py
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent

class FortRushMinimapMeta(ClassicMinimapComponent):

    def onZoneClicked(self, zoneName):
        self._printOverrideError('onZoneClicked')

    def as_showZonePingS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_showZonePing(zoneName)

    def as_showZoneCommitS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_showZoneCommit(zoneName)

    def as_clearZonePingS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_clearZonePing(zoneName)

    def as_updateZoneCaptureStateS(self, zoneName, ownerTeam, progressTeam, captureActive, isContested, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateZoneCaptureState(zoneName, ownerTeam, progressTeam, captureActive, isContested, progress)
