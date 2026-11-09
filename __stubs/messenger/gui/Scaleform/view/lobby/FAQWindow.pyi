# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/view/lobby/FAQWindow.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.shared.events import OpenLinkEvent as OpenLinkEvent
from messenger.gui.Scaleform.data.faq_data import FAQList as FAQList
from messenger.gui.Scaleform.meta.FAQWindowMeta import FAQWindowMeta as FAQWindowMeta
from messenger import g_settings as g_settings
FAQ_BATCH_SIZE = 5

class FAQWindow(FAQWindowMeta):
    __list: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def onLinkClicked(self, name):
        ...
    def updateData(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
