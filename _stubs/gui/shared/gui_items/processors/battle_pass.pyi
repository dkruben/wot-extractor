# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/battle_pass.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import BigWorld as BigWorld
from gui import SystemMessages as SystemMessages
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.processors import Processor as Processor, plugins as plugins, makeError as makeError
from gui.shared.gui_items.processors.plugins import MessageConfirmator as MessageConfirmator, SyncValidator as SyncValidator
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
_logger: Any

class _BattlePassActivateChapterValidator(SyncValidator):
    __battlePassController: Any
    __chapterID: Any
    def __init__(self, chapterID, isEnabled=True):
        ...
    def _validate(self):
        ...
    def __isValid(self):
        ...

class _BattlePassActivateChapterConfirmator(MessageConfirmator):
    __chapterID: Any
    def __init__(self, chapterID, isEnabled=True):
        ...
    def _gfMakeMeta(self):
        ...

class BattlePassActivateChapterProcessor(Processor):
    __battlePassController: Any
    __WAITING_TEXT = 'switchChapter'
    __chapterID: Any
    __seasonID: Any
    __hasActiveChapter: Any
    def __init__(self, chapterID, seasonID):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def __pushSuccessMessage(self):
        ...

class BuyBattlePass(Processor):
    __battlePass: Any
    __seasonID: Any
    __chapterID: Any
    def __init__(self, seasonID, chapterID):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class BuyBattlePassLevels(Processor):
    __seasonID: Any
    __chapterID: Any
    __levels: Any
    def __init__(self, seasonID, chapterID, levels):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class BuyBattlePassWithLevels(Processor):
    __battlePass: Any
    __seasonID: Any
    __chapterID: Any
    def __init__(self, seasonID, chapterID):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...
