# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/fairplay_violation_types.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from soft_exception import SoftException as SoftException
from extension_utils import ResMgr as ResMgr
from constants import FairplayViolationType as FairplayViolationType, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, PENALTY_TYPES as PENALTY_TYPES, IS_CLIENT as IS_CLIENT
from gui.impl.gen import R as R
_CONFIG_FILE = 'scripts/item_defs/fairplay_violation_types.xml'
_XML_NAMESPACE = 'xmlns:xmlref'
FAIRPLAY_EXCLUDED_ARENA_BONUS_TYPES: list
FAIRPLAY_VIOLATIONS_NAMES: list
FAIRPLAY_VIOLATIONS_MASKS: dict
BASE_VIOLATIONS: list

class FairplayViolations(object):
    __violation2type: dict
    __type2violations: dict
    @classmethod
    def getViolationType(cls, violationName):
        ...
    @classmethod
    def setViolationType(cls, violationName, violationType):
        ...
    @classmethod
    def getViolationsByType(cls, violationType):
        ...

def getViolationsByMask(violationsMask):
    ...
def getViolationTypesMask(violationsMask):
    ...
def init():
    ...
def _readViolations(section):
    ...
def initViolationTypes(violationTypes):
    ...
def getPenaltyTypeAndViolationName(fairplayViolations, banDuration):
    ...
def getFairplayViolationLocale(violationName):
    ...
