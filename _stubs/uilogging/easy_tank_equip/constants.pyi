# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/easy_tank_equip/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from items import ITEM_TYPE_NAMES as ITEM_TYPE_NAMES, ITEM_TYPES as ITEM_TYPES
FEATURE = 'easy_tank_equip'

class EasyTankEquipLogActions(str, Enum):
    OPEN = 'open'
    CLOSE = 'close'
    CLICK = 'click'
    SWITCH_PRESET = 'switch_preset'
    SWAP_SLOTS = 'swap_slots'

class EasyTankEquipLogItems(str, Enum):
    MAIN_VIEW = 'easy_tank_equip_view'
    APPLY_BUTTON = 'apply_button'
    CANCEL_BUTTON = 'cancel_button'
    CREW: Any
    OPT_DEVICES: Any
    SHELLS: Any
    CONSUMABLES: Any
    STYLES: Any

class EasyTankEquipSwapInitiators(str, Enum):
    DRAG_AND_DROP = 'drag_and_drop'
    SWAP_BUTTON = 'swap_button'
