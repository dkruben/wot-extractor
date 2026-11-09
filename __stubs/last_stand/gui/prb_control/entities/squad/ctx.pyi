# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/prb_control/entities/squad/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx as UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from last_stand.gui.ls_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from last_stand_common.last_stand_constants import PREBATTLE_TYPE as PREBATTLE_TYPE

# decorador original: @ReprInjector.withParent(...)
class SetDifficultyLevelUnitCtx(UnitRequestCtx):
    __slots__: tuple
    _queueType: Any
    def __init__(self, queueType, waitingID=''):
        ...
    def getQueueType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class LastStandSquadSettingsCtx(SquadSettingsCtx):
    __slots__: tuple
    _arenaUniqueID: Any
    def __init__(self, entityType=..., waitingID='', flags=..., accountsToInvite=None, isForced=False, arenaUniqueID=None):
        ...
    def getArenaUniqueID(self):
        ...
