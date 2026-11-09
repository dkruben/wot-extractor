# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/serializable_types/customizations/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/serializable_types/customizations/__init__.py
from __future__ import absolute_import
from serialization import parseCompDescr
from serialization.serializable_component import SerializableComponentChildType
from .attachment import AttachmentComponent
from .camouflage import CamouflageComponent
from .customization_outfit import CustomizationOutfit, getAllItemsFromOutfit
from .decal import DecalComponent
from .insignia import InsigniaComponent
from .paint import PaintComponent
from .personal_number import PersonalNumberComponent
from .projection_decal import ProjectionDecalComponent
from .sequence import SequenceComponent
from .stat_tracker import StatTrackerComponent
__all__ = ('AttachmentComponent', 'CamouflageComponent', 'CustomizationOutfit', 'getAllItemsFromOutfit',
           'DecalComponent', 'InsigniaComponent', 'PaintComponent', 'PersonalNumberComponent',
           'ProjectionDecalComponent', 'SequenceComponent', 'StatTrackerComponent',
           'CUSTOMIZATION_CLASSES', 'parseC11sComponentDescr')
CUSTOMIZATION_CLASS_LIST = [
 AttachmentComponent, 
 CamouflageComponent, 
 CustomizationOutfit, 
 DecalComponent, 
 InsigniaComponent, 
 PaintComponent, 
 PersonalNumberComponent, 
 ProjectionDecalComponent, 
 SequenceComponent, 
 StatTrackerComponent]
CUSTOMIZATION_CLASSES = {subClass.customType: subClass for subClass in CUSTOMIZATION_CLASS_LIST}

def parseC11sComponentDescr(customizationElementCompDescr):
    return parseCompDescr(CUSTOMIZATION_CLASSES, customizationElementCompDescr)
