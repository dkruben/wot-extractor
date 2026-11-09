# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/cgf_components_common/vehicle_mechanics/staged_jet_boosters.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/cgf_components_common/vehicle_mechanics/staged_jet_boosters.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class StagedJetBoostersControllerDescriptor(object):
    category = 'Vehicle Mechanics'
    editorTitle = 'Staged Jet Boosters Controller'
    domain = CGF.Domain.All
    left = ComponentProperty(CGF.PropertyType.Link, editorName='Left Rocket', value=CGF.GameObject)
    right = ComponentProperty(CGF.PropertyType.Link, editorName='Right Rocket', value=CGF.GameObject)
    stateController = ComponentProperty(CGF.PropertyType.Link, editorName='State Controller', value=CGF.GameObject)
