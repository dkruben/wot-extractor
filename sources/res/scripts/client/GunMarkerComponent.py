# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/GunMarkerComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/GunMarkerComponent.py
from __future__ import absolute_import
import BigWorld

class GunMarkerComponent(BigWorld.DynamicScriptComponent):

    def set_gunMarker(self, _=None):
        gunMarker = self.gunMarker
        if gunMarker is None:
            return
        else:
            avatar = BigWorld.player()
            avatar.updateGunMarker(self.entity.id, gunMarker.gunPosition, gunMarker.shotVector, gunMarker.dispersion)
            return
