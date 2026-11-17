# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/widget/personal_missions_list_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.personal_mission_model import PersonalMissionModel as PersonalMissionModel

class PersonalMissionsListModel(ViewModel):
    __slots__: tuple
    onClick: Any
    onMarkAsViewed: Any
    def __init__(self, properties=2, commands=2):
        ...
    def getMissions(self):
        ...
    def setMissions(self, value):
        ...
    @staticmethod
    def getMissionsType():
        ...
    def getReadyForAnimations(self):
        ...
    def setReadyForAnimations(self, value):
        ...
    def _initialize(self):
        ...
