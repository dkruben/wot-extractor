# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/menu_item_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.notification_model import NotificationModel as NotificationModel

class MenuItemModel(ViewModel):
    __slots__: tuple
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def notification(self):
        ...
    @staticmethod
    def getNotificationType():
        ...
    def getName(self):
        ...
    def setName(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def _initialize(self):
        ...
