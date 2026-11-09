# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/telecom_rentals_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/telecom_rentals_common.py
from __future__ import absolute_import
from enum import IntEnum
RENT_TOKEN_NAME = 'telecom_rent_token'
PARTNERSHIP_TOKEN_NAME = 'telecom_partnership_token'
PARTNERSHIP_BLOCKED_TOKEN_NAME = 'telecom_partnership_blocked_token'
ROSTER_EXPIRATION_TOKEN_NAME = 'telecom_roster_expiration_token'
TELECOM_RENTALS_CONFIG = 'telecom_rentals_config'
TELECOM_RENTALS_RENT_KEY = 'telecom'

class PartnershipState(IntEnum):
    NO_PARTNERSHIP = 0
    ACTIVE_PARTNERSHIP = 1
    BLOCKED_PARTNERSHIP = 2
