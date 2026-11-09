# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/register_additional_params.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_hints import battle_hints_overlap_controller as battle_hints_overlap_controller
from halloween.gui.halloween_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, HWDailyQuestDecorationMap as HWDailyQuestDecorationMap
from halloween.gui.shared.utils import checkAbilities as checkAbilities
from helpers import dependency as dependency
from gui.prb_control.prb_utils import addSupportedQueues as addSupportedQueues, addArenaGUITypeByQueueType as addArenaGUITypeByQueueType, addQueueTypeToPrbType as addQueueTypeToPrbType
from gui.prb_control.settings import PREBATTLE_TYPE_TO_QUEUE_TYPE as PREBATTLE_TYPE_TO_QUEUE_TYPE
from halloween.messenger.formatters.invites import HalloweenPrbInviteHtmlTextFormatter as HalloweenPrbInviteHtmlTextFormatter
from halloween.gui import halloween_gui_constants as halloween_gui_constants
from halloween.gui.prb_control.entities.pre_queue.entity import canSelectPrbEntity as canSelectPrbEntity, HalloweenEntity as HalloweenEntity
from halloween_common.halloween_constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.impl.lobby.platoon.platoon_config import addQueueTypeToPrbSquadActionName as addQueueTypeToPrbSquadActionName
from gui.impl.lobby.tank_setup.backports.context_menu import TANK_SETUP_CARD_CM as TANK_SETUP_CARD_CM, TANK_SETUP_SLOT_CM as TANK_SETUP_SLOT_CM, HANGAR_TANK_SETUP_SLOT_CM as HANGAR_TANK_SETUP_SLOT_CM
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VEHICLE_PREVIEW_ALIASES as VEHICLE_PREVIEW_ALIASES
from halloween.gui.scaleform.genConsts.HALLOWEEN_CM_HANDLER_TYPE import HALLOWEEN_CM_HANDLER_TYPE as HALLOWEEN_CM_HANDLER_TYPE
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES as HALLOWEEN_HANGAR_ALIASES
from gui.impl.lobby.tank_setup.backports.tooltips import PANEL_SLOT_TOOLTIPS as PANEL_SLOT_TOOLTIPS
from halloween.gui.impl.lobby.tank_setup.backports.tooltips import HWConsumableTooltipBuilder as HWConsumableTooltipBuilder
from gui.shared.gui_items.items_actions.factory import _ACTION_MAP as _ACTION_MAP
from halloween.gui.shared.gui_items.items_actions import actions as actions
from halloween.gui.impl.lobby.tank_setup.interactor import BUY_AND_INSTALL_HW_CONSUMABLES_ACTION as BUY_AND_INSTALL_HW_CONSUMABLES_ACTION
from gui.impl.lobby.tank_setup.dialogs.confirm_dialog import _SECTION_TO_FITTING_TYPE as _SECTION_TO_FITTING_TYPE
from halloween.gui.impl.lobby.tank_setup import HWTankSetupConstants as HWTankSetupConstants, HWFittingTypes as HWFittingTypes
from gui.shared.system_factory import registerHitDirectionController as registerHitDirectionController, registerPrbInviteHtmlFormatter as registerPrbInviteHtmlFormatter, registerIgnoredModeForAutoSelectVehicle as registerIgnoredModeForAutoSelectVehicle, registerReadyVehicleChekers as registerReadyVehicleChekers
from halloween.gui.battle_control.controllers.hit_direction_ctrl.hw_ctrl import HWHitDirectionController as HWHitDirectionController, HWHitDirectionControllerPlayer as HWHitDirectionControllerPlayer
from messenger.m_constants import LAZY_CHANNEL as LAZY_CHANNEL
from messenger.ext.channel_num_gen import _CHANNEL_LAZY_ORDER as _CHANNEL_LAZY_ORDER, _LAZY_CLIENT_IDS as _LAZY_CLIENT_IDS
from soft_exception import SoftException as SoftException
from web.web_client_api.ui import OpenTabWebApi as OpenTabWebApi
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController

def _registerHWOpenTabWebApi():
    ...
def registerAdditionalParams(personality):
    ...
def registerLazyChannelParam(extChannelConst, personality):
    ...
def initAdditionalGuiTypes(guiConstants, personality):
    ...
def registerConditionFormatterIcons():
    ...
def registerDailyQuestDecorationMap(personality):
    ...
