# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/state_machine/machine.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/state_machine/machine.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.machine import BaseStateMachine
from gui.Scaleform.daapi.view.battle.pve_base.progress_counter.state_machine import states
from gui.Scaleform.daapi.view.battle.pve_base.progress_counter.state_machine import transitions

class ProgressCounterStateMachine(BaseStateMachine):

    def configure(self, view, widgetType, widgetId):
        initialState = states.InitialState()
        appearanceState = states.AppearanceState()
        regularState = states.RegularState()
        hiddenState = states.HiddenState()
        initialState.configure(view, widgetType, widgetId)
        appearanceState.configure(view, widgetType, widgetId)
        regularState.configure(view, widgetType, widgetId)
        hiddenState.configure(view, widgetType, widgetId)
        initialState.addTransition(transitions.ToAppearanceTransition(), target=appearanceState)
        initialState.addTransition(transitions.ToRegularTransition(), target=regularState)
        appearanceState.addTransition(transitions.ToRegularTransition(), target=regularState)
        appearanceState.addTransition(transitions.ToHiddenTransition(), target=hiddenState)
        regularState.addTransition(transitions.ToHiddenTransition(), target=hiddenState)
        self.addState(initialState)
        self.addState(appearanceState)
        self.addState(regularState)
        self.addState(hiddenState)
