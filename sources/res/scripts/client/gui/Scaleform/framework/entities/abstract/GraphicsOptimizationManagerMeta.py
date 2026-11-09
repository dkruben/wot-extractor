# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/entities/abstract/GraphicsOptimizationManagerMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GraphicsOptimizationManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GraphicsOptimizationManagerMeta(BaseDAAPIComponent):

    def registerOptimizationArea(self, x, y, width, height):
        self._printOverrideError('registerOptimizationArea')

    def unregisterOptimizationArea(self, optimizationID):
        self._printOverrideError('unregisterOptimizationArea')

    def updateOptimizationArea(self, optimizationID, x, y, width, height):
        self._printOverrideError('updateOptimizationArea')

    def isOptimizationAvailable(self, alias):
        self._printOverrideError('isOptimizationAvailable')

    def isOptimizationEnabled(self, alias):
        self._printOverrideError('isOptimizationEnabled')

    def switchOptimizationEnabled(self, value):
        self._printOverrideError('switchOptimizationEnabled')

    def as_invalidateRectanglesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_invalidateRectangles()

    def as_switchOptimizationEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_switchOptimizationEnabled(value)
