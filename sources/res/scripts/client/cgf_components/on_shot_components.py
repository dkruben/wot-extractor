# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/on_shot_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/on_shot_components.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class EffectOnShotComponent(object):
    group = 'Shooting'
    editorTitle = 'Effect On Shot'
    domain = CGF.Domain.ClientEditor
    effectPath = ComponentProperty(type=CGF.PropertyType.String, editorName='Effect Prefab', annotations={'path': '*.prefab'})


@registerComponent
class SoundOnShotComponent(object):
    group = 'Shooting'
    editorTitle = 'Sound On Shot'
    domain = CGF.Domain.ClientEditor
    soundPath = ComponentProperty(type=CGF.PropertyType.String, editorName='Sound Prefab', annotations={'path': '*.prefab'})
