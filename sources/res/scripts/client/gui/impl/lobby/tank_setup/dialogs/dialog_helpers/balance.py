# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/dialog_helpers/balance.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/tank_setup/dialogs/dialog_helpers/balance.py
from frameworks.wulf.view.array import fillViewModelsArray
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.sub_views.current_balance_model import CurrentBalanceModel

def initBalance(balanceArray, currencies, itemsCache):
    money = itemsCache.items.stats.money
    currencyModelsList = []
    for currency in currencies:
        cur = CurrentBalanceModel()
        cur.setCurrencyType(currency)
        cur.setCurrencyValue(money.get(currency, 0))
        currencyModelsList.append(cur)

    fillViewModelsArray(currencyModelsList, balanceArray)
