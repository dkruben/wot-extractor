# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/renewable_subscription_common/passive_xp.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import VEHICLE_NO_CREW_TRANSFER_PENALTY_TAG as VEHICLE_NO_CREW_TRANSFER_PENALTY_TAG
from items import vehicles as vehicles, tankmen as tankmen
from items.tankmen import TankmanDescr as TankmanDescr, VEHICLE_CLASS_TAGS as VEHICLE_CLASS_TAGS
from typing import Set as Set
FORBIDDEN_TAGS: set

class _Tank(object):
    vehicleType: Any
    def __init__(self, vehicleType):
        ...
    @property
    def isPremium(self):
        ...
    @property
    def hasNoCrewTransferPenalty(self):
        ...
    @property
    def nation(self):
        ...
    def isSameClass(self, tank):
        ...
    def __str__(self):
        ...
    def __eq__(self, other):
        ...
    def __hash__(self):
        ...

class CrewSlotValidationResult(object):
    isEmpty: Any
    tManValidRes: Any
    def __init__(self):
        ...

class ValidationResult(object):
    isValid: Any
    errorList: Any
    class ERRORS:
        NOT_PREMIUM = 1
        NOT_THE_SAME_CLASS = 2
        NOT_THE_SAME_NATION = 3
        NO_VEHICLE_ASSOCIATED = 4
        NO_NEED_XP = 5
    def __init__(self):
        ...
    def appendError(self, error):
        ...

class CrewValidator(object):
    tank: Any
    def __init__(self, vehicleType):
        ...
    def validateCrew(self, crew):
        ...
    def validateCrewSlot(self, compactDescr):
        ...
    def _isTankmanOk(self, tmanDescr):
        ...

def isTagsSetOk(tags):
    ...
