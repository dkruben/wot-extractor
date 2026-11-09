# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/session_stats_views.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from account_helpers.settings_core.settings_constants import SESSION_STATS as SESSION_STATS
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.lobby.session_stats.shared import packLastBattleData as packLastBattleData, packBattleEfficiencyData as packBattleEfficiencyData, packTotalData as packTotalData, toIntegral as toIntegral, toNiceNumber as toNiceNumber, getDeltaAsData as getDeltaAsData, getNationIcon as getNationIcon
from gui.Scaleform.daapi.view.meta.SessionBattleStatsViewMeta import SessionBattleStatsViewMeta as SessionBattleStatsViewMeta
from gui.Scaleform.daapi.view.meta.SessionVehicleStatsViewMeta import SessionVehicleStatsViewMeta as SessionVehicleStatsViewMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_VEH_LIST_LEN = 12

class SessionBattleStatsView(SessionBattleStatsViewMeta):
    itemsCache: Any
    def updateData(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __updateViewHandler(self, *_):
        ...
    def __makeVO(self):
        ...

class SessionVehicleStatsView(SessionVehicleStatsViewMeta):
    itemsCache: Any
    def updateData(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    @property
    def __makeVO(self):
        ...
    def _sortedVehiclesData(self, vehiclesSortData, vehiclesData):
        ...
    def __updateViewHandler(self, *_):
        ...
