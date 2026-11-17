# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/dialogs/short_modification_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class ModificationType(Enum):
    MODIFICATION = 'modification'
    PAIRMODIFICATION = 'pairModification'
    MODIFICATIONWITHFEATURE = 'modificationWithFeature'

class ShortModificationModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getModificationName(self):
        ...
    def setModificationName(self, value):
        ...
    def getLevel(self):
        ...
    def setLevel(self, value):
        ...
    def getModificationType(self):
        ...
    def setModificationType(self, value):
        ...
    def _initialize(self):
        ...
