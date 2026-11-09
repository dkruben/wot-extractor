# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/crew_tab_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags, ViewEvent as ViewEvent
from gui.Scaleform.daapi.view.lobby.vehicle_preview.info.crew_tab_helper import PreviewTankman as PreviewTankman, isValidCrewForVehicle as isValidCrewForVehicle, getCrewPreviewTitle as getCrewPreviewTitle, getCustomHeader as getCustomHeader, getPreviewCrewMemberArgs as getPreviewCrewMemberArgs
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import OFFER_CHANGED_EVENT as OFFER_CHANGED_EVENT
from gui.Scaleform.daapi.view.meta.VehiclePreviewCrewTabInjectMeta import VehiclePreviewCrewTabInjectMeta as VehiclePreviewCrewTabInjectMeta
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import createAndLoadBackportTooltipWindow as createAndLoadBackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.vehicle_preview.tabs.crew_tab_model import CrewTabModel as CrewTabModel
from gui.impl.gen.view_models.views.lobby.vehicle_preview.tabs.tankman_preview_model import TankmanPreviewModel as TankmanPreviewModel
from gui.impl.lobby.crew.crew_helpers.model_setters import setTmanSkillsModel as setTmanSkillsModel
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getRoleBySkillName as getRoleBySkillName
from gui.impl.lobby.crew.tooltips.empty_skill_tooltip import EmptySkillTooltip as EmptySkillTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items.Tankman import crewMemberRealSkillLevel as crewMemberRealSkillLevel
from gui.shared.gui_items.Vehicle import sortCrew as sortCrew
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from soft_exception import SoftException as SoftException
from web.web_client_api.common import ItemPackTypeGroup as ItemPackTypeGroup, ItemPackType as ItemPackType
from typing import Optional as Optional
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from web.web_client_api.common import ItemPackEntry as ItemPackEntry
DOG = 'dog'

class CrewTabView(ViewImpl):
    __slots__: tuple
    __appLoader: Any
    __itemsCache: Any
    _toolTipMgr: Any
    _isCustomCrew: Any
    _crewItemPack: Any
    _crew: Any
    _vehicle: Any
    _title: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def updateData(self, crewStr, vehicleItems, crewItemPack):
        ...
    def _fillViewModel(self):
        ...
    def _fillExtraInfo(self, vm):
        ...
    def _fillTankmen(self, vm):
        ...
    def _update(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _finalize(self):
        ...
    def _getListeners(self):
        ...
    def _getVehicle(self):
        ...
    def _onOfferChanged(self, event):
        ...

class CrewTabInject(VehiclePreviewCrewTabInjectMeta):
    def _makeInjectView(self):
        ...
    def updateInjectData(self, text, vehicleItems, crewItemPack):
        ...
