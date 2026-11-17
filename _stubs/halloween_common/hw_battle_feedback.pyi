# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/common/halloween_common/hw_battle_feedback.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
HWGameplayAction: Any

class HWGameplayActionID(object):
    UNKNOWN = 0
    VEHICLE_REPAIR_INCOMING = 1
    VEHICLE_REPAIR_OUTCOMING = 2
    MODULES_DAMAGE_BLOCKED = 3
    HEALTH_DRAINED_BY_PASSIVE_VAMPIRE = 4
    SHELLS_LOOT_PICKUP = 5
    HANGAR_ITEMS_LOOT_PICKUP = 6
    HANGAR_ITEMS_LOOT_RECEIVE = 7
    SOULS_LOOT_PICKUP = 8
    SHELLS_LOOT_RECEIVE = 9
    SOULS_LOOT_RECEIVE = 10
    ANOMALY_LOOT_PICKUP = 11
    ANOMALY_LOOT_RECEIVE = 12
    SOULS_LOOT_REFUND = 13
    BOMBER_RESIST = 14
    SOULS_MIRIUMIZATION_ADD = 15
    SOULS_MIRIUMIZATION_DECREASE = 16

def packGameplayActionFeedback(action):
    ...
def unpackGameplayActionFeedback(packedData):
    ...
