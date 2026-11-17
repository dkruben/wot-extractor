# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/challenges/notifications/challenges_mission_completed_notification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.challenges.challenges_award_manager import AwardsManager as AwardsManager
from gui.challenges.challenges_bonuses_packers import getChallengesBonusPacker as getChallengesBonusPacker
from gui.challenges.challenges_decorators import createTooltipContentDecorator as createTooltipContentDecorator
from gui.impl.gen.view_models.views.lobby.challenges.notifications.challenges_mission_completed_model import ChallengesMissionCompletedModel as ChallengesMissionCompletedModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.gf_notifications import NotificationBase as NotificationBase
from gui.server_events.events_dispatcher import showChallenges as showChallenges

class ChallengesMissionCompletedNotification(NotificationBase):
    __tooltipItems: Any
    def __init__(self, resId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _getEvents(self):
        ...
    def _update(self):
        ...
    def __onClick(self):
        ...
    def __setRewards(self, rewardsData, model):
        ...
