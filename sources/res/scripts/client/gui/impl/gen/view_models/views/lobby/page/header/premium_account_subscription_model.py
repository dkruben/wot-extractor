# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/premium_account_subscription_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/header/premium_account_subscription_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class PremiumTypeEnum(Enum):
    NONE = 'None'
    BASIC = 'Basic'
    PLUS = 'Plus'
    VIP = 'VIP'


class PremiumStateEnum(Enum):
    INACTIVE = 'Inactive'
    ACTIVE = 'Active'
    CANCELLED = 'Cancelled'


class PremiumAccountSubscriptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PremiumAccountSubscriptionModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return PremiumTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getState(self):
        return PremiumStateEnum(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)

    def getExpiryTime(self):
        return self._getNumber(2)

    def setExpiryTime(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(PremiumAccountSubscriptionModel, self)._initialize()
        self._addStringProperty('type')
        self._addStringProperty('state')
        self._addNumberProperty('expiryTime', 0)
