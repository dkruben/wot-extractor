# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/common/last_stand_common/ls_battle_feedback.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
LSGameplayAction: Any

class LSGameplayActionID(object):
    UNKNOWN = 0
    VEHICLE_REPAIR_INCOMING = 1
    VEHICLE_REPAIR_OUTCOMING = 2
    MODULES_DAMAGE_BLOCKED = 3
    HEALTH_DRAINED_BY_PASSIVE_VAMPIRE = 4
    EQUIPMENT_ACTIVATED = 5
    HEAL_BY_SELF_SITUATIONAL = 6
    HEAL_BY_OBELISK = 7

def packGameplayActionFeedback(action):
    ...
def unpackGameplayActionFeedback(packedData):
    ...
