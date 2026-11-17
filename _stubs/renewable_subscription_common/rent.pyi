# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/renewable_subscription_common/rent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum

class RentEventTypes(Enum):
    START_RENT = 1
    END_RENT = 2

class RentLogInfo(Enum):
    ADD = 'excl_veh:add'
    START = 'excl_veh:on'
    END = 'excl_veh:off'
