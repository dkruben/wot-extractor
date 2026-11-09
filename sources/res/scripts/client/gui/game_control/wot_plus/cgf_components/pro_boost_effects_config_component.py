# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_control/wot_plus/cgf_components/pro_boost_effects_config_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_control/wot_plus/cgf_components/pro_boost_effects_config_component.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerComponent, ComponentProperty

@registerComponent
class ProBoostEffectsConfigComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'Pro Boost Effects Config'
    category = 'Hangar'
    vseVisible = False
    activationPrefab = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='Activation prefab', annotations={'path': '*.prefab'})
    deactivationPrefab = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='Deactivation prefab', annotations={'path': '*.prefab'})
