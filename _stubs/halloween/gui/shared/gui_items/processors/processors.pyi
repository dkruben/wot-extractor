# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/shared/gui_items/processors/processors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from gui import SystemMessages as SystemMessages
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import formatPrice as formatPrice
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.gui_items.processors import Processor as Processor, makeError as makeError
from gui.shared.gui_items.processors.plugins import MoneyValidator as MoneyValidator
from gui.shared.money import Money as Money
from halloween.gui.shared.gui_items.processors.plugins import CheckArtefact as CheckArtefact, CheckTwitchCon as CheckTwitchCon

class OpenArtefactProcessor(Processor):
    MSG_KEY = R.strings.halloween_system_messages.open_artefact
    MSG_TYPE = SM_TYPE.Information
    _controller: Any
    _artefactID: Any
    _isSkipQuest: Any
    def __init__(self, controller, artefactID, isSkipQuest):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class ChoiceProcessor(Processor):
    MSG_KEY = R.strings.halloween_system_messages.make_choice
    MSG_TYPE = SM_TYPE.Information
    _choiceID: Any
    def __init__(self, choiceID):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class BuyBundleProcessor(Processor):
    MSG_KEY = R.strings.halloween_system_messages.open_artefact
    _bundleID: Any
    _price: Any
    _count: Any
    def __init__(self, bundleID, price, count):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def __pushSuccessMessage(self):
        ...

class ExchangeCommandersProcessor(Processor):
    MSG_KEY = R.strings.halloween_system_messages.open_artefact
    MSG_TYPE = SM_TYPE.Information
    _commandersData: Any
    def __init__(self, controller, commandersData):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
