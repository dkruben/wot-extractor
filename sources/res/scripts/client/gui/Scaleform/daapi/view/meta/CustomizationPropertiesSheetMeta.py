# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/CustomizationPropertiesSheetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CustomizationPropertiesSheetMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationPropertiesSheetMeta(BaseDAAPIComponent):

    def onActionBtnClick(self, actionType, actionData):
        self._printOverrideError('onActionBtnClick')

    def elementControlsHide(self):
        self._printOverrideError('elementControlsHide')

    def onClose(self):
        self._printOverrideError('onClose')

    def registerInscriptionController(self, inscriptionController, inputLines):
        self._printOverrideError('registerInscriptionController')

    def as_setDataAndShowS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDataAndShow(data)

    def as_setArrowsStatesS(self, left, right):
        if self._isDAAPIInited():
            return self.flashObject.as_setArrowsStates(left, right)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
