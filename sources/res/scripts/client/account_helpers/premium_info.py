# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/premium_info.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/premium_info.py
from __future__ import absolute_import
from constants import PREMIUM_TYPE

class PremiumInfo(object):

    def __init__(self):
        self._rawPremiumInfo = {p: 0 for p in PREMIUM_TYPE.TYPES_SORTED}
        self._rawPremiumInfo['premMask'] = 0

    def update(self, rawPremiumInfo):
        self._rawPremiumInfo.update(rawPremiumInfo)

    def isActivePremium(self, checkPremiumType):
        return self.activePremiumType >= checkPremiumType

    @property
    def isPremium(self):
        return self.activePremiumType != PREMIUM_TYPE.NONE

    @property
    def totalPremiumExpiryTime(self):
        premiumMask = self._rawPremiumInfo['premMask']
        return max(tuple(self._rawPremiumInfo[p] for p in PREMIUM_TYPE.TYPES_SORTED if bool(premiumMask & p)) + (0, ))

    @property
    def activePremiumExpiryTime(self):
        activePremiumType = self.activePremiumType
        if activePremiumType != PREMIUM_TYPE.NONE:
            return self._rawPremiumInfo[activePremiumType]
        return 0

    @property
    def activePremiumType(self):
        return PREMIUM_TYPE.activePremium(self._rawPremiumInfo['premMask'])

    @property
    def data(self):
        premiumMask = self._rawPremiumInfo['premMask']
        return {pType: {'active': (bool(premiumMask & pType)), 'expiryTime': (self._rawPremiumInfo[pType])} for pType in PREMIUM_TYPE.TYPES_SORTED}
