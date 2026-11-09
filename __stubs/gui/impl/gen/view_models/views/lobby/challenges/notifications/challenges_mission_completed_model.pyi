# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/challenges/notifications/challenges_mission_completed_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel as NotificationBaseModel
from gui.impl.gen.view_models.views.lobby.challenges.bonus_model import BonusModel as BonusModel

class ChallengesMissionCompletedModel(NotificationBaseModel):
    __slots__: tuple
    onClick: Any
    def __init__(self, properties=3, commands=1):
        ...
    def getMissionID(self):
        ...
    def setMissionID(self, value):
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def _initialize(self):
        ...
