# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/factories/UnitFactory.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared.system_factory import registerUnitEntity as registerUnitEntity, collectUnitEntity as collectUnitEntity
from gui.shared.system_factory import registerUnitEntryPoint as registerUnitEntryPoint, collectUnitEntryPoint as collectUnitEntryPoint
from gui.shared.system_factory import registerUnitEntryPointByType as registerUnitEntryPointByType, collectUnitEntryPointByType as collectUnitEntryPointByType
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.factories.ControlFactory import ControlFactory as ControlFactory
from gui.prb_control.entities.base.unit.ctx import LeaveUnitCtx as LeaveUnitCtx
from gui.prb_control.entities.base.unit.entity import UnitIntroEntity as UnitIntroEntity
from gui.prb_control.entities.e_sport.unit.entity import ESportIntroEntity as ESportIntroEntity, ESportIntroEntry as ESportIntroEntry
from gui.prb_control.entities.e_sport.unit.public.entity import PublicBrowserEntity as PublicBrowserEntity, PublicEntity as PublicEntity
from gui.prb_control.entities.e_sport.unit.public.entity import PublicBrowserEntryPoint as PublicBrowserEntryPoint, PublicEntryPoint as PublicEntryPoint
from gui.prb_control.entities.event.squad.entity import EventBattleSquadEntity as EventBattleSquadEntity, EventBattleSquadEntryPoint as EventBattleSquadEntryPoint
from gui.prb_control.entities.mapbox.squad.entity import MapboxSquadEntryPoint as MapboxSquadEntryPoint, MapboxSquadEntity as MapboxSquadEntity
from gui.prb_control.entities.stronghold.unit.entity import StrongholdEntity as StrongholdEntity, StrongholdEntryPoint as StrongholdEntryPoint, StrongholdBrowserEntryPoint as StrongholdBrowserEntryPoint, StrongholdBrowserEntity as StrongholdBrowserEntity
from gui.prb_control.entities.random.squad.entity import RandomSquadEntity as RandomSquadEntity, RandomSquadEntryPoint as RandomSquadEntryPoint
from gui.prb_control.items import PlayerDecorator as PlayerDecorator, FunctionalState as FunctionalState
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.prb_control.settings import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, CTRL_ENTITY_TYPE as CTRL_ENTITY_TYPE
__all__: tuple
_SUPPORTED_INTRO_BY_TYPE: dict
_SUPPORTED_BROWSER_BY_TYPE: dict

class UnitFactory(ControlFactory):
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
