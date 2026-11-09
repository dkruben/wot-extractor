# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/notification/actions_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from notification.actions_handlers import NavigationDisabledActionHandler as NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE
from resource_well.gui.shared.event_dispatcher import showMainWindow as showMainWindow

class OpenResourceWellProgressionStartWindow(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class OpenResourceWellProgressionWindow(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...
