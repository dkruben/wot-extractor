# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_components_common/material_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/material_component.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent
from material_kinds import EFFECT_MATERIALS

@registerComponent
class MaterialComponent(object):
    category = 'Material'
    editorTitle = 'Material'
    domain = CGF.Domain.All
    materials = {m: m for m in EFFECT_MATERIALS}
    kind = ComponentProperty(type=CGF.PropertyType.String, editorName='Kind', value='', annotations={'comboBox': materials})
