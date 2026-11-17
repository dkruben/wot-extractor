# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic/pre_queue/permissions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions as PreQueuePermissions
from helpers import time_utils as time_utils, dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicPermissions(PreQueuePermissions):
    __epicCtrl: Any
    def canCreateSquad(self):
        ...
