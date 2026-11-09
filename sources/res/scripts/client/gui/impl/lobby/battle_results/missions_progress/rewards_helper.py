# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/rewards_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/battle_results/missions_progress/rewards_helper.py
from gui.Scaleform.daapi.view.lobby.server_events.token_converter_helper import getBonusDataFromOneOfBonuses, convertTokensInBonusData
from gui.server_events.bonuses import TokensBonus
from gui.shared.missions.packers.events import packQuestBonusModelAndTooltipData
_RANDOM_REWARD_PLACEHOLDER_SUFFIX = ':random'

def _isRandomRewardPlaceholder(bonus):
    if not isinstance(bonus, TokensBonus):
        return False
    return any(tokenID.endswith(_RANDOM_REWARD_PLACEHOLDER_SUFFIX) for tokenID in bonus.getTokens())


def packBonusesWithActualTokensConvertion(pCur, model, event, questTokensConvertion, questTokensCount, tooltipData, bonusPacker):
    bonusData = getBonusDataFromOneOfBonuses(event, pCur)
    bonusData = convertTokensInBonusData(event=event, bonusData=bonusData, questTokensConvertion=questTokensConvertion, questTokensCount=questTokensCount)
    questBonuses = [bonus for bonus in event.getBonuses(bonusData=bonusData) if not _isRandomRewardPlaceholder(bonus)]
    bonuses = model.getBonuses()
    bonuses.clear()
    packQuestBonusModelAndTooltipData(bonusPacker, bonuses, event, questBonuses=questBonuses, tooltipData=tooltipData)


def packBonusesWithTokensConvertionIfCompleted(pCur, model, event, questTokensConvertion, questTokensCount, tooltipData, bonusPacker, complete):
    if complete:
        packBonusesWithActualTokensConvertion(pCur, model, event, questTokensConvertion, questTokensCount, tooltipData, bonusPacker)
    else:
        bonuses = model.getBonuses()
        bonuses.clear()
        packQuestBonusModelAndTooltipData(bonusPacker, bonuses, event, questBonuses=[bonus for bonus in event.getBonuses() if not _isRandomRewardPlaceholder(bonus)], tooltipData=tooltipData)
