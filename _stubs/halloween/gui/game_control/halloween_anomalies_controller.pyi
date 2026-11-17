# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/game_control/halloween_anomalies_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple, OrderedDict as OrderedDict
import random as random
import typing as typing
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from Event import Event as Event
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from halloween.skeletons.halloween_anomalies_controller import IHalloweenAnomaliesController as IHalloweenAnomaliesController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween_common.configs.halloween_anomalies import anomaliesConfigSchema as anomaliesConfigSchema
from halloween_common.halloween_constants import HALLOWEEN_ANOMALIES_PARAMS_KEY as HALLOWEEN_ANOMALIES_PARAMS_KEY, ANOMALIES_SYSTEM_UNLOCKED as ANOMALIES_SYSTEM_UNLOCKED, ALL_LOOT_ANOMALY_TYPES as ALL_LOOT_ANOMALY_TYPES, AnomalySettings as AnomalySettings
from shared_utils import nextTick as nextTick
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from visual_script_client.arena_blocks import dependency as dependency
from typing import Optional as Optional, List as List
from halloween_common.configs.halloween_anomalies import AnomaliesConfigModel as AnomaliesConfigModel
from gui.shared.events import GUICommonEvent as GUICommonEvent
AnomalyData: Any
RecipeData: Any

class HalloweenAnomaliesController(IHalloweenAnomaliesController):
    __lobbyContext: Any
    __itemsCache: Any
    __hwCtrl: Any
    __slots__: tuple
    onRefreshData: Any
    onChangeSystemAnomaliesUnlock: Any
    __anomalies: Any
    __lootAnomalies: Any
    __recipes: Any
    _lastSkinId: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onDisconnected(self):
        ...
    @property
    def anomalies(self):
        ...
    @property
    def lootAnomalies(self):
        ...
    @property
    def recipes(self):
        ...
    def getAnomalyByID(self, anomalyID):
        ...
    def _getConfig(self):
        ...
    def __clear(self):
        ...
    def __handleTokensUpdate(self, diff):
        ...
    def __refreshData(self):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def getNextSkinId(self, maxSkinId):
        ...
