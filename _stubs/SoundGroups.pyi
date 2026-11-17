# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SoundGroups.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import total_ordering as total_ordering
from future.utils import lrange as lrange, viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
import WWISE as WWISE
import Event as Event
import Settings as Settings
import ResMgr as ResMgr
import PlayerEvents as PlayerEvents
import MusicControllerWWISE as MusicControllerWWISE
import Windowing as Windowing
from ReplayEvents import g_replayEvents as g_replayEvents
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_WARNING as LOG_WARNING, LOG_DEBUG as LOG_DEBUG
from helpers import i18n as i18n, dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader, GuiGlobalSpaceID as GuiGlobalSpaceID
from soft_exception import SoftException as SoftException
from vehicle_systems.tankStructure import TankPartNames as TankPartNames
ENABLE_LS = True
ENABLE_ENGINE_N_TRACKS = True
DEBUG_TRACE_SOUND = False
DEBUG_TRACE_STACK = False
DEBUG_TRACE_EFFECTLIST = False
g_instance = None
DSP_LOWPASS_LOW = 7000
DSP_LOWPASS_HI = 20000
DSP_SEEKSPEED = 200000
SOUND_ENABLE_STATUS_DEFAULT = 0
SOUND_ENABLE_STATUS_VALUES: Any
MASTER_VOLUME_DEFAULT = 0.5
CUSTOM_MP3_EVENTS: tuple

class CREW_GENDER_SWITCHES(object):
    GROUP = 'SWITCH_ext_vo_gender'
    MALE = 'SWITCH_ext_vo_gender_male'
    FEMALE = 'SWITCH_ext_vo_gender_female'
    DEFAULT = MALE
    GENDER_ALL: tuple

class SoundModes(object):
    __MODES_FOLDER = 'gui/soundModes/'
    __MODES_FILENAME = 'main_sound_modes.xml'
    DEFAULT_MODE_NAME = 'default'
    DEFAULT_NATION = 'default'
    MEDIA_PATH = None
    modes: Any
    nationalPresets: Any
    currentMode: Any
    currentNationalPreset: Any
    nationToSoundModeMapping: Any
    __modes: Any
    __currentMode: Any
    __nationalPresets: Any
    __nationToSoundModeMapping: Any
    __currentNationalPreset: Any
    name: Any
    voiceLanguage: Any
    description: Any
    invisible: Any
    wwbanksToBeLoaded: Any
    __isValid: Any
    mapping: Any
    # decorador original: @total_ordering
    class SoundModeDesc(object):
        __hash__: Any
        name: Any
        voiceLanguage: Any
        description: Any
        invisible: Any
        wwbanksToBeLoaded: Any
        __isValid: Any
        def __init__(self, dataSection):
            ...
        def __repr__(self):
            ...
        def __eq__(self, other):
            ...
        def __lt__(self, other):
            ...
        def getIsValid(self, soundModes):
            ...
        def __compare(self, other):
            ...
    class NationalPresetDesc(object):
        name: Any
        description: Any
        mapping: Any
        def __init__(self, dataSection):
            ...
        def __repr__(self):
            ...
    def __init__(self, initialModeName):
        ...
    def __readSoundModesConfig(self, rootSection, mainNationalPresets):
        ...
    def __readNationalPresets(self, rootSection):
        ...
    def setMode(self, modeName):
        ...
    def __setMode(self, modeName):
        ...
    def setCurrentNation(self, nation, genderSwitch=...):
        ...
    def setNationalMapping(self, nationToSoundModeMapping):
        ...
    def setNationalMappingByMode(self, soundMode):
        ...
    def setNationalMappingByPreset(self, presetName):
        ...

class SoundGroups(object):
    soundModes: Any
    onVolumeChanged: Any
    onMusicVolumeChanged: Any
    __enableStatus: Any
    __volumeByCategory: Any
    __masterVolume: Any
    __handleInside: Any
    __handleOutside: Any
    __activeStinger: Any
    __activeTrack: Any
    __activeStingerPriority: Any
    __muffled: Any
    __muffledByReplay: Any
    __spaceID: Any
    __categories: Any
    __soundModes: Any
    __viewPlayModeParam: Any
    __muffledVolume: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def startListeningGUISpaceChanges(self):
        ...
    def stopListeningGUISpaceChanges(self):
        ...
    def enableLobbySounds(self, enable):
        ...
    def enableArenaSounds(self, enable):
        ...
    def enableAmbientAndMusic(self, enable):
        ...
    def enableEverythingExceptGui(self, enable):
        ...
    def enableVoiceSounds(self, enable):
        ...
    def __onReplayMute(self, mute):
        ...
    def __onGUISpaceEntered(self, spaceID):
        ...
    def setMasterVolume(self, volume):
        ...
    def getMasterVolume(self):
        ...
    def getEnableStatus(self):
        ...
    def setEnableStatus(self, status):
        ...
    def setVolume(self, categoryName, volume, updatePrefs=True):
        ...
    def getVolume(self, categoryName):
        ...
    def savePreferences(self):
        ...
    def applyPreferences(self):
        ...
    def muffleWWISEVolume(self):
        ...
    def restoreWWISEVolume(self):
        ...
    def onAvatarReady(self):
        ...
    def __onCameraChanged(self, cameraName, currentVehicleId=None):
        ...
    def __onWindowAccessibilityChanged(self, isAccessible):
        ...
    def unloadAll(self):
        ...
    def preloadSoundGroups(self, arenaName):
        ...
    def getSound3D(self, node, event):
        ...
    def prepareMP3(self, event):
        ...
    def getSound2D(self, event):
        ...
    def playSound2D(self, event, checkSoundBankName=''):
        ...
    def playSafeSound2D(self, event):
        ...
    def playSoundPos(self, event, pos):
        ...
    def playCameraOriented(self, event, pos):
        ...
    def getCameraOriented(self, event, pos):
        ...
    def WWgetSoundObject(self, objectName, matrix, local=..., auxSend=False):
        ...
    def WWgetSound(self, eventName, objectName, matrix, local=...):
        ...
    def WWgetSoundCallback(self, eventName, objectName, matrix, callback):
        ...
    def WWgetSoundPos(self, eventName, objectName, position):
        ...
    def changePlayMode(self, mode):
        ...
    def playStinger(self, event, priority):
        ...
    def playTrack(self, event):
        ...
    def setSwitch(self, group, switch):
        ...
    def setState(self, stateName, stateValue):
        ...
    def setGlobalRTPC(self, rtpcName, rtpcValue):
        ...
