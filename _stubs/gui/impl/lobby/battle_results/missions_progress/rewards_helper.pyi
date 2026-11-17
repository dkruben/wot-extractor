# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/rewards_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.lobby.server_events.token_converter_helper import getBonusDataFromOneOfBonuses as getBonusDataFromOneOfBonuses, convertTokensInBonusData as convertTokensInBonusData
from gui.server_events.bonuses import TokensBonus as TokensBonus
from gui.shared.missions.packers.events import packQuestBonusModelAndTooltipData as packQuestBonusModelAndTooltipData
_RANDOM_REWARD_PLACEHOLDER_SUFFIX = ':random'

def _isRandomRewardPlaceholder(bonus):
    ...
def packBonusesWithActualTokensConvertion(pCur, model, event, questTokensConvertion, questTokensCount, tooltipData, bonusPacker):
    ...
def packBonusesWithTokensConvertionIfCompleted(pCur, model, event, questTokensConvertion, questTokensCount, tooltipData, bonusPacker, complete):
    ...
