# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/utils.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from builtins import str as str
import nations as nations
from WebBrowser import getWebCache as getWebCache
from adisp import adisp_async as adisp_async
from server_side_replay.gui.impl.gen.view_models.views.lobby.enums import TankmanLocation as TankmanLocation
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import ToggleGroupType as ToggleGroupType
from server_side_replay.gui.impl.gen.view_models.views.lobby.popovers.replays_filter_popover_model import VehicleSortColumn as VehicleSortColumn
from server_side_replay.gui.impl.lobby.filter import GRADE_PREMIUM as GRADE_PREMIUM, GRADE_ELITE as GRADE_ELITE, GRADE_PRIMARY as GRADE_PRIMARY
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES as VEHICLE_TYPES_ORDER_INDICES
_logger: Any

class WebReplaysHelper(object):
    __slots__: tuple
    __DEFAULT_TIMEOUT = 10.0
    __callbackMethod: Any
    __imageUrl: Any
    __callbackDelayer: Any
    __webCache: Any
    __defLocalDirPath: Any
    def __init__(self, defLocalDirPath='server_replays'):
        ...
    # decorador original: @adisp_async
    def getRelativePath(self, imageUrl, callback=...):
        ...
    def __stop(self):
        ...
    def __onTimer(self):
        ...
    def __callMethod(self, localPath):
        ...

def getRentCriteria():
    ...
def buildPopoverTankKeySortCriteria(field):
    ...
def buildPopoverTankFilterCriteria(filters):
    ...
