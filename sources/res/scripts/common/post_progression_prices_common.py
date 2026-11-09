# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/post_progression_prices_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/post_progression_prices_common.py
from __future__ import absolute_import
from items import vehicles

def getPostProgressionPrice(priceTag, vehType, priceContainer=None):
    postProgressionPricesOverrides = vehType.postProgressionPricesOverrides
    postProgressionPrices = priceContainer if priceContainer else vehicles.g_cache.postProgression().prices
    if postProgressionPricesOverrides and priceTag in postProgressionPricesOverrides:
        price = postProgressionPricesOverrides[priceTag]
    else:
        price = postProgressionPrices.get(priceTag, {}).get(vehType.level, {})
    return price
