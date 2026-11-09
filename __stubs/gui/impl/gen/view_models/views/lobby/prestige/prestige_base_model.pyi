# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_base_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel as PrestigeEmblemModel

class PrestigeBaseModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def emblem(self):
        ...
    @staticmethod
    def getEmblemType():
        ...
    def getCurrentProgress(self):
        ...
    def setCurrentProgress(self, value):
        ...
    def getMaxProgress(self):
        ...
    def setMaxProgress(self, value):
        ...
    def _initialize(self):
        ...
