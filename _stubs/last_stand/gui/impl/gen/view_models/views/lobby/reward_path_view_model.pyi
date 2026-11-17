# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/reward_path_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.reward_path_artefact_view_model import RewardPathArtefactViewModel as RewardPathArtefactViewModel

class RewardPathViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onViewLoaded: Any
    onAbout: Any
    onShowIntro: Any
    goToMission: Any
    def __init__(self, properties=4, commands=5):
        ...
    def getArtefacts(self):
        ...
    def setArtefacts(self, value):
        ...
    @staticmethod
    def getArtefactsType():
        ...
    def getPoints(self):
        ...
    def setPoints(self, value):
        ...
    def getCurrentArtefactID(self):
        ...
    def setCurrentArtefactID(self, value):
        ...
    def getOpenFromQuestCard(self):
        ...
    def setOpenFromQuestCard(self, value):
        ...
    def _initialize(self):
        ...
