# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/progress/research.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from collections import namedtuple as namedtuple
from constants import NEW_PERK_SYSTEM as NPS
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP as g_techTreeDP
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, Tankman as Tankman
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from items import tankmen as tankmen
from items.components.crew_skins_constants import NO_CREW_SKIN_ID as NO_CREW_SKIN_ID
MIN_BATTLES_TO_SHOW_PROGRESS = 5
TankmanProgress: Any
VehicleProgress: Any
ModuleProgress: Any

class VehicleProgressHelper(object):
    __slots__: tuple
    _itemsCache: Any
    _lobbyContext: Any
    __unlocks: Any
    __vehTypeCompDescr: Any
    __vehicle: Any
    __vehicleXp: Any
    __avgVehicleXp: Any
    def __init__(self, vehTypeCompDescr):
        ...
    def clear(self):
        ...
    def _getAvgVehicleXp(self, vehTypeCompDescr):
        ...
    def getReady2UnlockItems(self, vehicleBattleXp):
        ...
    def getNewSkilledTankmen(self, tankmenXps):
        ...
    @staticmethod
    def __getBonusSkillsAmount(tmanToCheck, skillsCountBefore, skillsCountAfter):
        ...
    def __getAvgBattles2Unlock(self, unlockProps):
        ...
    def __getAvgBattles2NewSkill(self, avgTmanXp, tman):
        ...
