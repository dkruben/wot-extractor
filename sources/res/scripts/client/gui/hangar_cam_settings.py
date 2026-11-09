# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/hangar_cam_settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/hangar_cam_settings.py
from __future__ import absolute_import
from account_helpers.settings_core.options import HangarCamPeriodSetting
OPTIONS = HangarCamPeriodSetting.OPTIONS
HANGAR_CAM_PERIODS = {(OPTIONS.TYPE0): 30, 
   (OPTIONS.TYPE1): 45, 
   (OPTIONS.TYPE2): 60}

def convertSettingToFeatures(value):
    selected = OPTIONS.HANGAR_CAM_TYPES[value]
    return HANGAR_CAM_PERIODS.get(selected, -1)
