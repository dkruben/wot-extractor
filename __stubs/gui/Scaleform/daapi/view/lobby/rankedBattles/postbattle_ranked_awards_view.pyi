# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/postbattle_ranked_awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_OVERLAY_SOUND_SPACE as RANKED_OVERLAY_SOUND_SPACE
from gui.ranked_battles.ranked_builders.postbattle_awards_vos import getVOsSequence as getVOsSequence
from gui.Scaleform.daapi.view.meta.RankedBattlesAwardsViewMeta import RankedBattlesAwardsViewMeta as RankedBattlesAwardsViewMeta
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class PostbattleRankedAwardsView(RankedBattlesAwardsViewMeta):
    _COMMON_SOUND_SPACE = RANKED_OVERLAY_SOUND_SPACE
    __rankedController: Any
    __slots__: tuple
    __awardsSequence: Any
    __rankedInfo: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def onSoundTrigger(self, triggerName):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __close(self):
        ...
