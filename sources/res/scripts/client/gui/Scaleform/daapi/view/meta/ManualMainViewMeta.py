# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ManualMainViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ManualMainViewMeta.py
from gui.Scaleform.framework.entities.View import View

class ManualMainViewMeta(View):

    def onChapterOpenedS(self, id):
        self._printOverrideError('onChapterOpenedS')

    def closeView(self):
        self._printOverrideError('closeView')

    def onBackButton(self):
        self._printOverrideError('onBackButton')

    def as_setChaptersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setChapters(data)

    def as_setPageBackgroundS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPageBackground(value)

    def as_showCloseBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showCloseBtn(value)

    def as_showBackBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBackBtn(value)

    def as_setDescrLabelBackBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescrLabelBackBtn(value)
