# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/premacc/dashboard/piggy_bank/piggy_bank_states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/premacc/dashboard/piggy_bank/piggy_bank_states.py
from enum import Enum
from frameworks.wulf import ViewModel

class BankState(Enum):
    AVAILABLE = 'available'
    ACTIVE = 'active'
    DISABLE = 'disable'


class PiggyBankStates(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(PiggyBankStates, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(PiggyBankStates, self)._initialize()
