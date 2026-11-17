# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/prb_control/entities/base/ctx.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.shared.utils.decorators import ReprInjector as ReprInjector

# decorador original: @ReprInjector.withParent(...)
class Comp7LightPrbAction(PrbAction):
    __squadSize: Any
    def __init__(self, actionName, squadSize, mmData=0, accountsToInvite=None):
        ...
    def getSquadSize(self):
        ...
