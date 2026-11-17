# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/challenges_missions_progress_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.challenge_quest_progress_model import ChallengeQuestProgressModel as ChallengeQuestProgressModel

class ChallengesMissionsProgressModel(ViewModel):
    __slots__: tuple
    PATH: str
    onNavigate: Any
    def __init__(self, properties=1, commands=1):
        ...
    @property
    def challengeQuest(self):
        ...
    @staticmethod
    def getChallengeQuestType():
        ...
    def _initialize(self):
        ...
