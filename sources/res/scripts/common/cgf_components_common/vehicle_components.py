# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_components_common/vehicle_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/vehicle_components.py
from __future__ import absolute_import
import CGF, Triggers
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class VehicleDestroyingComponent(object):
    category = 'Vehicle'
    editorTitle = 'Vehicle Destroying Component'
    domain = CGF.Domain.ServerEditor
    trigger = ComponentProperty(type=CGF.PropertyType.Link, editorName='AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.reactionID = None
        return


@registerComponent
class VehicleDamageLoggerComponent(object):
    category = 'Loggers'
    editorTitle = 'Vehicle Damage Logger Component'
    domain = CGF.Domain.ServerEditor

    def __init__(self):
        self.topMostParentName = None
        return


@registerComponent
class VehicleSequenceParamsAttachedComponent(object):
    category = 'Vehicle'
    editorTitle = 'Vehicle Sequence Params Attached Component'
    domain = CGF.Domain.All
