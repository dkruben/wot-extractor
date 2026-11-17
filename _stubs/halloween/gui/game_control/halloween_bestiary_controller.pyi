# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/game_control/halloween_bestiary_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import typing as typing
from Event import Event as Event
from halloween.gui.impl.lobby.hw_helpers.bestiary_helper import getEnemiesSeenList as getEnemiesSeenList, isEnemyUnlocked as isEnemyUnlocked
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from halloween_common.configs.halloween_bestiary import bestiarySchema as bestiarySchema
from halloween_common.halloween_constants import HALLOWEEN_BESTIARY_PARAMS_KEY as HALLOWEEN_BESTIARY_PARAMS_KEY
from items.vehicles import makeVehicleTypeCompDescrByName as makeVehicleTypeCompDescrByName
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from visual_script_client.arena_blocks import dependency as dependency
from typing import Optional as Optional, Tuple as Tuple
from halloween_common.configs.halloween_bestiary import BestiaryModel as BestiaryModel, EnemyModel as EnemyModel
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from gui.shared.events import GUICommonEvent as GUICommonEvent
EnemyData: Any

class HalloweenBestiaryController(IHalloweenBestiaryController):
    __lobbyContext: Any
    __hwCtrl: Any
    __enemies: Any
    __isBestiaryPostponed: Any
    onSettingsUpdate: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def getEnemyByIntCD(self, intCD):
        ...
    def getEnemyByToken(self, token):
        ...
    def getFirstNewEnemy(self):
        ...
    def hasEnemy(self, token):
        ...
    @property
    def hasUnlockedEnemies(self):
        ...
    @property
    def isBestiaryPostponed(self):
        ...
    @isBestiaryPostponed.setter
    def isBestiaryPostponed(self, value):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, event):
        ...
    @property
    def enemies(self):
        ...
    def _getConfig(self):
        ...
    def __clear(self):
        ...
    def __initEnemies(self):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
