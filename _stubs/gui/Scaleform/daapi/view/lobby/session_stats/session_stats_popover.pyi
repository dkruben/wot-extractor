# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/session_stats_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.SessionStatsPopoverMeta import SessionStatsPopoverMeta as SessionStatsPopoverMeta
from gui.Scaleform.genConsts.SESSION_STATS_CONSTANTS import SESSION_STATS_CONSTANTS as SESSION_STATS_CONSTANTS
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_settings import SessionStatsSettings as SessionStatsSettings
from gui.Scaleform.daapi.view.lobby.session_stats.session_stats_overview import SessionStatsOverview as SessionStatsOverview

class SessionStatsPopover(SessionStatsPopoverMeta):
    __sessionBattleStats: Any
    __sessionSettings: Any
    def __init__(self, ctx=None):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def onShowSettings(self):
        ...
    def onShowStats(self):
        ...
