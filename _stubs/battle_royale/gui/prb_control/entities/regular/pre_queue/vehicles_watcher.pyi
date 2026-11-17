# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher as BaseVehiclesWatcher
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Iterable as Iterable
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class BattleRoyaleVehiclesWatcher(BaseVehiclesWatcher):
    itemsCache: Any
    lobbyContext: Any
    def _getUnsuitableVehicles(self, onClear=False):
        ...
