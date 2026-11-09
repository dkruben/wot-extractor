# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/missions_state_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory as MissionCategory
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.missions_model import MissionsModel as MissionsModel

class MissionsStateModel(ViewModel):
    __slots__: tuple
    changeCategory: Any
    def __init__(self, properties=2, commands=1):
        ...
    def getAllMissions(self):
        ...
    def setAllMissions(self, value):
        ...
    @staticmethod
    def getAllMissionsType():
        ...
    def getMissionsCategory(self):
        ...
    def setMissionsCategory(self, value):
        ...
    def _initialize(self):
        ...
