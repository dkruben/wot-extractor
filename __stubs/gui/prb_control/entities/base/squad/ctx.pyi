# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/squad/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.prb_control import settings as prb_settings
from gui.prb_control.entities.base.unit.ctx import UnitRequestCtx as UnitRequestCtx
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class SquadSettingsCtx(UnitRequestCtx):
    __slots__: tuple
    __accountsToInvite: Any
    def __init__(self, entityType=..., waitingID='', flags=..., accountsToInvite=None, isForced=False):
        ...
    def getRequestType(self):
        ...
    def getID(self):
        ...
    def getAccountsToInvite(self):
        ...
