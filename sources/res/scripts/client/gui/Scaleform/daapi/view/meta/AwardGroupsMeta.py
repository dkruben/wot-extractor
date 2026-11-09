# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/AwardGroupsMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AwardGroupsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AwardGroupsMeta(BaseDAAPIComponent):

    def showGroup(self, groupId):
        self._printOverrideError('showGroup')

    def as_setDataS(self, groups):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(groups)

    def as_setTooltipsS(self, tooltips):
        if self._isDAAPIInited():
            return self.flashObject.as_setTooltips(tooltips)

    def as_setSelectedS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelected(id, value)

    def as_setEnabledS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(id, value)
