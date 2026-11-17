# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/mentor_assigment_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional
import SoundGroups as SoundGroups
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowLayer as WindowLayer, WindowFlags as WindowFlags
from goodies import goodie_constants as goodie_constants
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.dialogs.dialogs import showMentorAssignmentConfirmDialog as showMentorAssignmentConfirmDialog
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.info_tip_model import InfoTipModel as InfoTipModel, TipType as TipType
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.mentor_assigment_tankman_model import MentorAssigmentTankmanModel as MentorAssigmentTankmanModel
from gui.impl.gen.view_models.views.lobby.crew.mentor_assigment_view_model import MentorAssigmentViewModel as MentorAssigmentViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanCardState as TankmanCardState
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.crew.base_crew_view import BaseCrewView as BaseCrewView
from gui.impl.lobby.crew.base_tankman_list_view import BaseTankmanListView as BaseTankmanListView
from gui.impl.lobby.crew.crew_helpers.model_setters import setTankmanModel as setTankmanModel, setTmanSkillsModel as setTmanSkillsModel
from gui.impl.lobby.crew.crew_helpers.skill_helpers import quickEarnCrewSkills as quickEarnCrewSkills, quickEarnTmanSkills as quickEarnTmanSkills
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.impl.lobby.crew.filter import getTankmanRoleSettings as getTankmanRoleSettings, getVehicleTypeSettings as getVehicleTypeSettings, getVehicleTierSettings as getVehicleTierSettings, getTankmanLocationSettings as getTankmanLocationSettings
from gui.impl.lobby.crew.filter.data_providers import MentorDataProvider as MentorDataProvider
from gui.impl.lobby.crew.filter.filter_panel_widget import FilterPanelWidget as FilterPanelWidget
from gui.impl.lobby.crew.filter.state import FilterState as FilterState
from gui.impl.lobby.crew.tooltips.mentoring_license_tooltip import MentoringLicenseTooltip as MentoringLicenseTooltip
from gui.impl.lobby.crew.utils import getMetoringLicensesAmount as getMetoringLicensesAmount
from gui.impl.pub import WindowImpl as WindowImpl
from gui.shared.event_dispatcher import showChangeCrewMember as showChangeCrewMember
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN, NO_SLOT as NO_SLOT
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from gui.shared.gui_items.items_actions import factory as factory
from helpers import dependency as dependency, i18n as i18n
from nations import NAMES as NAMES
from skeletons.gui.game_control import IRestoreController as IRestoreController
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.impl.lobby.crew.widget.crew_widget import QuickTrainingCrewWidget as CrewWidgetType
_POPOVER_GROUP_SETTINGS: tuple
_DEFAULT_TIP_ID = 0
_LOST_XP_TIP_ID = 1

class MentorAssigmentView(BaseCrewView, BaseTankmanListView):
    restore: Any
    itemsCache: Any
    __slots__: tuple
    __parent: Any
    __tankmanInvID: Any
    __tankman: Any
    __vehicleInvID: Any
    __nation: Any
    __hasActiveCard: Any
    __activeCardTotalXp: Any
    __filterState: Any
    __dataProvider: Any
    __filterPanelWidget: Any
    __isDefaultTipVisible: Any
    __isDefaultTipShown: Any
    _crewWidget: Any
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def _tankman(self):
        ...
    @property
    def _vehicle(self):
        ...
    @property
    def _crew(self):
        ...
    def _getCrewWidgetBaseData(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _updateTankmanData(self):
        ...
    def _setWidgets(self, **kwargs):
        ...
    def _onVehicleLockChanged(self, _, lockReason):
        ...
    def _onEmptySlotClick(self, tankmanID, slotIdx):
        ...
    def _onTankmanSlotClick(self, tankmanInvID, slotIdx):
        ...
    def _isCrewWidgetButtonBarVisible(self):
        ...
    @property
    def _tankmenProvider(self):
        ...
    @property
    def _recruitsProvider(self):
        ...
    @property
    def _filterState(self):
        ...
    def _fillTankmanCard(self, cardsList, tankman):
        ...
    def _fillRecruits(self, cardsList, limit, offset):
        ...
    def _destroyParentView(self):
        ...
    # decorador original: @wg_async
    # decorador original: @args2params(...)
    def _onTankmanSelected(self, tankmanID):
        ...
    # decorador original: @args2params(...)
    def _onCardMouseEnter(self, totalXP):
        ...
    def _onCardMouseLeave(self):
        ...
    # decorador original: @args2params(...)
    def _onTipClose(self, tipId):
        ...
    def _onTipsReadyToShow(self):
        ...
    def _onClose(self, params=None):
        ...
    def _onBack(self):
        ...
    def _onFilterStateUpdated(self):
        ...
    def _fillRecruitCard(self, cardsList, recruitInfo):
        ...
    def _fillViewModel(self, vm):
        ...
    def _fillTankmenList(self, tx):
        ...
    def _setBackButtonLabel(self, vm):
        ...
    def __fillTips(self):
        ...
    def __clearWidgetPossibleSkillsLevel(self):
        ...
    def __onGoodiesUpdate(self, diff):
        ...
    def __onInventoryUpdate(self, invDiff):
        ...
    def __onDisconnected(self):
        ...
    def __onResetFilters(self):
        ...

class MentorAssigmentWindow(WindowImpl):
    def __init__(self, **kwargs):
        ...
