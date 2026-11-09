# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_components_common/vehicle_mechanics/crest_moving_sequence_params_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/vehicle_mechanics/crest_moving_sequence_params_component.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class CrestMovingSequenceParamsComponent(object):
    category = 'Sequence'
    editorTitle = 'Crest moving sequence params'
    domain = CGF.Domain.All
    sequence0PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName='Sequence 0 position layer', value='')
    sequence1PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName='Sequence 1 position layer', value='')
    sequence2PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName='Sequence 2 position layer', value='')
    sequence3PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName='Sequence 3 position layer', value='')
