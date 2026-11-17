# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/visual_script/misc.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING
from typing import Dict as Dict, Union as Union
from ResMgr import DataSection as DataSection
from visual_script.block import Block as Block
VisualScriptTag = 'visualScript'

class DeferredQueue(object):
    COMMON = 0
    SINGLE = 1

class ASPECT(object):
    SERVER = 'SERVER'
    CLIENT = 'CLIENT'
    HANGAR = 'HANGAR'
    ALL: list

class EDITOR_TYPE(object):
    NONE = 0
    STR_KEY_SELECTOR = 1
    ENUM_SELECTOR = 2
    COMPLEX_KEY_SELECTOR = 3
    VEHICLE_NAME_SELECTOR = 4
    VEHICLE_PRESET_SELECTOR = 5

class EDITOR_CUSTOM_ICON(object):
    EVENT_DELAYED = 1

class BLOCK_MODE(object):
    NONE = 0
    UNIQUE = 32
    DEV = 64
    HIDE_FROM_LIB = 256
    DEPRECATED = 512
    CAN_BE_CONST_EXPR = 2048

def makePlanPath(planName):
    ...
def errorVScript(owner, msg):
    ...
def warningVScript(owner, msg):
    ...
def readVisualScriptPlanParams(section, commonParams=...):
    ...
def readVisualScriptPlan(section, commonParams=...):
    ...
def readVisualScriptPlans(section, commonParams=...):
    ...
def readVisualScriptSection(section, aspects=None):
    ...
def _readVisualScriptAspect(section, aspect, commonParams):
    ...
