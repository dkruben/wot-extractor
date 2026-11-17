# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/daily_missions_section_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.block_status_model import BlockStatusModel as BlockStatusModel

class DailyMissionsSectionModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    @property
    def dailyMissionsBlockStatus(self):
        ...
    @staticmethod
    def getDailyMissionsBlockStatusType():
        ...
    @property
    def premiumDailyMissionsBlockStatus(self):
        ...
    @staticmethod
    def getPremiumDailyMissionsBlockStatusType():
        ...
    @property
    def rewardProgressBlockStatus(self):
        ...
    @staticmethod
    def getRewardProgressBlockStatusType():
        ...
    def getTargetQuestId(self):
        ...
    def setTargetQuestId(self, value):
        ...
    def _initialize(self):
        ...
