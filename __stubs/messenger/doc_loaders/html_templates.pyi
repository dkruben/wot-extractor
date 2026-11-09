# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/doc_loaders/html_templates.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from debug_utils import LOG_WARNING as LOG_WARNING
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel, NotificationGroup as NotificationGroup
from helpers.html import translation as html_translation, templates as templates

class _MessageTemplate(templates.Template):
    data: Any
    priority: Any
    groupID: Any
    def __init__(self, source, data, priority, groupID):
        ...
    @property
    def lifeTime(self):
        ...
    def format(self, ctx=None, data=None):
        ...

class MessageTemplates(templates.XMLCollection):
    def format(self, key, ctx=None, **kwargs):
        ...
    def priority(self, key):
        ...
    def groupID(self, key):
        ...
    def lifeTime(self, key):
        ...
    def __missing__(self, key):
        ...
    def _make(self, source):
        ...
    def _makeButtonData(self, sourceID, section):
        ...
    def _makeBgIconsData(self, section):
        ...

def loadForMessage(_, section, settings):
    ...
def loadForOthers(_, section, settings):
    ...
