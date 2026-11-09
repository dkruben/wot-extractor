# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/models/ext_money.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.gui_items import formatMoneyError as formatMoneyError, GUI_ITEM_ECONOMY_CODE as GUI_ITEM_ECONOMY_CODE
from gui.shared.money import Currency as Currency, Money as Money
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from soft_exception import SoftException as SoftException
_XP = CURRENCIES_CONSTANTS.XP_COST
_VEH_XP = 'vehXP'
_FREE_XP = CURRENCIES_CONSTANTS.FREE_XP
_ALL_EXT: tuple
EXT_MONEY_UNDEFINED: Any
EXT_MONEY_ZERO_CREDITS: Any
EXT_MONEY_ZERO: Any

class ExtendedCurrency(Currency):
    XP = _XP
    VEH_XP = _VEH_XP
    FREE_XP = _FREE_XP
    ALL: Any
    BY_WEIGHT: Any

class ExtendedGuiItemEconomyCode(GUI_ITEM_ECONOMY_CODE):
    NOT_ENOUGH_XP: Any
    NOT_ENOUGH_VEH_XP: Any
    NOT_ENOUGH_FREE_XP: Any
    NOT_ENOUGH_CURRENCIES: Any
    COMPOUND_PRICE = 'price_is_compound'
    XP_COMPOUND_PRICE = 'price_is_xp_compound'
    STEP_LOCKED = 'step_locked'
    STEP_RECIEVED = 'step_received'
    STEP_RESTRICTED = 'step_restricted'
    MOD_PERSISTENT = 'mod_persistent'
    MULTI_NOT_EXISTS = 'multi_not_exists'
    MULTI_NOT_EMPTY = 'multi_not_empty'
    MULTI_NOT_PURCHASED = 'multi_not_purchased'

class ExtendedMoney(Money):
    ALL = ExtendedCurrency.ALL
    WEIGHT = ExtendedCurrency.BY_WEIGHT
    def __init__(self, xp=None, vehXP=None, freeXP=None, *args, **kwargs):
        ...
    @property
    def xp(self):
        ...
    @property
    def vehXP(self):
        ...
    @property
    def freeXP(self):
        ...
    def isXPCompound(self):
        ...
    def toMoneyTuple(self):
        ...

def getFullXPFromXPPrice(balance, price):
    ...
