# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/post_mortem_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES
from debug_utils import LOG_ERROR as LOG_ERROR

class POSTMORTEM_FEATURES:
    DEATH_FREE_CAM = 'deathfreecam'
    KILL_CAM = 'killcam'
    LOOK_AT_KILLER = 'lookAtKiller'
    ALL: tuple

class POSTMORTEM_MODIFIERS:
    POST_MORTEM = 'postmortemModifiers'
    DEATH_FREE_CAM = 'deathfreecamModifiers'
    KILL_CAM = 'killcamModifiers'
    ALL: tuple

def readPostMortemSection(dataSection, supportedFeatures=..., supportedModifiers=...):
    ...
