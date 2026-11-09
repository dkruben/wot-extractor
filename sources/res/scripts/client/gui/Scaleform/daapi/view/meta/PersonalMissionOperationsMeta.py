# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionOperationsMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionOperationsMeta.py
from gui.Scaleform.framework.entities.View import View

class PersonalMissionOperationsMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def onOperationClick(self, pmType, operationID):
        self._printOverrideError('onOperationClick')

    def showInfo(self):
        self._printOverrideError('showInfo')

    def as_setOperationsS(self, operations):
        if self._isDAAPIInited():
            return self.flashObject.as_setOperations(operations)

    def as_setTitleS(self, titleVO):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(titleVO)
