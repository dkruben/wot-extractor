# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/base_stats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.StatsBaseMeta import StatsBaseMeta as StatsBaseMeta
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from uilogging.player_satisfaction_rating.loggers import InviteToPlatoonLogger as InviteToPlatoonLogger

class StatsBase(StatsBaseMeta):
    sessionProvider: Any
    _logger: Any
    __invitations: Any
    def __init__(self):
        ...
    @property
    def hasTabs(self):
        ...
    def acceptSquad(self, sessionID):
        ...
    def addToSquad(self, sessionID, source):
        ...
    def onToggleVisibility(self, isVisible):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onToggleVisibility(self, isVisible):
        ...
    def __handleShowCursor(self, _):
        ...
    def __handleHideCursor(self, _):
        ...
