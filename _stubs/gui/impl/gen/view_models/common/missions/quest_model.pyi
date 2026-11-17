# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/common/missions/quest_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel as ConditionGroupModel
from gui.impl.gen.view_models.common.missions.event_model import EventModel as EventModel

class QuestModel(EventModel):
    __slots__: tuple
    def __init__(self, properties=11, commands=0):
        ...
    @property
    def preBattleCondition(self):
        ...
    @staticmethod
    def getPreBattleConditionType():
        ...
    @property
    def bonusCondition(self):
        ...
    @staticmethod
    def getBonusConditionType():
        ...
    @property
    def postBattleCondition(self):
        ...
    @staticmethod
    def getPostBattleConditionType():
        ...
    def getBonuses(self):
        ...
    def setBonuses(self, value):
        ...
    @staticmethod
    def getBonusesType():
        ...
    def _initialize(self):
        ...
