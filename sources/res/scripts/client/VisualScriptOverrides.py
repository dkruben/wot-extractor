# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/VisualScriptOverrides.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/VisualScriptOverrides.py
from __future__ import absolute_import
from copy import copy
import BigWorld

class VisualScriptOverrides(BigWorld.DynamicScriptComponent):

    def updateParams(self, planDefs):
        if not self.params:
            return planDefs
        result = []
        for planDef in planDefs:
            planName = planDef['name']
            planOverrides = self.params.get(planName)
            if planOverrides:
                planDef = copy(planDef)
                oldParams = planDef.get('params', {})
                newParams = copy(oldParams)
                newParams.update(planOverrides)
                planDef['params'] = newParams
            result.append(planDef)

        return result
