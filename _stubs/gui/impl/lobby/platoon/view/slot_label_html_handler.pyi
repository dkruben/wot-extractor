# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/view/slot_label_html_handler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from HTMLParser import HTMLParser as HTMLParser
from gui.impl.gen.view_models.views.lobby.platoon.slot_label_element_model import Types as Types

class SlotLabelHtmlParser(HTMLParser, object):
    parsingResult: Any
    def __init__(self):
        ...
    def handle_starttag(self, tag, attrs):
        ...
    def handle_data(self, data):
        ...
    def getElements(self):
        ...
    @staticmethod
    def __attrsToDict(attrs):
        ...

def getStyle(attrs):
    ...
