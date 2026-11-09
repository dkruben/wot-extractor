# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/crosshair/settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/crosshair/settings.py
from __future__ import absolute_import
import aih_constants
from gui.Scaleform.genConsts.ROOT_SWF_CONSTANTS import ROOT_SWF_CONSTANTS
CROSSHAIR_CONTAINER_SWF = 'battleCrosshairsApp.swf'
CROSSHAIR_ROOT_PATH = 'root.main'
CROSSHAIR_INIT_CALLBACK = ROOT_SWF_CONSTANTS.BATTLE_CROSSHAIRS_REGISTER_CALLBACK
CROSSHAIR_ITEM_PATH_FORMAT = '_level0.' + CROSSHAIR_ROOT_PATH + '.{}'
CROSSHAIR_RADIUS_MC_NAME = 'radiusMC'
SPG_GUN_MARKER_ELEMENTS_COUNT = aih_constants.SPG_GUN_MARKER_ELEMENTS_COUNT
SHOT_RESULT_TO_DEFAULT_COLOR = {(aih_constants.SHOT_RESULT.EMPTY): '', 
   (aih_constants.SHOT_RESULT.UNDEFINED): 'normal', 
   (aih_constants.SHOT_RESULT.NOT_PIERCED): 'red', 
   (aih_constants.SHOT_RESULT.LITTLE_PIERCED): 'orange', 
   (aih_constants.SHOT_RESULT.GREAT_PIERCED): 'green'}
SHOT_RESULT_TO_ALT_COLOR = {(aih_constants.SHOT_RESULT.EMPTY): '', 
   (aih_constants.SHOT_RESULT.UNDEFINED): 'normal', 
   (aih_constants.SHOT_RESULT.NOT_PIERCED): 'purple', 
   (aih_constants.SHOT_RESULT.LITTLE_PIERCED): 'pink', 
   (aih_constants.SHOT_RESULT.GREAT_PIERCED): 'yellow'}
