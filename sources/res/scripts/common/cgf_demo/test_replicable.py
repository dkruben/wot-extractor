# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_demo/test_replicable.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_demo/test_replicable.py
from __future__ import absolute_import
import Math, CGF
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.registration import ComponentProperty

class TestReplicableComponentDescriptor(object):
    category = DEMO_CATEGORY
    editorTitle = 'Test Replication Types'
    replicableInt = ComponentProperty(type=CGF.PropertyType.Int, editorName='IntValue', value=777)
    replicableFloat = ComponentProperty(type=CGF.PropertyType.Float, editorName='Float Value', value=10.0)
    replicableString = ComponentProperty(type=CGF.PropertyType.String, editorName='States', value='Test String')
    replicableVector3 = ComponentProperty(type=CGF.PropertyType.Vector3, editorName='States', value=Math.Vector3(1.0, 2.0, 3.0))
    replicableStringList = ComponentProperty(type=CGF.PropertyType.StringList, editorName='States', value=('one',
                                                                                                           'two',
                                                                                                           'three'))
    assetIndex = ComponentProperty(type=CGF.PropertyType.Int, editorName='Default asset', value=0)
    assets = ComponentProperty(type=CGF.PropertyType.StringList, editorName='Models')
