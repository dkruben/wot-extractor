# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ColorSettingsViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ColorSettingsViewMeta.py
from gui.Scaleform.framework.entities.View import View

class ColorSettingsViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onApply(self, diff):
        self._printOverrideError('onApply')

    def onReset(self):
        self._printOverrideError('onReset')

    def onSettingsChange(self, settingName, settingValue):
        self._printOverrideError('onSettingsChange')

    def onTabSelected(self, selectedTab):
        self._printOverrideError('onTabSelected')

    def setViewWidth(self, value):
        self._printOverrideError('setViewWidth')

    def moveSpace(self, x, y, delta):
        self._printOverrideError('moveSpace')

    def as_initDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initData(data)

    def as_updateDataS(self, selectedTab, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateData(selectedTab, data)
