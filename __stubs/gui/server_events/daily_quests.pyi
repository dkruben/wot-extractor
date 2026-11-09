# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/daily_quests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import AccountCommands as AccountCommands
import wg_async as wg_async
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.gui_items.processors.plugins import SyncValidator as SyncValidator, makeSuccess as makeSuccess, makeError as makeError
from gui.shared.gui_items.processors.plugins import AwaitConfirmator as AwaitConfirmator
from gui.shared.gui_items.processors import Processor as Processor, makeI18nError as makeI18nError, makeI18nSuccess as makeI18nSuccess
from gui.server_events.events_helpers import isRerollEnabled as isRerollEnabled, getRerollTimeout as getRerollTimeout
from gui.impl import backport as backport
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen import R as R
from gui.impl.dialogs.builders import WarningDialogBuilder as WarningDialogBuilder, ResSimpleDialogBuilder as ResSimpleDialogBuilder
from gui.impl.wrappers.user_format_string_arg_model import UserFormatStringArgModel as FmtArgs
_logger: Any

class DQRerollEnabledValidator(SyncValidator):
    def _validate(self):
        ...

class DQRerollCooldown(SyncValidator):
    eventsCache: Any
    def _validate(self):
        ...

class DQNotCompletedValidator(SyncValidator):
    __quest: Any
    def __init__(self, quest, isEnabled=True):
        ...
    def _validate(self):
        ...

class DQRerollConfirmator(AwaitConfirmator):
    eventsCache: Any
    _dialog: Any
    _callback: Any
    def __init__(self, isEnabled=True):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    # decorador original: @wg_async.wg_async
    def _confirm(self, callback):
        ...
    def _onSyncCompleted(self, *args, **kwargs):
        ...
    def _destroy(self):
        ...

class DailyQuestReroll(Processor):
    eventsCache: Any
    _quest: Any
    _callback: Any
    def __init__(self, quest):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def _onRerolCmdResponseReceived(self, resID):
        ...
    def _startListeningForResponse(self, callback):
        ...
    def _stopListeningForResponse(self):
        ...
    def _onEventsSyncCompleted(self):
        ...
    def __response(self, resID):
        ...
    def __resID2ErrStr(self, resID):
        ...
