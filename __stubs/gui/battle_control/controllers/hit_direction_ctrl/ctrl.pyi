# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/hit_direction_ctrl/ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import typing as typing
from future.utils import viewvalues as viewvalues
from account_helpers.settings_core import settings_constants as settings_constants
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import HIT_INDICATOR_MAX_ON_SCREEN as HIT_INDICATOR_MAX_ON_SCREEN, BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.hit_direction_ctrl.base import HitType as HitType
from gui.battle_control.controllers.hit_direction_ctrl.components import BaseHitComponent as BaseHitComponent, HitDamageComponent as HitDamageComponent
from gui.battle_control.controllers.hit_direction_ctrl.pulls import HitDamagePull as HitDamagePull, ArtyHitPredictionPull as ArtyHitPredictionPull
from gui.battle_control.controllers.hit_direction_ctrl.hit_data import HitData as HitData, SimpleHitData as SimpleHitData
from gui.battle_control.view_components import IViewComponentsController as IViewComponentsController
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

class HitDirectionController(IViewComponentsController):
    __slots__: tuple
    settingsCore: Any
    sessionProvider: Any
    lobbyContext: Any
    __uiHitComponents: Any
    __isVisible: Any
    __arenaDP: Any
    __controllingVehicleID: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def getHit(self, idx, hitType=...):
        ...
    def isVisible(self):
        ...
    def setVisible(self, flag):
        ...
    def setViewComponents(self, *components):
        ...
    def clearViewComponents(self):
        ...
    def addHit(self, hitDirYaw, attackerID, damage, isBlocked, critFlags, isHighExplosive, damagedID, attackReasonID):
        ...
    def addArtyHitPrediction(self, yaw):
        ...
    def removeArtyHitPrediction(self, yaw):
        ...
    def artyHitIsPostponed(self, yaw):
        ...
    def _hideAllHits(self):
        ...
    def __isFriendlyFireMode(self):
        ...
    def __clearHideCallbacks(self):
        ...
    def __handleGUIVisibility(self, event):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onPostmortemKillerVision(self, killerVehicleID):
        ...
    def __onVehicleControlling(self, vehicle):
        ...

class HitDirectionControllerPlayer(HitDirectionController):
    def stopControl(self):
        ...
