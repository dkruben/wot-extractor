# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/postmortem_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import WWISE as WWISE
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import ATTACK_REASON_INDICES as ATTACK_REASON_INDICES, ATTACK_REASON as ATTACK_REASON, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.components_packer import unpack_component as unpack_component, pack_component as pack_component
from dog_tags_common.player_dog_tag import PlayerDogTag as PlayerDogTag, DisplayableDogTag as DisplayableDogTag
from gui import makeHtmlString as makeHtmlString
from dog_tags_common.config.common import ComponentPurpose as ComponentPurpose, ComponentViewType as ComponentViewType
from gui.Scaleform.daapi.view.battle.shared.formatters import normalizeHealthPercent as normalizeHealthPercent
from gui.Scaleform.daapi.view.meta.PostmortemPanelMeta import PostmortemPanelMeta as PostmortemPanelMeta
from gui.Scaleform.settings import ICONS_SIZES as ICONS_SIZES
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.dog_tag_composer import layoutComposer as layoutComposer
from gui.battle_control.controllers.kill_cam_ctrl import KillCamInfoMarkerType as KillCamInfoMarkerType
from gui.doc_loaders import messages_panel_reader as messages_panel_reader
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.badges import buildBadge as buildBadge
from gui.shared.events import DeathCamEvent as DeathCamEvent
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.gui_items.Vehicle import getSmallIconPath as getSmallIconPath, getIconResourceName as getIconResourceName
from gui.shared.view_helpers import UsersInfoHelper as UsersInfoHelper
from helpers import dependency as dependency
from helpers import int2roman as int2roman
from items import vehicles as vehicles
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Iterable as Iterable, Optional as Optional
_logger: Any
_POSTMORTEM_PANEL_SETTINGS_PATH = 'gui/postmortem_panel.xml'
_VEHICLE_SMALL_ICON_RES_PATH = '../maps/icons/vehicle/small/{0}.png'
_BR_VEHICLE_SMALL_ICON_RES_PATH = '../maps/icons/battleRoyale/vehicles/{0}.png'
_ATTACK_REASON_CODE_TO_MSG: dict
_ALLOWED_EQUIPMENT_DEATH_CODES: list

class _ENTITIES_POSTFIX(object):
    UNKNOWN = '_UNKNOWN'
    SELF_SUICIDE = '_SELF_SUICIDE'
    ALLY_SELF = '_ALLY_SELF'
    ENEMY_SELF = '_ENEMY_SELF'

class _BasePostmortemPanel(PostmortemPanelMeta):
    __slots__: tuple
    sessionProvider: Any
    settingsCore: Any
    _messages: Any
    _deathInfo: Any
    def __init__(self):
        ...
    def getDeathInfo(self):
        ...
    def resetDeathInfo(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def _deathInfoReceived(self):
        ...
    def _prepareMessage(self, code, killerVehID, device=None):
        ...
    def _onShowVehicleMessageByCode(self, code, postfix, entityID, extra, equipmentID, ignoreMessages):
        ...
    def _getDevice(self, extra):
        ...

class _SummaryPostmortemPanel(_BasePostmortemPanel):
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def __onPostmortemSummaryReceived(self, postmortemSummaryEvent):
        ...
    def __prepareMessageFromSummary(self, vehID, deathReasonCode):
        ...
    def __getPostfixByKiller(self, killerVehID):
        ...

class PostmortemPanel(_SummaryPostmortemPanel):
    __slots__: tuple
    __playerInfo: Any
    _isPlayerVehicle: Any
    _maxHealth: Any
    __healthPercent: Any
    _isInPostmortem: Any
    _deathAlreadySet: Any
    __isColorBlind: Any
    __userInfoHelper: Any
    __arenaInfo: Any
    __isPostmortemEnabled: Any
    __wasPostmortemInfoHidden: Any
    def __init__(self):
        ...
    def changeCtrlMode(self, ctrlMode):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def _deathInfoReceived(self):
        ...
    def _preloadDTImages(self, usedDogTagsComponents, skipSameTeam=True):
        ...
    @staticmethod
    def _hasBonusCap(cap):
        ...
    def _setHealthPercent(self, health):
        ...
    def __setPlayerInfo(self, vehicleID):
        ...
    def _onVehicleControlling(self, vehicle):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def __onRespawnBaseMoving(self):
        ...
    def _updateVehicleInfo(self):
        ...
    def _showOwnDeathInfo(self):
        ...
    def _setDeadReasonInfo(self, vInfoVO, reason, showVehicle, vehLvl, vehImg, vehClass, vehName, killerUserVO):
        ...
    def _makeKillerVO(self, vInfoVO):
        ...
    def _makeReasonInfo(self, deathInfo):
        ...
    def _showPlayerInfo(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def onDogTagKillerInPlaySound(self):
        ...
    def onDogTagKillerOutPlaySound(self):
        ...
    def onVictimDogTagInPlaySound(self):
        ...
    @staticmethod
    def _buildDogTag(dogTag):
        ...
    def __onKillerDogTagSet(self, dogTagInfo):
        ...
    def __onVictimDogTagSet(self, dogTagInfo):
        ...
    def __onKillerDogCheat(self, deadReasonInfo):
        ...
    def __onUsedComponentsUpdated(self, usedComponents):
        ...
    def __onKillCamStateChanged(self, killCamState, totalSceneDuration):
        ...
    def __onMarkerDisplayChanged(self, markerState, ctx):
        ...
    def __isSimpleDeathCam(self):
        ...
