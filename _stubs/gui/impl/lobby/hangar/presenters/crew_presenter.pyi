# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/crew_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
import typing as typing
from enum import Enum as Enum
from future.utils import itervalues as itervalues, iteritems as iteritems
from typing import NamedTuple as NamedTuple, Union as Union
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from cgf_components.marker_component import IGuiLoader as IGuiLoader
from frameworks.wulf import PyResAccessor as PyResAccessor
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants as CrewConstants
from gui.impl.gen.view_models.views.lobby.loadout.crew.bonus_skills_model import BonusSkillsModel as BonusSkillsModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.crew_model import CrewModel as CrewModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.perk_model import PerkModel as PerkModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel as SlotModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.tankman_model import TankmanModel as TankmanModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.vehicle_bonus_detail_model import VehicleBonusDetailModel as VehicleBonusDetailModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.lobby.crew.crew_header_tooltip_view import CrewHeaderTooltipView as CrewHeaderTooltipView
from gui.impl.lobby.crew.tooltips.empty_skill_tooltip import EmptySkillTooltip as EmptySkillTooltip
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getTmanNewSkillCount as getTmanNewSkillCount, isTankmanSkillIrrelevant as isTankmanSkillIrrelevant
from gui.impl.lobby.crew.widget.crew_widget import BuildedMessage as BuildedMessage
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.event_dispatcher import showBarracks as showBarracks, showChangeCrewMember as showChangeCrewMember, showPersonalCase as showPersonalCase
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import NO_TANKMAN as NO_TANKMAN, Tankman as Tankman
from gui.shared.gui_items.Vehicle import getIconResourceName as getIconResourceName
from gui.shared.gui_items.processors.vehicle import VehicleTmenXPAccelerator as VehicleTmenXPAccelerator
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils import decorators as decorators
from helpers.dependency import descriptor as descriptor
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency, int2roman as int2roman
from items.special_crew import CustomSkills as CustomSkills
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL, getLessMasteredIDX as getLessMasteredIDX
from nations import AVAILABLE_NAMES as AVAILABLE_NAMES
from renewable_subscription_common.passive_xp import isTagsSetOk as isTagsSetOk
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.shared.gui_items.artefacts import BattleBooster as BattleBooster
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from frameworks.wulf import Array as Array
DOG = 'dog'
BuiltMessage: Any

class IdleCrewBonus(Enum):
    DISABLED = 'Disabled'
    ENABLED = 'Enabled'
    ACTIVE_ON_CURRENT_VEHICLE = 'ActiveOnCurrentVehicle'
    INCOMPATIBLE_WITH_CURRENT_VEHICLE = 'IncompatibleWithCurrentVehicle'
    ACTIVE_ON_ANOTHER_VEHICLE = 'ActiveOnAnotherVehicle'
    INVISIBLE = 'Invisible'

# base nao representavel no stub: ViewComponent[...]
class CrewPresenter:
    __itemsCache: Any
    __wotPlusCtrl: Any
    __lobbyContext: Any
    appLoader: Any
    __toolTipMgr: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def finalize(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getCallbacks(self):
        ...
    def __idleCrewXPUpdated(self, diff):
        ...
    def _getEvents(self):
        ...
    def _getCrewPanelState(self):
        ...
    def _createTankmanModel(self, tman, battleBoosterBonus, isQuickTrainingEnabled, vehicleBonusDetails, vehicleCrewBoosterBonusDetails, optDeviceBonuses):
        ...
    # decorador original: @wg_async
    def __onToggleIntensiveTraining(self):
        ...
    def __buildConfirmationMessage(self):
        ...
    def __onWotPlusStatusChanged(self, _):
        ...
    # decorador original: @wg_async
    def __onToggleAcceleratedTraining(self):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __onAccelerateCrewTrainingConfirmed(self, vehicle, wasActive):
        ...
    def __getIdleCrewState(self):
        ...
    def __onOpenCrew(self, ctx):
        ...
    def __onOpenBarracks(self, ctx):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __onVehicleChanged(self):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __updateModel(self):
        ...
    def __findLessMasteredTman(self):
        ...
    def __updateCrewModel(self):
        ...
    def __getVehicleCrewBoosters(self, vehicle):
        ...
    def __calcVehicleBonusDetails(self, vehicle):
        ...
    def __calcOptDeviceBonuses(self, vehicle):
        ...
    def __calcVehicleBooster(self, vehicle):
        ...
    def __addMajorSkills(self, tman, model):
        ...
    def __addBonusSkills(self, tman, model):
        ...
    def __addSkills(self, tman, skills, container):
        ...
    def __addPerkModel(self, skill, state, container):
        ...
    def __createVehicleBonusDetail(self, name, bonusType, bonus):
        ...
    def __setBrotherhoodBonus(self, model, tankman):
        ...
    def __setCommanderBonus(self, model, tankman):
        ...
    def __setEquipmentsBonuses(self, man, tankman, battleBoosterBonus, vehicleBonusDetails, vehicleCrewBoosterBonusDetails, optDeviceBonuses):
        ...
    @staticmethod
    def __isTankmanTrainedForVehicle(tman):
        ...
    @staticmethod
    def __getPerkState(skill, tman):
        ...
    def __updateAcceleratedTraining(self):
        ...
    def __updateIntensiveTraining(self):
        ...
    def __onDogMoreInfoClick(self):
        ...

def setCrewSlots(slots, vehicle):
    ...
