# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/hover_group_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/hover_group_components.py
from __future__ import absolute_import
import CGF, SoundGroups
from cgf_script.registration import ComponentProperty, registerComponent
from cgf_components.hover_component import IsHoveredComponent, HoverGroupTrackerComponent

@registerComponent
class HoverableComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'Hoverable'
    group = 'Common'
    groupTracker = ComponentProperty(type=CGF.PropertyType.Link, editorName='Group tracker', value=HoverGroupTrackerComponent)


@registerComponent
class HoverSoundComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'Hover group sound'
    group = 'Common'
    hoverAddingSound = ComponentProperty(type=CGF.PropertyType.String, editorName='Hover adding sound', value='')
    hoverRemovingSound = ComponentProperty(type=CGF.PropertyType.String, editorName='Hover removing sound', value='')


class HoverGroupSystem(CGF.System):
    HoverableActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(HoverableComponent), CGF.ReactHas(IsHoveredComponent))
    HoverableDeactivated = CGF.DeactivateReaction(CGF.GameObject, CGF.ReactRw(HoverableComponent), CGF.ReactHas(IsHoveredComponent))
    HoverSoundActivated = CGF.ActivateReaction(CGF.ReactRo(HoverSoundComponent), CGF.ReactHas(IsHoveredComponent))
    HoverSoundDeactivated = CGF.DeactivateReaction(CGF.ReactRo(HoverSoundComponent), CGF.ReactHas(IsHoveredComponent))
    HoverGroupTrackerAccess = CGF.AccessReaction(CGF.Ro(HoverGroupTrackerComponent))
    Reactions = CGF.Reactions(HoverableActivated, HoverableDeactivated, HoverSoundActivated, HoverSoundDeactivated, HoverGroupTrackerAccess)

    def update(self):
        hoverGroupTrackerAccess = self.reaction(self.HoverGroupTrackerAccess)
        for gameObject, hoverableComponent in self.reaction(self.HoverableDeactivated):
            self.onHoverRemoved(hoverableComponent, gameObject, hoverGroupTrackerAccess)

        for hoverSound in self.reaction(self.HoverSoundDeactivated):
            self.onHoverSoundRemoved(hoverSound)

        for gameObject, hoverableComponent in self.reaction(self.HoverableActivated):
            self.onHoverAdded(hoverableComponent, gameObject, hoverGroupTrackerAccess)

        for hoverSound in self.reaction(self.HoverSoundActivated):
            self.onHoverSoundAdded(hoverSound)

    def onHoverAdded(self, hoverableComponent, gameObject, hoverGroupTrackerAccess):
        groupTracker = hoverGroupTrackerAccess.find(hoverableComponent.groupTracker)
        if groupTracker:
            groupTracker.addHoveredGO(gameObject)

    def onHoverRemoved(self, hoverableComponent, gameObject, hoverGroupTrackerAccess):
        groupTracker = hoverGroupTrackerAccess.find(hoverableComponent.groupTracker)
        if groupTracker:
            groupTracker.removeHoveredGO(gameObject)

    def onHoverSoundAdded(self, hoverSound):
        if hoverSound.hoverAddingSound:
            SoundGroups.g_instance.playSound2D(hoverSound.hoverAddingSound)

    def onHoverSoundRemoved(self, hoverSound):
        if hoverSound.hoverRemovingSound:
            SoundGroups.g_instance.playSound2D(hoverSound.hoverRemovingSound)
