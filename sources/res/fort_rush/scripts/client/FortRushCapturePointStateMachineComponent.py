# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/FortRushCapturePointStateMachineComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/FortRushCapturePointStateMachineComponent.py
from __future__ import absolute_import
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent
from fort_rush_common.fort_rush_constants import CaptureStates

class FortRushCapturePointStateMachineComponent(ReplicableDynamicScriptComponent):

    def __init__(self):
        super(FortRushCapturePointStateMachineComponent, self).__init__()
        self.state = CaptureStates.NEUTRAL.value
