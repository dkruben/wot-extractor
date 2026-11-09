# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tankman_container_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import OrderedDict as OrderedDict
import Event as Event
from account_helpers.AccountSettings import CREW_SKINS_VIEWED as CREW_SKINS_VIEWED
from account_helpers import AccountSettings as AccountSettings
from .base_crew_view import BaseCrewView as BaseCrewView, IS_FROM_ESCAPE_PARAM as IS_FROM_ESCAPE_PARAM
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tankman_container_tab_model import TankmanContainerTabModel as TankmanContainerTabModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_container_view_model import TankmanContainerViewModel as TankmanContainerViewModel
from gui.impl.lobby.crew.personal_case import IPersonalTab as IPersonalTab
from gui.impl.lobby.crew.personal_case.personal_data_view import PersonalDataView as PersonalDataView
from gui.impl.lobby.crew.container_vews.personal_file.personal_file_view import PersonalFileView as PersonalFileView
from gui.impl.lobby.crew.container_vews.service_record.service_record_view import ServiceRecordView as ServiceRecordView
from gui.impl.lobby.hangar.sub_views.vehicle_params_view import VehicleSkillPreviewParamsPresenter as VehicleSkillPreviewParamsPresenter
from gui.shared.event_dispatcher import showChangeCrewMember as showChangeCrewMember
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from nations import NAMES as NAMES
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN, NO_SLOT as NO_SLOT
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
TABS: Any

class TabsId(object):
    PERSONAL_FILE: Any
    PERSONAL_DATA: Any
    SERVICE_RECORD: Any
    ALL: list
    DEFAULT = PERSONAL_FILE

class TankmanContainerView(BaseCrewView):
    __slots__: tuple
    itemsCache: Any
    gui: Any
    _activeTab: Any
    _tankmanInvID: Any
    vehicleID: Any
    onTabChanged: Any
    _createdTabs: Any
    _isAnimationEnabled: Any
    paramsView: Any
    _isContentVisible: Any
    def __init__(self, layoutID, **kwargs):
        ...
    def updateTankmanId(self, tankmanInvID):
        ...
    def updateTabId(self, tabID):
        ...
    def updateTTCWithSkillName(self, skillName):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def currentTabId(self):
        ...
    def toggleContentVisibility(self, isVisible):
        ...
    def setAnimationInProgress(self, isEnabled):
        ...
    def _onEmptySlotAutoSelect(self, _):
        ...
    def _setWidgets(self, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self, vm):
        ...
    def _setBackButtonLabel(self, vm):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _finalize(self):
        ...
    def _onClose(self, params=None):
        ...
    def widgetAutoSelectSlot(self, **kwargs):
        ...
    def _onFocus(self, focused):
        ...
    def _onTabChange(self, args):
        ...
    def _onTankmanSlotAutoSelect(self, tankmanInvID, slotIdx):
        ...
    def _onTankmanSlotClick(self, tankmanInvID, _):
        ...
    def _onEmptySlotClick(self, tankmanID, slotIdx):
        ...
    def _onSkinsUpdate(self, _):
        ...
    def __onAccountSettingsChanging(self, key, _):
        ...
    def __updateNewSkinsCounter(self):
        ...
    def __getNewSkinsAmount(self):
        ...
    def __selectTankman(self, tankmanInvID):
        ...
    def __changeTab(self, tabID):
        ...
    def __updateTabs(self, tankmanInvID):
        ...
    def __stopAnimations(self):
        ...
    def __createTab(self, tabId):
        ...
