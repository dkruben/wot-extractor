# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/hangar_switch_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import BigWorld as BigWorld
import Event as Event
import ResMgr as ResMgr
from constants import DEFAULT_HANGAR_SCENE as DEFAULT_HANGAR_SCENE
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from soft_exception import SoftException as SoftException
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers import dependency as dependency
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from skeletons.gui.game_control import IHangarSpaceSwitchController as IHangarSpaceSwitchController
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.utils.hangar_space_reloader import ErrorFlags as ErrorFlags
from shared_utils import nextTick as nextTick
from skeletons.gui.shared.utils import IHangarSpaceReloader as IHangarSpaceReloader, IHangarSpace as IHangarSpace
from gui.ClientHangarSpace import SERVER_CMD_CHANGE_HANGAR as SERVER_CMD_CHANGE_HANGAR, SERVER_CMD_CHANGE_HANGAR_PREM as SERVER_CMD_CHANGE_HANGAR_PREM, getDefaultHangarPath as getDefaultHangarPath, SERVER_CMD_CHANGE_HANGAR_ALT as SERVER_CMD_CHANGE_HANGAR_ALT, getHangarFullVisibilityMask as getHangarFullVisibilityMask, g_clientHangarSpaceOverride as g_clientHangarSpaceOverride
_logger: Any

class DefaultHangarSpaceConfig(object):
    _visibilityMask: Any
    _spaceIdOverride: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def getVisibilityMask(self, isPremium):
        ...
    def discardVisibilityMaskOverride(self, isPremium):
        ...
    def setVisibilityMask(self, isPremium, visibilityMask):
        ...
    def getHangarSpaceId(self, isPremium):
        ...
    def setSpaceIdOverride(self, isPremium, newId):
        ...
    def discardSpaceIdOverride(self, isPremium):
        ...

class SceneSpaceConfig(object):
    _waitingMessage: Any
    _waitingBackground: Any
    _spaceId: Any
    _spaceIdOverride: Any
    _visibilityMask: Any
    def __init__(self, spaceId=None, waitingMessage=None, waitingBackground=None, spaceIdOverride=None, visibilityMask=None):
        ...
    @property
    def waitingMessage(self):
        ...
    @property
    def waitingBackground(self):
        ...
    def getVisibilityMask(self):
        ...
    def discardVisibilityMaskOverride(self):
        ...
    def setVisibilityMask(self, visibilityMask):
        ...
    def getHangarSpaceId(self):
        ...
    def setSpaceIdOverride(self, newId):
        ...
    def discardSpaceIdOverride(self):
        ...

class HangarSpaceSwitchController(IHangarSpaceSwitchController, IGlobalListener):
    hangarSpaceReloader: Any
    hangarSpace: Any
    onCheckSceneChange: Any
    onSpaceUpdated: Any
    hangarSpaceUpdated: Any
    currentSceneName: Any
    _defaultHangars: Any
    _sceneSpaceParams: Any
    _defaultHangarSpaceConfig: Any
    __isHangarOverridingLocked: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    def hangarSpaceUpdate(self, sceneName):
        ...
    def lockHangarOverride(self, sceneName):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def _clear(self):
        ...
    def _delayedProcessChange(self):
        ...
    def processPossibleSceneChange(self, force=False):
        ...
    def _onSpaceCreatedCallback(self):
        ...
    def _readHangarSceneSpaceSettings(self):
        ...
    def _onEventNotificationsChanged(self, diff):
        ...
