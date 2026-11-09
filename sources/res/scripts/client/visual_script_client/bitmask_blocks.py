# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/visual_script_client/bitmask_blocks.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/visual_script_client/bitmask_blocks.py
from __future__ import absolute_import
from constants import EQUIPMENT_ERROR_STATES, CollisionFlags, VEHICLE_HIT_FLAGS
from visual_script.bitmask_blocks_common import BitMaskBase
from visual_script.misc import ASPECT

class BitMask(BitMaskBase):
    _MASK_TYPES = {'Equipment ErrorStates': EQUIPMENT_ERROR_STATES, 
       'Collision Flags': CollisionFlags, 
       'Vehicle Hit Flags': VEHICLE_HIT_FLAGS}

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]
