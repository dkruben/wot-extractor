# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic/pre_queue/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from itertools import chain as chain
import typing as typing
from constants import BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC as BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import isVehLevelUnlockableInBattle as isVehLevelUnlockableInBattle
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher as BaseVehiclesWatcher
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class EpicVehiclesWatcher(BaseVehiclesWatcher):
    _BATTLE_MODE_VEHICLE_TAGS = BATTLE_MODE_VEH_TAGS_EXCEPT_EPIC
    _VEH_STATE_PRIORITIES: dict
    itemsCache: Any
    lobbyContext: Any
    def _getUnsuitableVehicles(self, onClear=False):
        ...
    def _getVehiclesCustomStates(self, onClear=False):
        ...
    def __getWillBeUnlockedVehicles(self):
        ...
