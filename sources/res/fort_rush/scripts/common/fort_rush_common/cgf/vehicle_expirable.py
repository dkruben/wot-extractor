# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/common/fort_rush_common/cgf/vehicle_expirable.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/common/fort_rush_common/cgf/vehicle_expirable.py
from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class VehicleExpirableComponentDescriptor(object):
    category = 'Expirable'
    editorTitle = 'Vehicle Expirable Component'
    domain = CGF.Domain.All
    duration = ComponentProperty(CGF.PropertyType.Float, editorName='Duration', value=0.0)
