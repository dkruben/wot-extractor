# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/Loot.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from battleground.loot_object import loadLootById as loadLootById
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from battle_royale.gui.shared.events import LootEvent as LootEvent

class Loot(BigWorld.Entity):
    __lootDescr: Any
    def __init__(self, *args, **kwargs):
        ...
    def onEnterWorld(self, *args):
        ...
    def onLeaveWorld(self):
        ...
    def set_pickedUpBy(self, prev=None):
        ...
