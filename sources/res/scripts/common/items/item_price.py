# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/item_price.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/item_price.py
from __future__ import absolute_import
from future.utils import old_div, viewvalues
from goodies.GoodieResources import Gold, Credits

class PRICE_TYPE:
    DEFAULT = (0, )
    PROMO = (1, )
    PERSONAL = (2, )


def getItemPrice(item, gameParams, goodies=None, goodieTarget=None):
    priceType = PRICE_TYPE.DEFAULT
    actualPrice = gameParams['items']['itemPrices'][item]
    defaultPrice = gameParams['defaults'].get('items', {}).get('itemPrices', {}).get(item, None)
    if not defaultPrice:
        defaultPrice = actualPrice
    else:
        priceType = PRICE_TYPE.PROMO
    if (actualPrice[0] == 0 or actualPrice[1] == 0) and goodies and goodieTarget:
        personalDiscounts = goodies.test(goodieTarget, {Credits(defaultPrice[0]), Gold(defaultPrice[1])})
        for discount in viewvalues(personalDiscounts):
            if isinstance(discount, Gold) and discount.value <= actualPrice[1]:
                actualPrice = (
                 0, discount.value)
                priceType = PRICE_TYPE.PERSONAL
            elif isinstance(discount, Credits) and discount.value <= actualPrice[0]:
                actualPrice = (
                 discount.value, 0)
                priceType = PRICE_TYPE.PERSONAL

    return (
     defaultPrice, actualPrice, priceType)


def getNextSlotPrice(slots, slotsPrices):
    addSlotNumber = slots - slotsPrices[0]
    if addSlotNumber < 0:
        if len(slotsPrices[1]):
            return (slotsPrices[1][0][0], 0)
        return ('credits', 0)
    if addSlotNumber < len(slotsPrices[1]):
        return slotsPrices[1][addSlotNumber]
    return slotsPrices[1][-1]


def getNextBerthPackPrice(berths, berthsPrices):
    addPackNumber = old_div(berths - berthsPrices[0], berthsPrices[1])
    if addPackNumber < 0:
        return 0
    if addPackNumber < len(berthsPrices[2]):
        return berthsPrices[2][addPackNumber]
    return berthsPrices[2][-1]
