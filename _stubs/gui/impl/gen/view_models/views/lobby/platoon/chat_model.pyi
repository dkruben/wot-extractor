# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/platoon/chat_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.chat_message_model import ChatMessageModel as ChatMessageModel
from gui.impl.gen.view_models.views.lobby.platoon.chat_message_part_model import ChatMessagePartModel as ChatMessagePartModel

class ChatModel(ViewModel):
    __slots__: tuple
    onSend: Any
    onInputCleared: Any
    def __init__(self, properties=3, commands=2):
        ...
    @property
    def headerExtraInfo(self):
        ...
    @staticmethod
    def getHeaderExtraInfoType():
        ...
    def getMessages(self):
        ...
    def setMessages(self, value):
        ...
    @staticmethod
    def getMessagesType():
        ...
    def getCanClearInput(self):
        ...
    def setCanClearInput(self, value):
        ...
    def _initialize(self):
        ...
