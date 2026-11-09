# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/special_sound_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
import ResMgr as ResMgr
import SoundGroups as SoundGroups
import nations as nations
from account_helpers.settings_core import settings_constants as settings_constants
from account_helpers.settings_core.options import AltVoicesSetting as AltVoicesSetting
from helpers import dependency as dependency
from SoundGroups import CREW_GENDER_SWITCHES as CREW_GENDER_SWITCHES
from items import tankmen as tankmen
from items.components.tankmen_components import SPECIAL_VOICE_TAG as SPECIAL_VOICE_TAG
from items.components.crew_skins_constants import NO_CREW_SKIN_ID as NO_CREW_SKIN_ID, NO_CREW_SKIN_SOUND_SET as NO_CREW_SKIN_SOUND_SET
from items.special_crew import isHW25CrewCNCompleted as isHW25CrewCNCompleted, isHW25CrewCompleted as isHW25CrewCompleted, isMihoCrewCompleted as isMihoCrewCompleted, isYhaCrewCompleted as isYhaCrewCompleted, isWitchesCrewCompleted as isWitchesCrewCompleted, isMikaCrewCompleted as isMikaCrewCompleted, isDarjeelingCrewCompleted as isDarjeelingCrewCompleted, isErwinCrewCompleted as isErwinCrewCompleted, isNakajimaCrewCompleted as isNakajimaCrewCompleted
from items.vehicles import VehicleDescr as VehicleDescr
from constants import ITEM_DEFS_PATH as ITEM_DEFS_PATH, CURRENT_REALM as CURRENT_REALM
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.game_control import ISpecialSoundCtrl as ISpecialSoundCtrl
from gui.battle_control import avatar_getter as avatar_getter
from PlayerEvents import g_playerEvents as g_playerEvents
from vehicle_outfit.outfit import Outfit as Outfit
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any
_XML_PATH: Any
_FULL_CREW_CONDITION = 'isFullCrew'
_VoiceoverParams: Any
_genderStrToSwitch: dict
_isFullCrewCheckers: dict

class SpecialSoundCtrl(ISpecialSoundCtrl):
    __lobbyContext: Any
    __settingsCore: Any
    __sessionProvider: Any
    __voiceoverByVehicle: Any
    __voiceoverByTankman: Any
    __voiceoverSpecialModes: Any
    __arenaMusicByStyle: Any
    __specialVoiceTags: Any
    __currentMode: Any
    __arenaMusicSetup: Any
    def __init__(self):
        ...
    @property
    def arenaMusicSetup(self):
        ...
    @property
    def specialVoice(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def setPlayerVehicle(self, vehiclePublicInfo, isPlayerVehicle):
        ...
    def getVoiceoverByTankmanTagOrVehicle(self, tag):
        ...
    def getVoiceoverSpecialModesByTag(self, tag):
        ...
    def checkTagForSpecialVoice(self, tag):
        ...
    def __setVoiceoverByVehicleOrTankman(self, vehiclePublicInfo, isPlayerVehicle):
        ...
    def __setArenaMusicByStyle(self, vehiclePublicInfo, isPlayerVehicle):
        ...
    def __onAvatarBecomeNonPlayer(self):
        ...
    def __readSpecialVoices(self):
        ...
    def __setSpecialVoiceByVehicle(self, vehicleName, isPlayerVehicle):
        ...
    def __setSpecialVoiceByTankmen(self, vehicleType, crewGroups):
        ...
    def __setSpecialVoiceByCommanderSkinID(self, isFemale, commanderSkinID):
        ...
    def __setSpecialVoice(self, params):
        ...
    def __getSpecialModeForCrew(self, tag, vehicleType, crewGroups):
        ...
