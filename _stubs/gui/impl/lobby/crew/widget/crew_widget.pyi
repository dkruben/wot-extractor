# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/widget/crew_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from itertools import chain as chain
from helpers.dependency import descriptor as descriptor
from typing import TYPE_CHECKING as TYPE_CHECKING, NamedTuple as NamedTuple, Generator as Generator
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CREW_BOOKS_VIEWED as CREW_BOOKS_VIEWED
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, PyResAccessor as PyResAccessor
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl import backport as backport
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from gui.impl.backport import BackportContextMenuWindow as BackportContextMenuWindow, createContextMenuData as createContextMenuData
from gui.impl.backport.backport_pop_over import BackportPopOverContent as BackportPopOverContent, createPopOverData as createPopOverData
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.button_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_model import CrewWidgetModel as CrewWidgetModel, SlotSizeMode as SlotSizeMode
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_slot_model import CrewWidgetSlotModel as CrewWidgetSlotModel
from gui.impl.gen.view_models.views.lobby.crew.common.toggle_button_model import ToggleState as ToggleState
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.impl.gen.view_models.views.lobby.crew.idle_crew_bonus import IdleCrewBonusEnum as IdleCrewBonusEnum
from gui.impl.lobby.crew.crew_header_tooltip_view import CrewHeaderTooltipView as CrewHeaderTooltipView
from gui.impl.lobby.crew.crew_helpers.model_setters import setTmanSkillsModel as setTmanSkillsModel, setTmanMajorSkillsModel as setTmanMajorSkillsModel, setTmanBonusSkillsModel as setTmanBonusSkillsModel
from gui.impl.lobby.crew.crew_helpers.skill_formatters import SkillLvlFormatter as SkillLvlFormatter
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getTmanNewSkillCount as getTmanNewSkillCount, getSkillsLevelsForXp as getSkillsLevelsForXp
from gui.impl.lobby.crew.tooltips.empty_skill_tooltip import EmptySkillTooltip as EmptySkillTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, checkForTags as checkForTags
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN, NO_SLOT as NO_SLOT, SKILL_EFFICIENCY_UNTRAINED as SKILL_EFFICIENCY_UNTRAINED, getTankmanSkill as getTankmanSkill, Tankman as Tankman
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName, getLowEfficiencyCrew as getLowEfficiencyCrew, NO_VEHICLE_ID as NO_VEHICLE_ID, VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.gui_items.processors.vehicle import VehicleTmenXPAccelerator as VehicleTmenXPAccelerator
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils import decorators as decorators
from helpers import dependency as dependency, int2roman as int2roman
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL, getLessMasteredIDX as getLessMasteredIDX, sortTankmanRoles as sortTankmanRoles
from renewable_subscription_common.passive_xp import isTagsSetOk as isTagsSetOk
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_tankman_model import CrewWidgetTankmanModel as CrewWidgetTankmanModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_model import CrewSkillModel as CrewSkillModel
from typing import Union as Union
BuildedMessage: Any
DOG = 'dog'

class CrewWidget(ViewImpl, IGlobalListener):
    __slots__: tuple
    LAYOUT_DYN_ACCESSOR = R.views.lobby.crew.widgets.CrewWidget
    PREBATTLE_TYPE_TO_SLOT_MODE: dict
    DEFAULT_SLOT_MODE = SlotSizeMode.DEFAULT
    itemsCache: Any
    wotPlusCtrl: Any
    appLoader: Any
    onSlotTrySelect: Any
    onSlotClick: Any
    onChangeCrewClick: Any
    __toolTipMgr: Any
    __currentViewID: Any
    __previousViewID: Any
    __isButtonBarVisible: Any
    __currentTankman: Any
    __currentVehicle: Any
    __currentSlotIdx: Any
    def __init__(self, tankmanID=..., vehicleInvID=..., slotIdx=..., currentViewID=None, previousViewID=None, isButtonBarVisible=True):
        ...
    def getWidgetData(self):
        ...
    def updateTankmanId(self, tankmanID):
        ...
    def updateVehicleInvID(self, vehicleInvID):
        ...
    def updateSlotIdx(self, slotIdx):
        ...
    def updateDisableState(self, isDisabled):
        ...
    def updateVmSlotsData(self, vmSlotsList):
        ...
    def onPrbEntitySwitched(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def currentViewID(self):
        ...
    def setCurrentViewID(self, value):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createContextMenu(self, event):
        ...
    def createPopOverContent(self, event):
        ...
    def getSlotIdxByTankmanID(self, tankmanID):
        ...
    @staticmethod
    def _getContextMenuType():
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    def _updateButtonsBar(self, vmButtonsBar, isCrewEmpty=True):
        ...
    def _getTankmanSkillProgress(self, tman):
        ...
    def _getLastSkillLevelFormat(self, lastSkillLevel):
        ...
    def __updateWidgetModel(self):
        ...
    def __setSlotMode(self):
        ...
    def __updateWidgetModelByVehicle(self, vm):
        ...
    def __updateWidgetModelByTankman(self, vm):
        ...
    def __getSlotIdxByTankmanID(self, tankmanID):
        ...
    def __onVehicleDossierUpdate(self, diff=None):
        ...
    def __idleCrewXPUpdated(self, diff):
        ...
    def __updateTankmen(self, diff=None):
        ...
    def __checkIsTankmanUpdated(self, diff):
        ...
    def __onChangeCrewClick(self, args):
        ...
    def _onSlotClick(self, args):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __onAccountSettingsChanging(self, key, _):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __findTmanData(self):
        ...
    def __fillVehicleInfo(self, vm):
        ...
    def __fillSlotsList(self, vmSlotsList, lessMastered):
        ...
    def _fillTankmanModel(self, vmTankman, tman, isLessMastered=False):
        ...
    def __checkDog(self, vm):
        ...
    def __updateWotPlusButtonModel(self, vmWotPlusButton):
        ...
    def __onDogMoreInfoClick(self):
        ...
    def __onCrewBooksClick(self):
        ...
    # decorador original: @wg_async
    def __onAcceleratedTrainingClick(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __onAccelerateCrewTrainingConfirmed(self, vehicle, wasActive):
        ...
    # decorador original: @wg_async
    def __onWotPlusClick(self):
        ...
    def __buildConfirmationMessage(self):
        ...
    def __getIdleCrewState(self):
        ...
    def __updateCrewBooksAmount(self, vmCrewBooks):
        ...
    def __updateCrewBooksDiscount(self, vmCrewBooks):
        ...

class QuickTrainingCrewWidget(CrewWidget):
    __slots__: tuple
    _cachePossibleSkillsLevels: Any
    _cachePossibleSkillsEfficiency: Any
    def __init__(self, tankmanID=..., vehicleInvID=..., slotIdx=..., currentViewID=None, previousViewID=None, isButtonBarVisible=True):
        ...
    def clearPossibleSkillsLevelCache(self):
        ...
    def updateVmSlotsData(self, vmSlotsList):
        ...
    def updatePossibleSkillsLevel(self, possibleSkillsLevels, skillsEffLevels):
        ...
    def _finalize(self):
        ...
    def _updateButtonsBar(self, vmButtonsBar, isCrewEmpty=True):
        ...
    def _onSlotClick(self, args):
        ...
    def _getTankmanSkillProgress(self, tman):
        ...
    def _getLastSkillLevelFormat(self, lastSkillLevel):
        ...
    def __updatePossibleSkillsEfficiency(self, vmSlots):
        ...
    def __updatePossibleSkillsViewModel(self, vmSlots):
        ...

class SkillsTrainingCrewWidget(CrewWidget):
    def updateSelectedSkills(self, tankman, selectedSkills, role):
        ...
    def _fillTankmanModel(self, vmTankman, tman, isLessMastered=False):
        ...
