# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/seniority_awards/notifications/manual_claim_notification.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.seniority_awards.notifications.manual_claim_model import ManualClaimModel as ManualClaimModel
from gui.impl.lobby.gf_notifications import NotificationBase as NotificationBase
from helpers import dependency as dependency
from skeletons.gui.game_control import ISeniorityAwardsController as ISeniorityAwardsController
from uilogging.seniority_awards.constants import SeniorityAwardsLogSpaces as SeniorityAwardsLogSpaces
from uilogging.seniority_awards.loggers import RewardNotificationLogger as RewardNotificationLogger

class ManualClaimNotification(NotificationBase):
    __seniorityAwardsController: Any
    __uiRewardNotificationLogger: Any
    def __init__(self, resId, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _update(self):
        ...
    def __onClick(self):
        ...
    def __onClose(self):
        ...
