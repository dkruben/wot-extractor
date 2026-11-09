# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frontline.gui.prb_control.entities.epic.pre_queue import entity as fl_entity
from frontline.gui.prb_control.entities.epic.squad import entity as fl_squad_entity
from frontline.gui.prb_control.entities.epic_battle_training import entity as fl_training_entity
from frontline.gui.prb_control.storages.frontline_storage import FrontLineStorage as FrontLineStorage
from constants import QUEUE_TYPE as QUEUE_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from gui.prb_control.storages import makeQueueName as makeQueueName
from gui.shared.system_factory import registerQueueEntity as registerQueueEntity, registerEntryPoint as registerEntryPoint, registerUnitEntryPointByType as registerUnitEntryPointByType, registerUnitEntity as registerUnitEntity, registerLegacyEntryPointByType as registerLegacyEntryPointByType, registerLegacyEntryPoint as registerLegacyEntryPoint, registerLegacyEntity as registerLegacyEntity, registerPrbStorage as registerPrbStorage, registerBattleResultStatsCtrl as registerBattleResultStatsCtrl
from gui.prb_control.factories.LegacyFactory import extendSupportedIntroByType as extendSupportedIntroByType
from frontline.gui.battle_results.frontline_stats_controller import FrontlineBattleResultStatsCtrl as FrontlineBattleResultStatsCtrl

def registerFLPrebattles():
    ...
def extendIntroByType():
    ...
