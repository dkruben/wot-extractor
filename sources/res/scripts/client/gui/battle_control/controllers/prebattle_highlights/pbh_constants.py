# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/pbh_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/prebattle_highlights/pbh_constants.py
from __future__ import absolute_import
from shared_utils import CONST_CONTAINER
TANK_SIZE_LOWER_BOUNDS = (
 float('-inf'), 5.0, 8.0)
TANK_POS_TEMPLATE = 'pbh_top{}_{}'
TANK_CAMERA_TEMPLATE = 'pbh_camera_{}_{}'
MARKER_X_FACTOR = 0
MARKER_Y_FACTOR = 1.1

class TankSizes(CONST_CONTAINER):
    SMALL = 'small'
    MEDIUM = 'medium'
    BIG = 'big'
    ORDERED_SIZES = (
     SMALL, MEDIUM, BIG)
