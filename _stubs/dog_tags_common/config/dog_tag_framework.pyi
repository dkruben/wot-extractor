# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/dog_tags_common/config/dog_tag_framework.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import inspect as inspect
import sys as sys
from functools import partial as partial
import typing as typing
from future.utils import viewitems as viewitems
from dog_tags_common.config.common import ParameterType as ParameterType, Visibility as Visibility, ParseException as ParseException, ComponentPurpose as ComponentPurpose, ComponentViewType as ComponentViewType, ComponentNumberType as ComponentNumberType
from dog_tags_common.config.validators import validateTriumphMedal as validateTriumphMedal, validateTriumph as validateTriumph, validateSkill as validateSkill, validateDedication as validateDedication, validateDedicationUnlock as validateDedicationUnlock, validateBase as validateBase, validateRankedSkill as validateRankedSkill, validateViewType as validateViewType, validateCommon as validateCommon, validateStartingComponent as validateStartingComponent, validateCoupled as validateCoupled
from typing import List as List
parserInfo: Any

class XMLObjBuilder(object):
    __componentCls: Any
    _component: Any
    def __init__(self, componentCls):
        ...
    def reset(self):
        ...
    def validate(self):
        ...
    def build(self):
        ...

class ComponentBuilder(XMLObjBuilder):
    TAG = 'component'
    PARAMS: dict
    DEFAULTS: dict
    VALIDATORS: dict
    def __init__(self):
        ...
    def componentId(self, value):
        ...
    def resourceRoot(self, value):
        ...
    def viewType(self, value):
        ...
    def coupledComponentId(self, value):
        ...
    def animation(self, value):
        ...
    def isShowInPrebattle(self, value):
        ...
    def purpose(self, value):
        ...
    def unlockKey(self, value):
        ...
    def progressKey(self, value):
        ...
    def isHidden(self, value):
        ...
    def isSecret(self, value):
        ...
    def isDefault(self, value):
        ...
    def isExternalUnlockOnly(self, value):
        ...
    def grades(self, value):
        ...
    def isDeprecated(self, value):
        ...
    def numberType(self, value):
        ...
    def src(self, value):
        ...
    def minLevel(self, value):
        ...
    def battleTypes(self, value):
        ...
    def glossaryName(self, value):
        ...
    def validate(self):
        ...

class StartingComponentsBuilder(XMLObjBuilder):
    TAG = 'startingComponents'
    PARAMS: dict
    VALIDATORS: list
    __componentDefs: Any
    _compsID: Any
    def __init__(self, componentDefs=None):
        ...
    def components(self, value):
        ...
    def validate(self):
        ...
    def build(self):
        ...

class ComponentDefinition(object):
    componentId: Any
    resourceRoot: Any
    viewType: Any
    coupledComponentId: Any
    animation: Any
    isShowInPrebattle: Any
    purpose: Any
    unlockKey: Any
    progressKey: Any
    isHidden: Any
    isSecret: Any
    isDefault: Any
    isExternalUnlockOnly: Any
    grades: Any
    isDeprecated: Any
    src: Any
    numberType: Any
    minLevel: Any
    battleTypes: Any
    glossaryName: Any
    def __init__(self):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...

class StartingComponents(object):
    components: Any
    def __init__(self):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...

def buildParserInfo():
    ...
