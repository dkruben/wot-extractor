# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/factories/LegacyFactory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.shared.system_factory import registerLegacyEntity as registerLegacyEntity, collectLegacyEntity as collectLegacyEntity
from gui.shared.system_factory import registerLegacyEntryPoint as registerLegacyEntryPoint, collectLegacyEntryPoint as collectLegacyEntryPoint
from gui.shared.system_factory import registerLegacyEntryPointByType as registerLegacyEntryPointByType, collectLegacyEntryPointByType as collectLegacyEntryPointByType
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.factories.ControlFactory import ControlFactory as ControlFactory
from gui.prb_control.entities.base.legacy.ctx import LeaveLegacyCtx as LeaveLegacyCtx
from gui.prb_control.entities.base.legacy.entity import LegacyIntroEntryPoint as LegacyIntroEntryPoint, LegacyInitEntity as LegacyInitEntity, LegacyIntroEntity as LegacyIntroEntity
from gui.prb_control.entities.battle_session.legacy.entity import BattleSessionEntryPoint as BattleSessionEntryPoint, BattleSessionListEntryPoint as BattleSessionListEntryPoint, BattleSessionEntity as BattleSessionEntity
from gui.prb_control.entities.training.legacy.entity import TrainingEntryPoint as TrainingEntryPoint, TrainingIntroEntryPoint as TrainingIntroEntryPoint, TrainingEntity as TrainingEntity, TrainingIntroEntity as TrainingIntroEntity
from gui.prb_control.items import PlayerDecorator as PlayerDecorator, FunctionalState as FunctionalState
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE
__all__: tuple
_SUPPORTED_INTRO_BY_TYPE: dict

class LegacyFactory(ControlFactory):
    def createEntry(self, ctx):
        ...
    def createEntryByAction(self, action):
        ...
    def createEntity(self, ctx):
        ...
    def createPlayerInfo(self, entity):
        ...
    def createStateEntity(self, entity):
        ...
    def createLeaveCtx(self, flags=..., entityType=0):
        ...
    def __createByAccountState(self, ctx):
        ...
    def __createByFlags(self, ctx):
        ...
    def __createByPrbType(self, ctx):
        ...

def extendSupportedIntroByType(items):
    ...
