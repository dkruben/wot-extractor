# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/register_additional_params.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from future.utils import viewvalues as viewvalues
from helpers import dependency as dependency
from gui.prb_control.prb_utils import addSupportedQueues as addSupportedQueues, addArenaGUITypeByQueueType as addArenaGUITypeByQueueType, addQueueTypeToPrbType as addQueueTypeToPrbType
from gui.prb_control.settings import PREBATTLE_TYPE_TO_QUEUE_TYPE as PREBATTLE_TYPE_TO_QUEUE_TYPE
from last_stand.gui.shared.utils import checkAbilities as checkAbilities
from last_stand.messenger.formatters.invites import LSPrbInviteHtmlTextFormatter as LSPrbInviteHtmlTextFormatter
from last_stand.gui.prb_control.entities.pre_queue.entity import canSelectPrbEntity as canSelectPrbEntity, LastStandEntity as LastStandEntity
from last_stand_common.last_stand_constants import QUEUE_TYPE as QUEUE_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE, PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.impl.lobby.platoon.platoon_config import addQueueTypeToPrbSquadActionName as addQueueTypeToPrbSquadActionName
from gui.impl.lobby.tank_setup.backports.context_menu import TANK_SETUP_CARD_CM as TANK_SETUP_CARD_CM, TANK_SETUP_SLOT_CM as TANK_SETUP_SLOT_CM, HANGAR_TANK_SETUP_SLOT_CM as HANGAR_TANK_SETUP_SLOT_CM
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from last_stand.gui.scaleform.genConsts.LS_CM_HANDLER_TYPE import LS_CM_HANDLER_TYPE as LS_CM_HANDLER_TYPE
from gui.impl.lobby.tank_setup.backports.tooltips import PANEL_SLOT_TOOLTIPS as PANEL_SLOT_TOOLTIPS
from last_stand.gui.impl.lobby.tank_setup.backports.tooltips import LSConsumableTooltipBuilder as LSConsumableTooltipBuilder
from gui.shared.gui_items.items_actions.factory import _ACTION_MAP as _ACTION_MAP
from last_stand.gui.shared.gui_items.items_actions import actions as actions
from last_stand.gui.impl.lobby.tank_setup.interactor import ActionTypes as ActionTypes
from gui.impl.lobby.tank_setup.dialogs.confirm_dialog import _SECTION_TO_FITTING_TYPE as _SECTION_TO_FITTING_TYPE
from last_stand.gui.impl.lobby.tank_setup import LSTankSetupConstants as LSTankSetupConstants, LSFittingTypes as LSFittingTypes
from gui.shared.system_factory import registerHitDirectionController as registerHitDirectionController, registerPrbInviteHtmlFormatter as registerPrbInviteHtmlFormatter, registerLobbyTooltipsBuilders as registerLobbyTooltipsBuilders, registerIgnoredModeForAutoSelectVehicle as registerIgnoredModeForAutoSelectVehicle, registerReadyVehicleChekers as registerReadyVehicleChekers, registerTeamVoipSupport as registerTeamVoipSupport
from last_stand.gui.battle_control.controllers.hit_direction_ctrl.ls_ctrl import LSHitDirectionController as LSHitDirectionController, LSHitDirectionControllerPlayer as LSHitDirectionControllerPlayer
from messenger.m_constants import LAZY_CHANNEL as LAZY_CHANNEL
from messenger.ext.channel_num_gen import _CHANNEL_LAZY_ORDER as _CHANNEL_LAZY_ORDER, _LAZY_CLIENT_IDS as _LAZY_CLIENT_IDS
from personal_missions_constants import CONDITION_ICON as CONDITION_ICON
from soft_exception import SoftException as SoftException
from web.web_client_api.ui import OpenTabWebApi as OpenTabWebApi
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.gui.ls_gui_constants import LSDailyQuestDecorationMap as LSDailyQuestDecorationMap, LS_TOOLTIP_SET as LS_TOOLTIP_SET, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME, FUNCTIONAL_FLAG as FUNCTIONAL_FLAG

def _registerLSOpenTabWebApi():
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
