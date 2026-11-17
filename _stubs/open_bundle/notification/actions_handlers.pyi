# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/notification/actions_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from notification.actions_handlers import NavigationDisabledActionHandler as NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE
from open_bundle.gui.shared.event_dispatcher import showOpenBundleMainView as showOpenBundleMainView

class OpenBundleReminderHandler(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...
