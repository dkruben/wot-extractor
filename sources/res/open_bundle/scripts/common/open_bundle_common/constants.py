# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/common/open_bundle_common/constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/common/open_bundle_common/constants.py
from __future__ import absolute_import
from datetime import timedelta
OPEN_BUNDLE_GAME_PARAMS_KEY = 'open_bundle_config'
OPEN_BUNDLE_PDATA_KEY = 'openBundle'
MIN_X_COORDINATE = 0
MIN_Y_COORDINATE = 0
MAX_X_COORDINATE = 12
MAX_Y_COORDINATE = 5
OPEN_BUNDLE_MAX_CELLS = (MAX_X_COORDINATE - MIN_X_COORDINATE) * (MAX_Y_COORDINATE - MIN_Y_COORDINATE)
OPEN_BUNDLE_CELL_TAGS = ('rare', 'uniqueNotification')
OPEN_BUNDLE_TEMPLATES = ('S1', 'S2', 'S3', 'S4', 'M1', 'M2', 'L1')
OPEN_BUNDLE_DATA_LIFETIME = timedelta(days=60).total_seconds()
OPEN_BUNDLE_FIXED_REWARD_LOGGING_OFFSET = 1000
