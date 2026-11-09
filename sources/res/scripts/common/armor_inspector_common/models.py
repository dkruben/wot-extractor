# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/armor_inspector_common/models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/armor_inspector_common/models.py
from __future__ import absolute_import
import typing
from dict2model import models

class ArmorInspectorConfigModel(models.Model):
    __slots__ = ('enabled', 'linkButtonURL', 'disabledVehicle')

    def __init__(self, enabled, linkButtonURL, disabledVehicle):
        super(ArmorInspectorConfigModel, self).__init__()
        self.enabled = enabled
        self.linkButtonURL = linkButtonURL
        self.disabledVehicle = disabledVehicle

    def _reprArgs(self):
        return ('enabled={} linkButtonURL={} disabledVehicle={}').format(self.enabled, self.linkButtonURL, self.disabledVehicle)

    def isDisabledForVehicle(self, vehicleName):
        return vehicleName in self.disabledVehicle
