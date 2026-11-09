# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/VisualScriptCache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/VisualScriptCache.py
from __future__ import absolute_import
import BigWorld
from visual_script.misc import ASPECT
from visual_script.multi_plan_provider import MultiPlanCache

class VisualScriptCache(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(VisualScriptCache, self).__init__()
        self._multiPlanCache = MultiPlanCache(ASPECT.CLIENT)

    def _destroy(self):
        if self._multiPlanCache:
            self._multiPlanCache.destroy()
            self._multiPlanCache = None
        return

    def onLeaveWorld(self):
        self._destroy()

    def onDestroy(self):
        self._destroy()

    def getPlan(self, componentName, planNames):
        return self._multiPlanCache.getPlan(componentName, planNames)
