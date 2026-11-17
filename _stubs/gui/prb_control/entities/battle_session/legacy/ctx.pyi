# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/battle_session/legacy/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import OBSERVER_VEH_INVENTORY_ID as OBSERVER_VEH_INVENTORY_ID, OBSERVER_VEH_NAME as OBSERVER_VEH_NAME, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.prb_control.entities.base.legacy.ctx import JoinLegacyCtx as JoinLegacyCtx, SetPlayerStateCtx as SetPlayerStateCtx
from gui.prb_control.prb_getters import getPrebattleSettings as getPrebattleSettings
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class JoinBattleSessionCtx(JoinLegacyCtx):
    __slots__: tuple
    def __init__(self, prbID, prbType, prbClusterID, waitingID='', flags=...):
        ...

class BattleSessionSetPlayerStateCtx(SetPlayerStateCtx):
    def getVehicleInventoryID(self):
        ...
