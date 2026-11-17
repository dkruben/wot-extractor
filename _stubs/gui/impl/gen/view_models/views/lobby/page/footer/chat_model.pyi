# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/footer/chat_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Map as Map, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.page.footer.message_model import MessageModel as MessageModel

class ChatModel(ViewModel):
    __slots__: tuple
    onViewMessageAction: Any
    onDeleteMessageAction: Any
    onWindowAnchorPositionUpdated: Any
    onChatsAction: Any
    def __init__(self, properties=1, commands=4):
        ...
    def getMessages(self):
        ...
    def setMessages(self, value):
        ...
    @staticmethod
    def getMessagesType():
        ...
    def _initialize(self):
        ...
