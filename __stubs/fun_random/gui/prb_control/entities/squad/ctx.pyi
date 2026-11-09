# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/squad/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from fun_random.gui.fun_gui_constants import REQUEST_TYPE as REQUEST_TYPE, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.prb_control.entities.base.squad.ctx import SquadSettingsCtx as SquadSettingsCtx
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx as UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class FunSquadSettingsCtx(SquadSettingsCtx):
    __slots__: tuple
    __desiredSubModeID: Any
    def __init__(self, desiredSubModeID, flags=..., accountsToInvite=None, isForced=False):
        ...
    def getDesiredSubModeID(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class FunSquadChangeSubModeCtx(UnitRequestCtx):
    __slots__: tuple
    __desiredSubModeID: Any
    def __init__(self, desiredSubModeID):
        ...
    def getCooldown(self):
        ...
    def getDesiredSubModeID(self):
        ...
    def getRequestType(self):
        ...
