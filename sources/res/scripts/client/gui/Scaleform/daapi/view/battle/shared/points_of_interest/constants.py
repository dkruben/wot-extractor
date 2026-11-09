# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/points_of_interest/constants.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.POI_CONSTS import POI_CONSTS
from points_of_interest_shared import PoiStatus, PoiType
POI_TYPE_UI_MAPPING = {(PoiType.ARTILLERY): (POI_CONSTS.POI_TYPE_ARTILLERY), 
   (PoiType.RECON): (POI_CONSTS.POI_TYPE_RECON), 
   (PoiType.ILLUMINATION_FLARE): (POI_CONSTS.POI_TYPE_ILLUMINATION_FLARE)}
POI_STATUS_UI_MAPPING = {(PoiStatus.ACTIVE): (POI_CONSTS.POI_STATUS_ACTIVE), 
   (PoiStatus.CAPTURING): (POI_CONSTS.POI_STATUS_CAPTURING), 
   (PoiStatus.COOLDOWN): (POI_CONSTS.POI_STATUS_COOLDOWN)}
