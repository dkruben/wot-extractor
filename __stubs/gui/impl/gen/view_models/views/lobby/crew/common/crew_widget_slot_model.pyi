# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/crew_widget_slot_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_tankman_model import CrewWidgetTankmanModel as CrewWidgetTankmanModel

class CrewWidgetSlotModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def tankman(self):
        ...
    @staticmethod
    def getTankmanType():
        ...
    def getSlotIdx(self):
        ...
    def setSlotIdx(self, value):
        ...
    def getRoles(self):
        ...
    def setRoles(self, value):
        ...
    @staticmethod
    def getRolesType():
        ...
    def _initialize(self):
        ...
