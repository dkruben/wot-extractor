# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/panel/ammunition/section_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.slot_model import SlotModel as SlotModel

class SectionState(Enum):
    DEFAULT = 'default'
    WARNING = 'warning'

class SectionModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getId(self):
        ...
    def setId(self, value):
        ...
    def getSlots(self):
        ...
    def setSlots(self, value):
        ...
    @staticmethod
    def getSlotsType():
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
