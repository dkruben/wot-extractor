# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/common_tank_structure.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/common_tank_structure.py
from __future__ import absolute_import
from collections import namedtuple
import CGF
from constants import UNKNOWN_RESPAWN_ID
VehicleAppearanceCacheInfo = namedtuple('VehicleAppearanceCacheInfo', ('typeDescr',
                                                                       'health',
                                                                       'isCrewActive',
                                                                       'isTurretDetached',
                                                                       'outfitCD',
                                                                       'forceDynAttachmentLoading',
                                                                       'entityGameObject',
                                                                       'respawnID'))
VehicleAppearanceCacheInfo.__new__.__defaults__ = (
 None, 0, False, False, '', False, CGF.GameObject.INVALID_GAME_OBJECT, UNKNOWN_RESPAWN_ID)
