# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prb_control/entities/base/unit/vehicles_watcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from UnitBase import UNIT_SLOT as UNIT_SLOT
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.entities.base.unit.ctx import AssignUnitCtx as AssignUnitCtx
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IRentalsController as IRentalsController, IIGRController as IIGRController
from skeletons.gui.shared import IItemsCache as IItemsCache

class UnitVehiclesWatcher(object):
    itemsCache: Any
    rentals: Any
    igrCtrl: Any
    __entity: Any
    def __init__(self, entity):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def validate(self, update=False):
        ...
    def __onVehiclesUpdated(self, vehicles):
        ...
    def __onRentUpdated(self, vehicles):
        ...
    def __onIgrRoomChanged(self, roomType, xpFactor):
        ...
