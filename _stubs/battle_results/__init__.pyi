# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/battle_results/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewitems as viewitems
import importlib as importlib
from DictPackers import Meta as Meta, MergeDictPacker as MergeDictPacker
from battle_pass_integration import getAllIntergatedGameModes as getAllIntergatedGameModes
from battle_results.battle_results_common import BATTLE_RESULTS as BATTLE_RESULTS, BATTLE_PASS_RESULTS as BATTLE_PASS_RESULTS
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE, PATH_TO_CONFIG as PATH_TO_CONFIG, POSSIBLE_TYPES as POSSIBLE_TYPES, ARENA_BONUS_TYPE_TO_SM_TYPE_BATTLE_RESULT as ARENA_BONUS_TYPE_TO_SM_TYPE_BATTLE_RESULT
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
g_config: dict

def __processBonusTypeResults(config, allResults, bonusType, serverResults):
    ...
def setBattleResultsConfig(config):
    ...
def packClientBattleResults(data, bonusType, packingType):
    ...
def unpackClientBattleResults(data):
    ...
def getBattleResultsNames():
    ...
def getBattleResultsSysMsgType(bonusType):
    ...
def init():
    ...
