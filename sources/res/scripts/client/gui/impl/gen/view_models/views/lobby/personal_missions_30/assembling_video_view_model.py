# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/assembling_video_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/assembling_video_view_model.py
from frameworks.wulf import ViewModel

class AssemblingVideoViewModel(ViewModel):
    __slots__ = ('startAssembling', )

    def __init__(self, properties=2, commands=1):
        super(AssemblingVideoViewModel, self).__init__(properties=properties, commands=commands)

    def getOperationID(self):
        return self._getNumber(0)

    def setOperationID(self, value):
        self._setNumber(0, value)

    def getStageNumber(self):
        return self._getNumber(1)

    def setStageNumber(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(AssemblingVideoViewModel, self)._initialize()
        self._addNumberProperty('operationID', 0)
        self._addNumberProperty('stageNumber', 0)
        self.startAssembling = self._addCommand('startAssembling')
