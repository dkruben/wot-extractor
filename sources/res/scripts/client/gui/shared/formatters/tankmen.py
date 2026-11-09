# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/formatters/tankmen.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/tankmen.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from gui.shared.money import Currency
from gui.impl import backport
from gui.impl.gen.view_models.ui_kit.action_price_model import ActionPriceModel
from gui.shared.formatters import updateActionInViewModel
from gui.shared.gui_items.fitting_item import canBuyWithGoldExchange

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def formatDeletedTankmanStr(tankman, itemsCache=None):
    vehicle = itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)
    return tankman.fullUserName + ' (%s, %s)' % (tankman.roleUserName, vehicle.userName)


def getItemPricesViewModel(statsMoney, *itemPrices, **kwargs):
    result = []
    for itemPrice in itemPrices:
        priceModels = []
        if itemPrice.isDefined():
            for currency in statsMoney.currencies:
                currencyValue = itemPrice.price.get(currency)
                if currencyValue is not None:
                    actionPriceModel = ActionPriceModel()
                    isEnough = statsMoney.get(currency) >= currencyValue
                    if not isEnough and 'exchangeRate' in kwargs and currency == Currency.CREDITS:
                        isEnough = canBuyWithGoldExchange(itemPrice.price, statsMoney, kwargs.get('exchangeRate'))
                    actionPriceModel.setIsEnough(isEnough)
                    currencyAction = itemPrice.getActionPrcAsMoney().get(currency)
                    hasAction = currencyAction is not None
                    if hasAction:
                        updateActionInViewModel(currency, actionPriceModel, itemPrice)
                    actionPriceModel.setType(currency)
                    actionPriceModel.setIsWithAction(hasAction)
                    actionPriceModel.setPrice(backport.getIntegralFormat(currencyValue))
                    defPrice = backport.getIntegralFormat(itemPrice.defPrice.get(currency, 0))
                    actionPriceModel.setDefPrice(defPrice)
                    priceModels.append(actionPriceModel)

        else:
            actionPriceModel = ActionPriceModel()
            actionPriceModel.setIsFree(True)
            priceModels.append(actionPriceModel)
        if priceModels:
            result.append(priceModels)

    diff = len(itemPrices) - len(result)
    if diff > 0:
        result.extend([None] * diff)
    return result
