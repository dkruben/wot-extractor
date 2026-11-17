# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lootbox_system/base/awards.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from gui.shared.money import Currency as Currency, Money as Money, ZERO_MONEY as ZERO_MONEY
from helpers import dependency as dependency
from messenger.formatters.service_channel_helpers import getCustomizationItem as getCustomizationItem
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

def preformatRewardsInfo(rewards):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def addCompensation(rewards, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _addLockedStyleForVehicle(customizations, vehicles, itemsCache=None):
    ...
def _getCompensationValue(vehicles):
    ...
