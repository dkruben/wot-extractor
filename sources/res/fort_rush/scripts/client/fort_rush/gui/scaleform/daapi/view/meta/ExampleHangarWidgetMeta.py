# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/meta/ExampleHangarWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/meta/ExampleHangarWidgetMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ExampleHangarWidgetMeta(BaseDAAPIComponent):

    def as_showSomeDataS(self, message, iconSource):
        if self._isDAAPIInited():
            return self.flashObject.as_showSomeData(message, iconSource)

    def as_setVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibility(isVisible)
