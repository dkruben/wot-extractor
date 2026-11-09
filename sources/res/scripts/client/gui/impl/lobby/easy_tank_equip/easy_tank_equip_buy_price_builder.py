# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/easy_tank_equip_buy_price_builder.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/easy_tank_equip/easy_tank_equip_buy_price_builder.py
import typing
from gui.shared.money import Currency
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder
if typing.TYPE_CHECKING:
    from typing import Tuple, Dict, Union, Iterable
    from gui.shared.money import Money
    Price = Union[(Money, Dict)]

class EasyTankEquipBuyPriceModelBuilder(BuyPriceModelBuilder):

    @classmethod
    def _getCurrencyIterator(cls, price):
        order = (
         Currency.CRYSTAL, Currency.EQUIP_COIN, Currency.GOLD, Currency.CREDITS)
        for c in order:
            value = price.get(c)
            if value is not None:
                yield (
                 c, value)

        return
