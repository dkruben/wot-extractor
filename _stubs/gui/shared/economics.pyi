# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/economics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from ItemRestore import getVehicleRestorePrice as getVehicleRestorePrice
from gui.shared.money import Money as Money, Currency as Currency
from math_common import round_py2_style_int as round_py2_style_int
from rent_common import makeRentID as makeRentID
_DisplayPrice: Any

class ActualPrice(object):
    RESTORE_PRICE = 1
    RENT_PRICE = 2
    BUY_PRICE = 3

def getActionPrc(price, defaultPrice):
    ...
def calcRentPackages(vehicle, proxy, rentalsController):
    ...
def getPremiumCostActionPrc(discounts, packet, proxy):
    ...
def calcVehicleRestorePrice(defaultPrice, proxy):
    ...
def getGUIPrice(item, money, exchangeRate):
    ...
