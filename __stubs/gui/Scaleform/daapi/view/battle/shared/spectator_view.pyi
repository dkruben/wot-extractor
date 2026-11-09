# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/spectator_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from AvatarInputHandler.control_modes import DeathFreeCamMode as DeathFreeCamMode
from helpers import dependency as dependency, time_utils as time_utils
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.controllers.spectator_ctrl import ISpectatorViewListener as ISpectatorViewListener
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.meta.SpectatorViewMeta import SpectatorViewMeta as SpectatorViewMeta
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any
_MovementKeyBindings: Any

class SPECTATOR_VIEW_SOUND(object):
    SPEED_CHANGE = 'dc_fc_speed_change'
    FOLLOW_HINT = 'dc_fc_follow_hint'
    START_TO_FOLLOW_TANK = 'dc_fc_start_to_follow_tank'
    STOP_TO_FOLLOW_TANK = 'dc_fc_stop_to_follow_tank'

class SpectatorView(SpectatorViewMeta, ISpectatorViewListener, CallbackDelayer):
    sessionProvider: Any
    DELAY_HINT_MOVEMENT = 3
    DELAY_HINT_SPEED = 4
    __RETURN_TO_PREVIOUS_VEHICLE_HINT_DURATION = 10
    __followHintSound: Any
    __isInRespawn: Any
    __hintMode: Any
    __timestamp: Any
    __timeCB: Any
    __mode: Any
    __movementKeyBindings: Any
    _deathAlreadySet: Any
    class HintModes(Enum):
        init = 0
        speed_idle = 1
        speed_loading = 2
        finished = 3
    def __init__(self):
        ...
    def updateSpeedLevel(self, newSpeedLevel):
        ...
    def hideReturnHintWrapper(self):
        ...
    def toggleFollowHint(self, toggle):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _handleMovement(self):
        ...
    def _handleVerticalMovement(self):
        ...
    def _addGameListeners(self):
        ...
    def _removeGameListeners(self):
        ...
    def _updateVehicleInfo(self):
        ...
    def __startSpeedHintTimeout(self):
        ...
    def __showSpeedHeightHintWrapper(self, toShow):
        ...
    def __onSpectatorModeChanged(self, mode):
        ...
    @staticmethod
    def __showFreeCamHints():
        ...
    def __playFollowHintSound(self, toggle):
        ...
    def __playSound(self, eventName):
        ...
    def __onRespawnVisibility(self, isVisible):
        ...
    def __onReinforcementTimerUpdated(self, time):
        ...
    def __tick(self):
        ...
    def __removeMovementListener(self):
        ...
    @staticmethod
    def __getMovementKeyBindings():
        ...
    def __updateKeyBindingSettings(self):
        ...
    def __setHintStrings(self):
        ...
    def __onMappingChanged(self, *args):
        ...
