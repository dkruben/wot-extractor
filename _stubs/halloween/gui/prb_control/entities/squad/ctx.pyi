# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/prb_control/entities/squad/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx as UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from halloween.gui.halloween_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from halloween_common.halloween_constants import PREBATTLE_TYPE as PREBATTLE_TYPE

# decorador original: @ReprInjector.withParent(...)
class SetDifficultyLevelUnitCtx(UnitRequestCtx):
    __slots__: tuple
    _queueType: Any
    def __init__(self, queueType, waitingID=''):
        ...
    def getQueueType(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class HalloweenSquadSettingsCtx(SquadSettingsCtx):
    __slots__: tuple
    _arenaUniqueID: Any
    def __init__(self, entityType=..., waitingID='', flags=..., accountsToInvite=None, isForced=False, arenaUniqueID=None):
        ...
    def getArenaUniqueID(self):
        ...
