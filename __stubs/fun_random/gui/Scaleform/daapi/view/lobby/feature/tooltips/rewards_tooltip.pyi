# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/feature/tooltips/rewards_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from fun_random.gui.Scaleform.daapi.view.lobby.server_events.awards_formatters import FunCurtailingAwardsComposer as FunCurtailingAwardsComposer, getFunAwardsPacker as getFunAwardsPacker
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from fun_random.gui.impl.lobby.common.fun_view_helpers import sortFunProgressionBonuses as sortFunProgressionBonuses
from gui.server_events.bonuses import mergeBonuses as mergeBonuses
from gui.shared.tooltips.quests import AdditionalAwardTooltipData as AdditionalAwardTooltipData
_MAX_BONUS_COUNT = 8

class FunRandomRewardsTooltip(AdditionalAwardTooltipData, FunProgressionWatcher):
    # decorador original: @hasActiveProgression(...)
    def _packBlocks(self, *args, **kwargs):
        ...
