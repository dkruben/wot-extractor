# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_components_common/state_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/state_components.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from GenericComponents import StateSwitcherComponent
_DEFAULT_HEALTH = 300

class DEATH_REASON(object):
    UNKNOWN = 0
    DESTROYED = 1


class DeathComponentDescriptor(object):
    category = 'Common'
    editorTitle = 'Death Component'


class HealthComponentDescriptor(object):
    category = 'Common'
    editorTitle = 'Health Component'
    maxHealth = ComponentProperty(type=CGF.PropertyType.Int, editorName='MaxHealth', value=_DEFAULT_HEALTH)
    health = ComponentProperty(type=CGF.PropertyType.Int, editorName='CurrentHealth', value=_DEFAULT_HEALTH)


@registerComponent
class RemoveOnDeathComponent(object):
    category = 'Death'
    editorTitle = 'Remove On Death Component'
    domain = CGF.Domain.All
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName='Delay', value=0.0)


@registerComponent
class SpawnOnDeathComponent(object):
    category = 'Death'
    editorTitle = 'Spawn On Death Component'
    domain = CGF.Domain.All
    prefabPath = ComponentProperty(type=CGF.PropertyType.String, editorName='Spawn Prefab', annotations={'path': '*.prefab'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName='Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGF.PropertyType.Bool, editorName='Attach to GO', value=True)


@registerComponent
class VehicleHealthObserverComponent(object):
    category = 'Common'
    editorTitle = 'Vehicle Health Observer Component'
    domain = CGF.Domain.All
    state = ComponentProperty(type=CGF.PropertyType.Int, editorName='State', value=StateSwitcherComponent.NORMAL_STATE, annotations={'comboBox': {'None': (str(StateSwitcherComponent.NONE_STATE)), 
                    'Normal': (str(StateSwitcherComponent.NORMAL_STATE)), 
                    'Damaged': (str(StateSwitcherComponent.DAMAGED_STATE)), 
                    'Critical': (str(StateSwitcherComponent.CRITICAL_STATE))}})
