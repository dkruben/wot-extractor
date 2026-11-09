# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/items/hw_supply_slots_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from items.components.supply_slots_components import EquipmentSlot as EquipmentSlot
from items.vehicles import getItemByCompactDescr as getItemByCompactDescr

class HWEquipmentSlot(EquipmentSlot):
    tags: Any
    def readFromSection(self, section):
        ...
    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        ...
