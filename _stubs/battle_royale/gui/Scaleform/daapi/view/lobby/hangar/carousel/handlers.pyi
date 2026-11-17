# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/carousel/handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from stats_params import BATTLE_ROYALE_STATS_ENABLED as BATTLE_ROYALE_STATS_ENABLED
from gui.shared import event_dispatcher as shared_events
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import SimpleVehicleCMHandler as SimpleVehicleCMHandler

class VEHICLE(object):
    STATS = 'showVehicleStatistics'

class BRVehicleContextMenuHandler(SimpleVehicleCMHandler):
    vehInvID: Any
    vehCD: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def getVehCD(self):
        ...
    def getVehInvID(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
    def showVehicleStats(self):
        ...
