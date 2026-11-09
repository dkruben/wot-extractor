# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/bestiary_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from halloween.gui.impl.gen.view_models.views.lobby.enemy_model import EnemyModel as EnemyModel
from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel as SelectableViewModel

class BestiaryViewModel(SelectableViewModel):
    __slots__: tuple
    onClose: Any
    onChangeEnemy: Any
    onResize: Any
    def __init__(self, properties=2, commands=5):
        ...
    def getSelectedIntCD(self):
        ...
    def setSelectedIntCD(self, value):
        ...
    def getEnemies(self):
        ...
    def setEnemies(self, value):
        ...
    @staticmethod
    def getEnemiesType():
        ...
    def _initialize(self):
        ...
