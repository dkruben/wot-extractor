# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/common/fort_rush_common/cgf/capture_point.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/common/fort_rush_common/cgf/capture_point.py
from __future__ import absolute_import
import CGF, Triggers
from GenericComponents import Sequence
from cgf_script.registration import ComponentProperty

class FortRushCapturePointComponentDescr(object):
    category = 'CapturePoint'
    domain = CGF.Domain.All
    editorTitle = 'Capture Point Component'
    trigger = ComponentProperty(type=CGF.PropertyType.Link, editorName='AreaTrigger', value=Triggers.AreaTriggerComponent)
    sequence = ComponentProperty(type=CGF.PropertyType.Link, editorName='SequenceComponent', value=Sequence)
    capturablePointName = ComponentProperty(type=CGF.PropertyType.String, editorName='capturablePointName')
