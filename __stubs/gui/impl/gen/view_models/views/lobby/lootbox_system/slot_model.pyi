# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/slot_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.wrappers.user_list_model import UserListModel as UserListModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.bonus_model import BonusModel as BonusModel

class SlotModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    @property
    def bonuses(self):
        ...
    @staticmethod
    def getBonusesType():
        ...
    def getProbability(self):
        ...
    def setProbability(self, value):
        ...
    def _initialize(self):
        ...
