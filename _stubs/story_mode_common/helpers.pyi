# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from external_strings_utils import strtobool as strtobool
from story_mode_common.story_mode_constants import LONG_INT_HALF_SHIFT as LONG_INT_HALF_SHIFT, MissionType as MissionType, DISABLE_REGULAR_OPERATIONS as DISABLE_REGULAR_OPERATIONS
from story_mode_common.configs.story_mode_missions import MissionModel as MissionModel

def isTaskCompleted(progress, missionId, taskId):
    ...
def isMissionCompleted(progress, missionModel):
    ...
def taskBitMask(taskId):
    ...
def getRewardActionSetId(missionId, taskId=0):
    ...
def isMissionDisabledByABGroup(mission, group, abConfig):
    ...
