# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/permissions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions as PreQueuePermissions
from helpers import time_utils as time_utils, dependency as dependency
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyalePermissions(PreQueuePermissions):
    __battleRoyaleController: Any
    def canCreateSquad(self):
        ...
