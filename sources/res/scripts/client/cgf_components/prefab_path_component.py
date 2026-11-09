# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/prefab_path_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/prefab_path_component.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import registerComponent, ComponentProperty

@registerComponent
class PyPrefabPathComponent(object):
    domain = CGF.Domain.ClientEditor
    editorTitle = 'PyPrefab path component'
    category = 'Common'
    vseVisible = False
    prefabPath = ComponentProperty(type=CGF.PropertyType.String, value='', editorName='prefab path', annotations={'path': '*.prefab'})
