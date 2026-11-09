# wot-extractor: codigo DESCOMPILADO de sources/res/event_platform/scripts/common/event_platform_common/respawns/respawn_timer_component_descriptors.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: event_platform/scripts/common/event_platform_common/respawns/respawn_timer_component_descriptors.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class IndividualRespawnTimerComponentDescr(object):
    category = 'Respawns'
    editorTitle = 'IndividualRespawnTimerComponent'
    domain = CGF.Domain.All
    respawnDelay = ComponentProperty(type=CGF.PropertyType.Int, editorName='respawnDelay', value=1)
    timeOfDeath = ComponentProperty(type=CGF.PropertyType.Float, editorName='timeOfDeath', value=0.0)
