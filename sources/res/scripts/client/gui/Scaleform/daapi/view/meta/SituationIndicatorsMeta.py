# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/SituationIndicatorsMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SituationIndicatorsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SituationIndicatorsMeta(BaseDAAPIComponent):

    def as_setPerksS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_setPerks(items)

    def as_updatePerkS(self, perkName, state, duration, lifeTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePerk(perkName, state, duration, lifeTime)

    def as_setWeatherS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_setWeather(items)

    def as_updateWeatherS(self, weatherName, state, toolTip):
        if self._isDAAPIInited():
            return self.flashObject.as_updateWeather(weatherName, state, toolTip)

    def as_clearPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearPanel()

    def as_replayPauseS(self, isPaused):
        if self._isDAAPIInited():
            return self.flashObject.as_replayPause(isPaused)
