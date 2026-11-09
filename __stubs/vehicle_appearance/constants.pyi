# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/vehicle_appearance/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import enum as enum
DEFAULT_STICKERS_ALPHA = 1.0
PERIODIC_UPDATE_TIME = 0.25
DIRT_UPDATE_MIN_TIME = 0.05

class AppearanceState(enum.IntEnum):
    CREATED = 0
    CONSTRUCTED = 1
    COMPONENTS_CREATED = 2
    ACTIVATED = 3
    DEACTIVATED = 4
    DESTROYED = 5
