# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/vehicle_params_note.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R

class NoteThemeEnum(Enum):
    WARNING = 'warning'
    TEXTONLY = 'textOnly'
    CONTENT = 'content'
    AUTORELOADTIME = 'autoReloadTime'

class VehicleParamsNote(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getTitle(self):
        ...
    def setTitle(self, value):
        ...
    def getIcon(self):
        ...
    def setIcon(self, value):
        ...
    def getTheme(self):
        ...
    def setTheme(self, value):
        ...
    def _initialize(self):
        ...
