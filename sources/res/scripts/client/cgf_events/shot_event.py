# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_events/shot_event.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_events/shot_event.py
from __future__ import absolute_import
import CGF
from cgf_modules import game_events

def postVehicleShotEvent(entityGo, gunGO, gunIndex, shellType):
    CGF.postEvent(entityGo.spaceID, game_events.VehicleShotEvent(entityGoUuid=entityGo.uuid, gunGoUuid=gunGO.uuid, gunIndex=gunIndex, shellType=shellType))
