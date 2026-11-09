# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/readers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/readers/__init__.py
from __future__ import absolute_import
from items.readers import chassis_readers
from items.readers import gun_readers
from items.readers import shared_readers
from items.readers import skills_readers
from items.readers import sound_readers
from items.readers import tankmen_readers
from constants import HAS_DEV_RESOURCES
if HAS_DEV_RESOURCES:
    from items.readers.json_reader import vehicle_reader
__all__ = ('chassis_readers', 'gun_readers', 'shared_readers', 'skills_readers', 'sound_readers',
           'tankmen_readers', 'json_vehicle_reader')
if HAS_DEV_RESOURCES:
    json_vehicle_reader = vehicle_reader
else:
    json_vehicle_reader = None
