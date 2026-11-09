# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/vehicle_playlists_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import os as os
import uuid as uuid
import typing as typing
from future.utils import iteritems as iteritems
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID
from helpers.local_cache import FileLocalCache as FileLocalCache
from params_schemas.veh_playlists_schema import vehPlaylistsConfigSchema as vehPlaylistsConfigSchema
from skeletons.gui.game_control import IVehiclePlaylistsController as IVehiclePlaylistsController
from typing import Optional as Optional, Dict as Dict, Iterator as Iterator, Tuple as Tuple
_logger: Any
PLAY_LIST_SCHEMA: tuple

class _CurrentlyBeingModifiedData(object):
    id: Any
    data: Any
    initial: Any
    isReallyChanged: Any
    def __init__(self):
        ...
    def clear(self):
        ...

class _VehiclePlaylistsCache(FileLocalCache):
    __VERSION = 1
    __SPACE = 'playlists_cache'
    __filePath: Any
    data: Any
    selectedID: Any
    def __init__(self, userDatabaseID):
        ...
    def write(self):
        ...
    def clear(self):
        ...
    def _getCache(self):
        ...
    def _setCache(self, data):
        ...

class VehiclePlaylist(object):
    def __init__(self, pStrData):
        ...
    def __repr__(self):
        ...

class VehiclePlaylistsController(IVehiclePlaylistsController):
    __eventManager: Any
    onEnabledStatusChanged: Any
    onModifiedPlaylistDiscarded: Any
    onDirtyClean: Any
    onPlaylistSaved: Any
    __isEnabled: Any
    __cache: Any
    __modifiedPlaylist: Any
    def __init__(self):
        ...
    def initPlayLists(self):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onDisconnected(self):
        ...
    def fini(self):
        ...
    @property
    def isEnabled(self):
        ...
    def generateId(self):
        ...
    def getSelectedID(self):
        ...
    def setSelectedID(self, val):
        ...
    def iterPlaylists(self):
        ...
    def simplePlayListParser(self, pStrData):
        ...
    def updateModifiedPlaylist(self, plStrID, playlistData):
        ...
    def setInitialModifiedPlaylist(self, plStrID, playlistData):
        ...
    def clearModifiedPlaylist(self):
        ...
    def saveModifiedPlaylist(self):
        ...
    def setModifiedPlaylistChanged(self, isChanged):
        ...
    @property
    def isModifiedPlaylistChanged(self):
        ...
    def createPlaylist(self, plStrID, playlistData):
        ...
    def deletePlaylist(self, plStrID):
        ...
    def getPlaylistDataByID(self, plStrID):
        ...
    def discardModifiedPlaylist(self):
        ...
    def __setEnabledFeature(self, enabled):
        ...
    def __dispose(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
