# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/data/faq_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from builtins import range as range
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from gui.impl.gen import R as R
from gui.shared.events import OpenLinkEvent as OpenLinkEvent
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from skeletons.gui.impl import IGuiLoader as IGuiLoader
_logger: Any
QUESTION_FORMAT = 'question_{0:d}'
ANSWER_FORMAT = 'answer_{0:d}'
SUPPORTED_LINKS_EVENTS: tuple
FAQItem: Any

class FAQList(object):
    gui: Any
    __extraFormats: Any
    __links: Any
    __list: Any
    __cursor: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def getItem(self, index):
        ...
    def getIterator(self, offset=0):
        ...
    def __buildLinks(self):
        ...
    def __buildList(self):
        ...
    def __formatLinksInAnswer(self, answer):
        ...
    def __findAnswerWithSuffix(self, answer):
        ...
