# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/ls_story_point_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from helpers import dependency as dependency
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from skeletons.gui.server_events import IEventsCache as IEventsCache
from last_stand.skeletons.ls_story_point_controller import ILSStoryPointController as ILSStoryPointController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand_common.last_stand_constants import StoryPointsSettings as StoryPointsSettings
from last_stand.gui.ls_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared.events import GUICommonEvent as GUICommonEvent

class LSStoryPointController(ILSStoryPointController, IGlobalListener):
    eventsCache: Any
    lsCtrl: Any
    FIRST_STORY_POINT_INDEX = 1
    onStoryPointStatusUpdated: Any
    _storyPointsIDs: Any
    _selectedStoryPointID: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onLobbyInited(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    @property
    def selectedStoryPointID(self):
        ...
    @selectedStoryPointID.setter
    def selectedStoryPointID(self, storyPointID):
        ...
    @property
    def storyPoints(self):
        ...
    def isStoryPointReceived(self, storyPointID):
        ...
    def getStoryPointIDByIndex(self, index):
        ...
    def getIndex(self, storyPointID):
        ...
    def getStoryPointsCount(self):
        ...
    def _initStoryPoints(self):
        ...
    def __handleTokensUpdate(self, diff):
        ...
