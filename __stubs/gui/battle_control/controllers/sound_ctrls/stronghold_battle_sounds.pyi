# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/sound_ctrls/stronghold_battle_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import typing as typing
import BigWorld as BigWorld
import SoundGroups as SoundGroups
import WWISE as WWISE
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.controllers.sound_ctrls.common import VehicleStateSoundPlayer as VehicleStateSoundPlayer, SoundPlayersBattleController as SoundPlayersBattleController, SoundPlayer as SoundPlayer
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import artefacts as artefacts, vehicles as vehicles
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicle_systems.tankStructure import TankSoundObjectsIndexes as TankSoundObjectsIndexes

class SoundEvents(object):
    EQUIPMENT_ACTIVATED: dict
    EQUIPMENT_PREPARING: dict
    EQUIPMENT_PREPARING_CANSELED: dict
    INSPIRE_ENTER = 'gui_clan_abl_insp_enter'
    INSPIRE_EXIT = 'gui_clan_abl_insp_exit'
    INSPIRE_START = 'gui_clan_abl_insp_start'
    INSPIRE_END = 'gui_clan_abl_insp_end'
    ARTILLERY_ENTER = 'gui_clan_abl_art_enter'
    ARTILLERY_EXIT = 'gui_clan_abl_art_exit'
    ARTILLERY_HIT_PC = 'imp_small_splash_HE_NPC_PC'
    ARTILLERY_HIT_NPC = 'imp_small_pierce_HE_NPC_NPC'

class StrongholdBattleSoundController(SoundPlayersBattleController):
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def _initializeSoundPlayers(self):
        ...

class _EquipmentSoundPlayer(SoundPlayer):
    __sessionProvider: Any
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onEquipmentUpdated(self, _, item):
        ...
    @staticmethod
    def __playSound(descrType, soundMap):
        ...

class _InspireSoundPlayer(VehicleStateSoundPlayer, CallbackDelayer):
    STOP_SOURCE_SOUND_DELAY = 3
    __isInspiring: Any
    __isInspired: Any
    __isSource: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def __stopEvent(self):
        ...

class _AOEZoneSoundPlayer(VehicleStateSoundPlayer, CallbackDelayer):
    MIN_DELAY = 0.75
    MAX_DELAY = 1.5
    __isDelayPeriod: Any
    __tillFinishAttackTime: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def __playDamageReceivedSound(self):
        ...
    def __stopDelayPeriod(self):
        ...
    @staticmethod
    def __findLongest(zones):
        ...
    @staticmethod
    def __play3DVehicleSound():
        ...
    @staticmethod
    def __play2DSound(event):
        ...
