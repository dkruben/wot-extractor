# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/refill_shells_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.views.lobby.common.dialog_with_exchange import DialogWithExchange as DialogWithExchange
from gui.impl.gen.view_models.views.lobby.common.multiple_items_content_model import MultipleItemsContentModel as MultipleItemsContentModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import DealPanelModel as DealPanelModel

class RefillShellsModel(DialogWithExchange):
    __slots__: tuple
    def __init__(self, properties=18, commands=3):
        ...
    @property
    def dealPanel(self):
        ...
    @staticmethod
    def getDealPanelType():
        ...
    @property
    def mainContent(self):
        ...
    @staticmethod
    def getMainContentType():
        ...
    def getWithRollback(self):
        ...
    def setWithRollback(self, value):
        ...
    def _initialize(self):
        ...
