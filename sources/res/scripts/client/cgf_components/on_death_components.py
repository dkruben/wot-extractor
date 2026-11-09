# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/on_death_components.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/on_death_components.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class ChangeModelOnDeathComponent(object):
    group = 'Death'
    editorTitle = 'Change Model On Death'
    domain = CGF.Domain.ClientEditor
    modelPath = ComponentProperty(type=CGF.PropertyType.String, editorName='Model path', annotations={'path': '*.model'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName='Delay', value=0.0)

    def __init__(self):
        self.initialModel = None
        return


@registerComponent
class SoundOnDeathComponent(object):
    group = 'Death'
    editorTitle = 'Sound On Death'
    domain = CGF.Domain.ClientEditor
    soundPath = ComponentProperty(type=CGF.PropertyType.String, editorName='Sound Prefab', annotations={'path': '*.prefab'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName='Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGF.PropertyType.Bool, editorName='Attach to GO', value=True)


@registerComponent
class EffectOnDeathComponent(object):
    group = 'Death'
    editorTitle = 'Effect On Death'
    domain = CGF.Domain.ClientEditor
    effectPath = ComponentProperty(type=CGF.PropertyType.String, editorName='Effect Prefab', annotations={'path': '*.prefab'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName='Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGF.PropertyType.Bool, editorName='Attach to GO', value=True)
