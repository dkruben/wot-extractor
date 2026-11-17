# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/item_price.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import old_div as old_div, viewvalues as viewvalues
from goodies.GoodieResources import Gold as Gold, Credits as Credits

class PRICE_TYPE:
    DEFAULT: tuple
    PROMO: tuple
    PERSONAL: tuple

def getItemPrice(item, gameParams, goodies=None, goodieTarget=None):
    ...
def getNextSlotPrice(slots, slotsPrices):
    ...
def getNextBerthPackPrice(berths, berthsPrices):
    ...
