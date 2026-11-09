# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_events/mechanics_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_events/mechanics_events.py
from __future__ import absolute_import
import CGF, Vehicular

def postSightPointerSectorEvent(spaceID, entityID, slotName, targetWidth, targetDistance, targetOpacity, duration):
    CGF.postEvent(spaceID, Vehicular.VariablesChangedEvent(entityID=entityID, slotName=slotName, varValueMap={'sectorVision/length': targetDistance, 
       'sectorVision/width': targetWidth, 
       'sectorVision/opacity': targetOpacity, 
       'sectorVision/duration': duration}))
