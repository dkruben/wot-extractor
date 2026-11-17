# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/crits_mask_parser.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
from shared_utils import BitmaskHelper as BitmaskHelper
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from items.vehicles import VEHICLE_DEVICE_TYPE_NAMES as VEHICLE_DEVICE_TYPE_NAMES, VEHICLE_TANKMAN_TYPE_NAMES as VEHICLE_TANKMAN_TYPE_NAMES

class CRIT_MASK_SUB_TYPES(CONST_CONTAINER):
    DESTROYED_DEVICES = 'destroyedDevices'
    CRITICAL_DEVICES = 'criticalDevices'
    DESTROYED_TANKMENS = 'destroyedTankmen'

def critsParserGenerator(mask):
    ...
