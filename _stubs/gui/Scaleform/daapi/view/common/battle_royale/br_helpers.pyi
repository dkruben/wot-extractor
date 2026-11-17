# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/battle_royale/br_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import BigWorld as BigWorld
import CommandMapping as CommandMapping
from constants import BATTLE_ROYALE_SCENE as BATTLE_ROYALE_SCENE
from gui.Scaleform.daapi.view.common.keybord_helpers import getHotKeyList as getHotKeyList, getHotKeysInfo as getHotKeysInfo
from gui.server_events.awards_formatters import BR_PROGRESSION_TOKEN as BR_PROGRESSION_TOKEN
from helpers import dependency as dependency
from items import vehicles as vehicles, parseIntCompactDescr as parseIntCompactDescr, ITEM_TYPES as ITEM_TYPES
from skeletons.gui.game_control import IHangarSpaceSwitchController as IHangarSpaceSwitchController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

def getEquipmentById(equipmentId):
    ...
def getSmokeDataByPredicate(smokeInfo, predicate):
    ...
def parseSmokeData(smokesInfo):
    ...
def getCircularVisionAngle(vehicle=None):
    ...
def getHotKeyString(command):
    ...
def getHotKeyInfoListByIndex(index):
    ...
def isIncorrectVehicle(vehicle):
    ...
def isAdditionalModule(level, unlocks, moduleGetter):
    ...
def canVehicleSpawnBot(vehicle):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def currentHangarIsBattleRoyale(hangarSwitchController=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getAvailableNationsNames(lobbyContext=None):
    ...
def getAvailableVehicleTypes():
    ...
def sortQuestsByProgressionPointBonus(quests):
    ...
def _getProgressionPointBonus(quest):
    ...
