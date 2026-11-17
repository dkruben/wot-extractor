# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/sound_ctrls/epic_battle_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BATTLE_EVENT_TYPE
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES, VEHICLE_HIT_FLAGS as VHF
from frontline_common.frontline_constants import FLBattleReservesModifier as FLBattleReservesModifier
from gui.Scaleform.genConsts.EPIC_CONSTS import EPIC_CONSTS as EPIC_CONSTS
from gui.battle_control.avatar_getter import getSoundNotifications as getSoundNotifications
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, PROGRESS_CIRCLE_TYPE as PROGRESS_CIRCLE_TYPE
from gui.battle_control.controllers.sound_ctrls.common import BaseEfficiencySoundPlayer as BaseEfficiencySoundPlayer, SoundPlayersController as SoundPlayersController, VehicleStateSoundPlayer as VehicleStateSoundPlayer, ShotsResultSoundController as ShotsResultSoundController
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND
from helpers import dependency as dependency
from items import vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class EpicBattleSoundController(SoundPlayersController):
    _soundPlayers: Any
    def __init__(self):
        ...
    @classmethod
    def playSoundNotification(cls, eventName):
        ...

class EpicShotsResultSoundsController(ShotsResultSoundController):
    def getDestructibleHitResultSound(self, hitFlags):
        ...

class _EquipmentSoundPlayer(object):
    __sessionProvider: Any
    def init(self):
        ...
    def destroy(self):
        ...
    @staticmethod
    def __getEventName(itemName):
        ...
    def __onEquipmentUpdated(self, _, item):
        ...
    def __onCombatEquipmentUsed(self, shooterID, eqID):
        ...
    def __onPlayerRankUpdated(self, rank):
        ...

class _MineFieldSoundPlayer(BaseEfficiencySoundPlayer):
    def _onEfficiencyReceived(self, events):
        ...

class _StealthSoundPlayer(VehicleStateSoundPlayer):
    __stealthIsActive: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...
    def __stopEvent(self):
        ...

class _DeathZoneSoundPlayer(VehicleStateSoundPlayer):
    def _onVehicleStateUpdated(self, state, value):
        ...

class _UnderFireSoundPlayer(VehicleStateSoundPlayer):
    def _onVehicleStateUpdated(self, state, value):
        ...

class _RepairPointAndRegenerationKitSoundPlayer(VehicleStateSoundPlayer):
    __sessionProvider: Any
    __isRepairing: Any
    __isHealing: Any
    __curPointIdx: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _onSwitchViewPoint(self):
        ...
    def __stopHealingEvent(self):
        ...
    def __onVehicleEntered(self, type_, pointIdx, state):
        ...
    def __onVehicleLeft(self, type_, _):
        ...
    def __onCircleStatusChanged(self, type_, pointIdx, state):
        ...
    def __playResupplyReady(self):
        ...
    def __playResupplyStop(self):
        ...
