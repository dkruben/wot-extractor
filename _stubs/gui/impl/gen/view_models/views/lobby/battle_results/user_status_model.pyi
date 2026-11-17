# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/user_status_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel as UserNameModel

class UserStatusModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def killer(self):
        ...
    @staticmethod
    def getKillerType():
        ...
    def getIsLeftBattle(self):
        ...
    def setIsLeftBattle(self, value):
        ...
    def getDeathReason(self):
        ...
    def setDeathReason(self, value):
        ...
    def _initialize(self):
        ...
