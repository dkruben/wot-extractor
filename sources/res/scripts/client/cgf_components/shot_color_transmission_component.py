# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/shot_color_transmission_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/shot_color_transmission_component.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class ShotColorTransmissionComponent(object):
    editorTitle = 'Gun Shot Effect Component'
    category = 'Animator Triggers'
    domain = CGF.Domain.ClientEditor
    materialParam = ComponentProperty(type=CGF.PropertyType.String, editorName='material property', value='TintColor')
    startValue = ComponentProperty(type=CGF.PropertyType.Float, editorName='start value', value=0.0)
    endValue = ComponentProperty(type=CGF.PropertyType.Float, editorName='end value', value=0.5)
