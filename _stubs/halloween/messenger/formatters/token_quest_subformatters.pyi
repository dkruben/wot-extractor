# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/messenger/formatters/token_quest_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui.shared.gui_items import getItemTypeID as getItemTypeID
from gui.shared.gui_items.customization.c11n_items import Style as Style
from helpers import time_utils as time_utils, dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData, getRewardsForQuests as getRewardsForQuests
from messenger.formatters.token_quest_subformatters import AsyncTokenQuestsSubFormatter as AsyncTokenQuestsSubFormatter
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from skeletons.gui.customization import ICustomizationService as ICustomizationService

class HalloweenStarterBundleFormatter(AsyncTokenQuestsSubFormatter):
    __QUEST_PREFIX = 'hw_rent_vehicles'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class HalloweenBattlePassPointsFormatter(AsyncTokenQuestsSubFormatter):
    __MESSAGE_TEMPLATE = 'hwBattlePassPointsMessage'
    __BATTLE_PASS_TOKEN_QUEST_PATTERN = 'battlepass_points'
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __buildMessage(self, questID, message):
        ...

class HalloweenKingRewardFormatter(AsyncTokenQuestsSubFormatter):
    hwArtifactsCtrl: Any
    c11n: Any
    __MESSAGE_TEMPLATE = 'tokenQuests'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __formatSimpleTokenQuests(self, message, questIDs, popUps):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
