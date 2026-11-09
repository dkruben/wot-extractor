# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/common/story_mode_common/cgf_components_common/bunkers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/common/story_mode_common/cgf_components_common/bunkers.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty
from constants import ATTACK_REASON

class BunkerLogicComponentDescriptor(object):
    category = 'Bunker'
    editorTitle = 'Bunker Logic'
    domain = CGF.Domain.All
    destructibleEntityId = ComponentProperty(type=CGF.PropertyType.Int, editorName='Destructible Entity ID', value=0)
    transitionChild = ComponentProperty(type=CGF.PropertyType.Link, editorName='Transition', value=CGF.GameObject)
    destroyedChild = ComponentProperty(type=CGF.PropertyType.Link, editorName='Destroyed', value=CGF.GameObject)
    markerDistance = ComponentProperty(type=CGF.PropertyType.Int, editorName='Marker max distance', value=300)
    resistAttackReasons = ComponentProperty(type=CGF.PropertyType.StringList, editorName='Resist Attack Reasons', value=(
     ATTACK_REASON.RAM,
     ATTACK_REASON.BATTLESHIP,
     ATTACK_REASON.DESTROYER))
