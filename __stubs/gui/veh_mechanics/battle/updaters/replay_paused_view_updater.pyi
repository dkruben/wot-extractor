# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/replay_paused_view_updater.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
from ReplayEvents import g_replayEvents as g_replayEvents
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater

class ReplayPausedViewUpdater(ViewUpdater):
    isPaused: Any
    def __init__(self, *args, **kwargs):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def __onReplayTimeWarpFinished(self):
        ...
    def __onReplayPaused(self, isPaused, forced=False):
        ...
