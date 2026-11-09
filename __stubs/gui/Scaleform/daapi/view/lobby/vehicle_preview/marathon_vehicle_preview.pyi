# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/marathon_vehicle_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview as VehiclePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.server_events.events_dispatcher import showMissionsMarathon as showMissionsMarathon
from helpers import dependency as dependency
from skeletons.gui.game_control import IMarathonEventsController as IMarathonEventsController
from web.web_client_api.common import ItemPackTypeGroup as ItemPackTypeGroup

class MarathonVehiclePreview(VehiclePreview):
    __marathonCtrl: Any
    __marathonPrefix: Any
    __marathon: Any
    __backToHangar: Any
    def __init__(self, ctx=None):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _processBackClick(self, ctx=None):
        ...
