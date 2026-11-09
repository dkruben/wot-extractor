# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/full_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from battle_royale.gui.battle_control.controllers.vehicles_count_ctrl import IVehicleCountListener as IVehicleCountListener
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.meta.BattleRoyaleFullStatsMeta import BattleRoyaleFullStatsMeta as BattleRoyaleFullStatsMeta
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES_REVERSED as VEHICLE_TYPES_ORDER_INDICES_REVERSED
from gui.shared.utils.functions import getArenaShortName as getArenaShortName
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class FullStatsComponent(BattleRoyaleFullStatsMeta, IVehicleCountListener):
    sessionProvider: Any
    __battleRoyaleController: Any
    __vehicleTeams: Any
    __isSquadMode: Any
    __teamsCount: Any
    def __init__(self):
        ...
    @property
    def hasTabs(self):
        ...
    def onToggleVisibility(self, _):
        ...
    def setVehicles(self, _, vehicles, __):
        ...
    def setFrags(self, frags, isPlayerVehicle):
        ...
    def _populate(self):
        ...
    def _getBattleTypeIconPath(self, sizeFolder='c_136x136'):
        ...
    def __initPanel(self):
        ...
    def __getScoreBlock(self, icon, count, descr, squads=''):
        ...
    def __getMinimapItems(self):
        ...
    def __getMinimapItem(self, icon, description, blendMode='normal'):
        ...
    def __updateScore(self, frags=None):
        ...
    def __initTeamsCount(self):
        ...
