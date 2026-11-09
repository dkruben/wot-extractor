# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_components_common/vehicle_mechanics/custom_rotation_point.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/vehicle_mechanics/custom_rotation_point.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class CustomRotationPointComponent(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Custom Rotation Point Component'
    domain = CGF.Domain.All
    minSpeed = ComponentProperty(type=CGF.PropertyType.Int, editorName='Min speed bound (m/s)', value=0)
    minPoints = ComponentProperty(type=CGF.PropertyType.Vector3List, editorName='Min points (left, right)', value=[])
    maxSpeed = ComponentProperty(type=CGF.PropertyType.Int, editorName='Max speed bound (m/s)', value=0)
    maxPoints = ComponentProperty(type=CGF.PropertyType.Vector3List, editorName='Max points (left, right)', value=[])
    changeRailDirection = ComponentProperty(type=CGF.PropertyType.Bool, editorName='Change rail direction', value=False)

    def __init__(self):
        self.physicsRef = None
        self.originGimletCOMOffset = None
        self.originRailCOMOffset = None
        return
