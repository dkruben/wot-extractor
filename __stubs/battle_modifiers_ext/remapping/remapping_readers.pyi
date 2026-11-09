# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/remapping/remapping_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import List as List, Dict as Dict, FrozenSet as FrozenSet, TYPE_CHECKING as TYPE_CHECKING
from battle_modifiers_ext.constants_ext import RemappingConditionNames as RemappingConditionNames, ModifiersWithRemapping as ModifiersWithRemapping
from battle_modifiers_ext.remapping.remapping_composers import getComposerClass as getComposerClass
from battle_modifiers_ext.remapping.remapping_conditions import getConditionClass as getConditionClass
from ResMgr import DataSection as DataSection
from soft_exception import SoftException as SoftException
from battle_modifiers_ext.remapping.remapping_conditions import IRemappingCondition as IRemappingCondition
from battle_modifiers_ext.remapping.remapping_composers import IComposer as IComposer
ERR_TEMPLATE = "[Remapping] {} for remapping '{}'"

def readComposers(config, remappingName, availableConditions):
    ...
def readConditions(config, remappingName):
    ...
def _readComposerConditions(config, remappingName, composerName, availableConditions):
    ...
def _readComposerTemplate(config, remappingName, composerName):
    ...
def _readRemappingRules(config, remappingName, conditionName, sectionName):
    ...
def _readRemappingSource(config, remappingName, conditionName):
    ...
def _readRemappingTarget(config, remappingName, conditionName):
    ...
