# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/data/message_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control.controllers.dyn_squad_functional import DYN_SQUAD_TYPE as DYN_SQUAD_TYPE
from messenger import g_settings as g_settings
from messenger.gui.Scaleform import FILL_COLORS as FILL_COLORS
from messenger.proto.shared_messages import ACTION_MESSAGE_TYPE as ACTION_MESSAGE_TYPE
_MESSAGE_FORMATTERS_MAP: dict

class BaseMessageFormatter(object):
    _actionMessage: Any
    def __init__(self, actionMessage):
        ...
    def getFormattedMessage(self):
        ...
    def getFillColor(self):
        ...

class WarningMessageFormatter(BaseMessageFormatter):
    FONT_COLOR_GENERAL = '#FFC364'
    def __init__(self, actionMessage):
        ...
    def getFormattedMessage(self):
        ...

class ErrorMessageFormatter(BaseMessageFormatter):
    def getFormattedMessage(self):
        ...

class DynamicSquadMessageFormatter(WarningMessageFormatter):
    _DYN_SQUAD_IMAGE = 'squad_silver_{0}'
    FONT_COLOR_GENERAL = '#FFC364'
    FONT_COLOR_TEAM_SIDE_BASED = '#999999'
    def getFormattedMessage(self):
        ...
    def getFillColor(self):
        ...

class FairplayWarningMessageFormatter(BaseMessageFormatter):
    def getFormattedMessage(self):
        ...

class CommendationsMessageFormatter(BaseMessageFormatter):
    def getFormattedMessage(self):
        ...
    def getFillColor(self):
        ...

def getMessageFormatter(actionMessage):
    ...
