# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/shared/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from Event import Event as Event
from skeletons.gui.shared.utils import IItemsRequester as IItemsRequester, requesters as requesters

class IItemsCache(requesters.IRequester):
    onSyncStarted = None
    onSyncCompleted = None
    onPMSyncCompleted = None
    @property
    def waitForSync(self):
        ...
    @property
    def items(self):
        ...
    @property
    def compatVehiclesCache(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def update(self, updateReason, diff=None, notify=True, callback=None):
        ...
    def onDisconnected(self):
        ...
