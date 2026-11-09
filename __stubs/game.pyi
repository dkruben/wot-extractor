# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/game.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import locale as locale
import sys as sys
import zlib as zlib
import typing as typing
from future.moves import pickle as pickle
import Account as Account
import AreaDestructibles as AreaDestructibles
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import Input as Input
import GUI as GUI
import MusicControllerWWISE as MusicControllerWWISE
import Settings as Settings
import SoundGroups as SoundGroups
import TriggersManager as TriggersManager
import VOIP as VOIP
import WebBrowser as WebBrowser
import constants as constants
import persistent_data_cache as pdc
import services_config as services_config
from MemoryCriticalController import g_critMemHandler as g_critMemHandler
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR, LOG_NOTE as LOG_NOTE
from gui import onRepeatKeyEvent as onRepeatKeyEvent, g_keyEventHandlers as g_keyEventHandlers, g_mouseEventHandlers as g_mouseEventHandlers, InputHandler as InputHandler
from gui.game_loading import loading as gameLoading
from gui.impl.dialogs import dialogs as dialogs
from gui.shared import personality as gui_personality
from helpers import RSSDownloader as RSSDownloader, OfflineMode as OfflineMode, LightingGenerationMode as LightingGenerationMode
from helpers import dependency as dependency, log as log
from messenger import MessengerEntry as MessengerEntry
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gameplay import IGameplayLogic as IGameplayLogic
from system_events import g_systemEvents as g_systemEvents
from wg_async import wg_async as wg_async, wg_await as wg_await
from BigWorld import KeyEvent as KeyEvent, MouseEvent as MouseEvent, AxisEvent as AxisEvent
g_replayCtrl = None

class ServiceLocator(object):
    connectionMgr: Any
    gameplay: Any

def autoFlushPythonLog():
    ...
def init(scriptConfig, engineConfig, userPreferences):
    ...
def start():
    ...
def abort():
    ...
def fini():
    ...
def onChangeEnvironments(inside):
    ...
def onBeforeSend():
    ...
def onRecreateDevice():
    ...
def onStreamComplete(streamID, desc, data):
    ...
def onLoginToCellFailed():
    ...
def onConnected():
    ...
def onGeometryMapped(spaceID, path):
    ...
def onDisconnected():
    ...
def onFini():
    ...
def onCameraChange(oldCamera):
    ...
def handleAxisEvent(event):
    ...
def handleKeyEvent(event):
    ...
def handleMouseEvent(event):
    ...
def handleInputLangChangeEvent():
    ...
def getAuthRealm():
    ...
# decorador original: @wg_async
def requestQuit():
    ...
def addChatMsg(*msg):
    ...
def expandMacros(line):
    ...
def wg_onChunkLoad(spaceID, chunkID, numDestructibles, isOutside):
    ...
def wg_onChunkLoose(spaceID, chunkID, isOutside):
    ...
def wg_playModuleDestructionAnimation(chunkID, destrIndex, moduleIndex, isShotDamage, isHavokSpawnedDestructibles):
    ...
def convertKeyEvent(event):
    ...
def convertMouseEvent(event):
    ...
def onMemoryCritical():
    ...
def checkBotNet():
    ...
