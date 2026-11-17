# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/marathon/marathon_event_container.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from cache import cached_property as cached_property
from gui.server_events.event_items import Group as Group, Quest as Quest
from gui.game_control.links import URLMacros as URLMacros
from gui.marathon.marathon_constants import MarathonState as MarathonState, MISSION_TAB_FORMAT as MISSION_TAB_FORMAT, AWARD_TOKENS_FORMAT as AWARD_TOKENS_FORMAT, R_TITLE_TOOLTIP as R_TITLE_TOOLTIP, TOKEN_COUNT_INDEX as TOKEN_COUNT_INDEX, ZERO_TIME as ZERO_TIME
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from items.vehicles import makeVehicleTypeCompDescrByName as makeVehicleTypeCompDescrByName

class MarathonEventContainer(object):
    prefix: Any
    tokenPrefix: Any
    styleTokenPostfix: Any
    urlName: Any
    marathonCompleteUrlAdd: Any
    vehicleName: Any
    suspendPrefix: Any
    completedTokenPostfix: Any
    hangarFlagName: Any
    questsInChain: Any
    minVehicleLevel: Any
    awardTokensPostfix: Any
    awardPostTokensPostfix: Any
    showFlagTooltipBottom: Any
    flagTooltip: Any
    disabledFlagTooltip: Any
    marathonTooltipHeader: Any
    bodyAddInfo: Any
    doesShowRewardScreen: Any
    doesShowRewardVideo: Any
    doesShowInPostBattle: Any
    questsPerStep: Any
    isEnabled: Any
    isAvailable: Any
    rewardObtained: Any
    postRewardObtained: Any
    state: Any
    suspendFlag: Any
    quest: Any
    group: Any
    awardTokens: Any
    postAwardTokens: Any
    tabTooltip: Any
    infoBody: Any
    label: Any
    backBtnLabel: Any
    tooltips: Any
    icons: Any
    urlMacros: Any
    rewardPostfix: Any
    styleID: Any
    styleTokenDiscount: Any
    def __init__(self):
        ...
    def _initialize(self):
        ...
    def _override(self):
        ...
    # decorador original: @cached_property
    def vehicleID(self):
        ...
    def getTimeFromGroupStart(self):
        ...
    def getGroupStartFinishTime(self):
        ...
    def getGroupTimeInterval(self):
        ...
    def getQuestTimeInterval(self):
        ...
    def getQuestStartFinishTime(self):
        ...
    def setQuest(self, quests, currentStep):
        ...
    def setGroup(self, groups):
        ...
    def setState(self, state):
        ...
    def setRewardObtained(self, tokens):
        ...
    def setPostRewardObtained(self, tokens):
        ...
