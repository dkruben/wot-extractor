# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/trigger_vse_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/trigger_vse_component.py
from __future__ import absolute_import
import CGF, Event
from GenericComponents import VSEComponent
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class TriggerVSEComponent(object):
    editorTitle = 'Trigger VSE'
    domain = CGF.Domain.ClientEditor
    eventName = ComponentProperty(type=CGF.PropertyType.String, editorName='event name', value='event')

    def __init__(self):
        super(TriggerVSEComponent, self).__init__()
        self.triggerEvent = Event.Event()


class TriggerVisualScriptComponentsSystem(CGF.System):
    TriggerActivated = CGF.ActivateReaction(CGF.ReactRw(TriggerVSEComponent), VSEComponent)
    TriggerDeactivated = CGF.DeactivateReaction(CGF.ReactRw(TriggerVSEComponent), VSEComponent)
    Reactions = CGF.Reactions(TriggerActivated, TriggerDeactivated)

    def update(self):
        for trigger, vse in self.reaction(self.TriggerDeactivated):
            trigger.triggerEvent -= vse.context.onTriggerEvent

        for trigger, vse in self.reaction(self.TriggerActivated):
            self.doAction(trigger.eventName)
            trigger.triggerEvent += vse.context.onTriggerEvent
