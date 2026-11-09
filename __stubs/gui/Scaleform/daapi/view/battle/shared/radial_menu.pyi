# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/radial_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from future.utils import lmap as lmap
import GUI as GUI
import Keys as Keys
import CommandMapping as CommandMapping
from AvatarInputHandler import aih_global_binding as aih_global_binding
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, ReplyState as ReplyState, MarkerType as MarkerType, DefaultMarkerSubType as DefaultMarkerSubType, ONE_SHOT_COMMANDS_TO_REPLIES as ONE_SHOT_COMMANDS_TO_REPLIES, INVALID_MARKER_SUBTYPE as INVALID_MARKER_SUBTYPE, LocationMarkerSubType as LocationMarkerSubType
from gui.Scaleform.daapi.view.meta.RadialMenuMeta import RadialMenuMeta as RadialMenuMeta
from gui.Scaleform.genConsts.RADIAL_MENU_CONSTS import RADIAL_MENU_CONSTS as RADIAL_MENU_CONSTS
from gui.Scaleform.locale.INGAME_HELP import INGAME_HELP as INGAME_HELP
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.battle_control import event_dispatcher as gui_event_dispatcher, avatar_getter as avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from gui.battle_control.controllers.chat_cmd_ctrl import KB_MAPPING as KB_MAPPING
from gui.shared.SoundEffectsId import SoundEffectsId as SoundEffectsId
from gui.shared.utils.key_mapping import getScaleformKey as getScaleformKey, BW_TO_SCALEFORM as BW_TO_SCALEFORM
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from uilogging.player_satisfaction_rating.loggers import RadialMenuLogger as RadialMenuLogger
_logger: Any
_SHORTCUTS_IN_GROUP = 6
Shortcut: Any
CrosshairData: Any
REGULAR_BOTTOM_STATIC_SHORTCUTS: tuple
REGULAR_UPPER_STATIC_SHORTCUTS: tuple
ALLY_UPPER_SHORTCUTS_DEFAULT: tuple
ALLY_UPPER_SHORTCUTS_ONE_DISABLED: tuple
ALLY_UPPER_SHORTCUTS_THREE_DISABLED: tuple
_MARKERS_TYPE_TO_SUBTYPE_MAP: dict
_MESSAGE_TO_RELOAD_MAP: dict
_CAN_CANCEL_REPLY_SHORTCUT: Any
_CONFIRM_SHORTCUT: Any
_THANKS_SHORTCUT: Any
_EMPTY_BUTTON_SHORTCUT: Any

class RadialMenu(RadialMenuMeta, BattleGUIKeyHandler, CallbackDelayer):
    sessionProvider: Any
    _aimOffset: Any
    _REFRESH_TIME_IN_SECONDS = 0.3
    _CMD_CHAT_SHORTCUT_CONTEXT_COMMAND: tuple
    _CMD_CHAT_SHORTCUT_CONTEXT_COMMIT: tuple
    _ALL_TARGET_STATES = RADIAL_MENU_CONSTS.ALL_TARGET_STATES
    bottomShortcutSets: Any
    upperShortcutSets: Any
    __crosshairData: Any
    __stateData: Any
    __isVisible: Any
    __hideReshow: Any
    _uiPlayerSatisfactionRatingLogger: Any
    def __init__(self):
        ...
    def handleEscKey(self, isDown):
        ...
    def onAction(self, action):
        ...
    def getKeyFromAction(self, action):
        ...
    def onSelect(self):
        ...
    def onHideCompleted(self):
        ...
    def onRefresh(self):
        ...
    def show(self, reshowPreviousState=False):
        ...
    def hide(self, allowAction=True):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _initShortCuts(self):
        ...
    def _showInternal(self, radialState, staticDiff, replyDiff, position):
        ...
    def _getCanCancelReplyShortcut(self):
        ...
    def _getConfirmShortcut(self):
        ...
    def _getCanReplayShortcut(self, shortcut, canReplyAction):
        ...
    def __setVisibility(self, newState):
        ...
    def __onMappingChanged(self, *args):
        ...
    def __refreshShortcutsAndState(self):
        ...
    def __createShortcut(self, shortcutData):
        ...
    def __getRadialMenuState(self, targetID, targetMarkerType, targetMarkerSubtype, replyState, replyToAction):
        ...
    def __playSound(self, soundName):
        ...
    def __generateStaticDiffDict(self, menuState):
        ...
    def __generateDiffStateDict(self, targetState, replyState, replyAction, targetID):
        ...
    def __populateBottomRowData(self, resultingDiffList, menuState, message):
        ...
    def __populateWithNonAllyData(self, replyState, resultingDiffList, targetState):
        ...
    def __populateWithAllyData(self, replyAction, replyState, resultingDiffList, targetID):
        ...
    def __adjustPrimaryRadialButton(self, replyState, shortcut, canReplyAction):
        ...
    def __adjustReloadRadialButton(self, shortcut, message):
        ...
    def __handleSpgView(self, resultingDiffList, targetState):
        ...
    def __disableButton(self, buttonData):
        ...
    def __unbindKeyShortcutFromButton(self, buttonData):
        ...
    @staticmethod
    def __copyShortcutData(buttonData, shortcut):
        ...
    def __onReplyFeedbackReceived(self, uniqueTargetID, replierID, markerType, oldReplyCount, newReplyCount):
        ...
    def __onRemoveCommandReceived(self, removedID, markerType):
        ...
    def __reshow(self, removedID, markerType, reshowPreviousState):
        ...
    def __onVehicleMarkerRemoved(self, vehicleID):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __onAddCommandReceived(self, addedID, markerType):
        ...
    def __checkForValidLocationMarkerLoop(self):
        ...
    def __checkForTemporaryRespondUpdateLoop(self):
        ...
    @staticmethod
    def __isMarkerEmptyLocationOrOutOfBorder(markerType, markerSubType):
        ...
    @staticmethod
    def __isCanRespondToAlly(markerType, markerSubType, replyState):
        ...
