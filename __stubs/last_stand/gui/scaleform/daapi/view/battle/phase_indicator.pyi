# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/phase_indicator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional
from LSArenaPhasesComponent import LSArenaPhasesComponent as LSArenaPhasesComponent
from gui.impl import backport as backport
from last_stand.gui.scaleform.daapi.view.meta.PhaseIndicatorMeta import PhaseIndicatorMeta as PhaseIndicatorMeta
from helpers import dependency as dependency
from gui.impl.gen import R as R
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_R_INDICATOR = R.strings.last_stand_battle.arena
_PHASE = 'phase'
_WAVE = 'wave'

class LSPhaseIndicator(PhaseIndicatorMeta):
    sessionProvider: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _update(self, arenaPhases):
        ...
    def __updateProgressInfo(self, activePhase, phasesCount):
        ...
