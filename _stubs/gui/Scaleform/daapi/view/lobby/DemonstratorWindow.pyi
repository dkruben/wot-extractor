# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/DemonstratorWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import lfilter as lfilter, viewitems as viewitems
from operator import itemgetter as itemgetter
from past.utils import old_div as old_div
import ArenaType as ArenaType
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import gameplay_ctx as gameplay_ctx, isDemonstratorExpert as isDemonstratorExpert
from account_helpers.settings_core.settings_constants import GAME as GAME
from gui.Scaleform.daapi.view.meta.DemonstratorWindowMeta import DemonstratorWindowMeta as DemonstratorWindowMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import ListDAAPIDataProvider as ListDAAPIDataProvider
from gui.Scaleform.genConsts.BATTLE_TYPES import BATTLE_TYPES as GAMEPLAY
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
BATTLE_TEMPLATES: list
BATTLE_TO_VEHICLE_LEVELS: list
_logger: Any

class SPAWNS(object):
    ANY = 'any'
    BLUE = 'blue'
    RED = 'red'

class BATTLE_TYPES(object):
    UNKNOWN = 0
    TOP1 = 1
    TOP2 = 2
    BOT2 = 3
    TOP3 = 4
    MID3 = 5
    BOT3 = 6

class DemonstratorWindow(DemonstratorWindowMeta, IGlobalListener):
    __lobbyContext: Any
    __settingsCore: Any
    __itemsCache: Any
    __slots__: tuple
    __mapListDP: Any
    __isDemonstratorExpert: Any
    __gameplaySelected: Any
    __mapSelected: Any
    __spawnSelected: Any
    __levelSelected: Any
    __vehicleSelected: Any
    __availableGameplayTypes: Any
    __availableBattleTypes: Any
    __availableMapsLength: Any
    def __init__(self, ctx=None):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        ...
    def onGameplaySelected(self, index):
        ...
    def onLvlSelected(self, index):
        ...
    def onSpawnSelected(self, index):
        ...
    def onMapSelected(self, index):
        ...
    def onBattleStart(self):
        ...
    def onWindowClose(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onVehicleChanged(self):
        ...
    def __setGameplayTabs(self):
        ...
    def __setSpawnsList(self):
        ...
    def __setMapsList(self):
        ...
    def __setPlatoonWarning(self):
        ...
    def __enableBattleButton(self):
        ...
    def __disableBattleButton(self):
        ...
    def __isInUnit(self):
        ...
    def __isCommander(self):
        ...
    def __setLevelsList(self):
        ...
    def __getAvailableLevelsBattleTypes(self):
        ...
    def __getAvailableBattleLevelRange(self):
        ...
    def __packMMData(self, arenaTypeID, levelType, team):
        ...

class ArenasCache(object):
    __cache: Any
    __playerTeam: Any
    def __init__(self):
        ...
    def __getPointsList(self, arenaType):
        ...
    @property
    def cache(self):
        ...

class MapListDataProvider(ListDAAPIDataProvider):
    __lobbyContext: Any
    _list: Any
    _cache: Any
    def __init__(self):
        ...
    @property
    def collection(self):
        ...
    def emptyItem(self):
        ...
    def clear(self):
        ...
    def dispose(self):
        ...
    def rebuildList(self, cache):
        ...
    def buildList(self, currentVehicleLevel=0, gameplayName=None):
        ...
