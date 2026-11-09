# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/visual_script_client/vse_client_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/vse_client_helpers.py
from __future__ import absolute_import
import BigWorld

def runPlan(entity, planName, params, key='', contextName=''):
    player = BigWorld.player()
    if player is not None:
        arena = player.arena
        if arena is not None:
            context = None
            if contextName:
                if entity and hasattr(entity, 'getVseContextInstance'):
                    context = entity.getVseContextInstance(contextName)
                else:
                    context = arena.getVseContextInstance(contextName)
            arena.runVsePlan(planName, params, key, context)
    return


def stopPlan(planName, key=''):
    player = BigWorld.player()
    if player is not None:
        arena = player.arena
        if arena is not None:
            arena.stopVsePlan(planName, key)
    return
