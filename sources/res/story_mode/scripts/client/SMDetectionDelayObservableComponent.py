# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/SMDetectionDelayObservableComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/SMDetectionDelayObservableComponent.py
from __future__ import absolute_import
from future.utils import viewitems
from Event import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent
from story_mode_common.story_mode_constants import AwarenessState

class SMDetectionDelayObservableComponent(DynamicScriptComponent):
    onTimersChange = Event()
    onAwarenessStateChanged = Event()

    def __init__(self):
        super(SMDetectionDelayObservableComponent, self).__init__()
        self.timers = {}
        self._state = AwarenessState.NOT_SPOTTED

    def set_timers(self, prevValues):
        self.onTimersChange(prevValues, self.timers)
        if self.timers:
            state = AwarenessState.SPOTTING
        else:
            state = AwarenessState.NOT_SPOTTED
        for key, value in viewitems(self.timers):
            if key not in prevValues:
                if value['spotted']:
                    state = AwarenessState.SPOTTED
            elif not prevValues[key]['spotted'] and value['spotted']:
                state = AwarenessState.SPOTTED

        if state != self._state:
            if not (self._state == AwarenessState.SPOTTED and state == AwarenessState.SPOTTING):
                self._state = state
                self.onAwarenessStateChanged(self._state.value)
