# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/deathzones_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
_TimersData: Any

class DeathZonesController(IArenaLoadController):
    __timersData: Any
    __timeToStrikeInCurrentNotification: Any
    __playerEnterZone: Any
    def __init__(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def updateDeathZoneWarningNotification(self, zoneId, show, timeToStrike, waveDuration):
        ...
