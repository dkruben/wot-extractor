# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/challenges.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from functools import partial as partial
from gui.impl import backport as backport
from gui import SystemMessages as SystemMessages
from gui.impl.gen import R as R
from gui.shared.gui_items.processors import Processor as Processor, makeError as makeError, makeSuccess as makeSuccess
from gui.shared.gui_items.processors.plugins import MessageConfirmator as MessageConfirmator
from gui.shared.money import Money as Money
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime, makeLocalServerTime as makeLocalServerTime
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from skeletons.gui.challenges import IChallengesController as IChallengesController

class _ChallengesActionConfirmator(MessageConfirmator):
    __challengeID: Any
    __actionType: Any
    __isFree: Any
    def __init__(self, challengeID, actionType, isFree=False):
        ...
    def _gfMakeMeta(self):
        ...

class _ChallengesProcessor(Processor):
    _challengesCtrl: Any
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _getMessageKey(self):
        ...
    def _makeError(self, errStr):
        ...

class ActivateChallengeProcessor(_ChallengesProcessor):
    __ACTION_TYPE = 'activate'
    __challengeId: Any
    def __init__(self, challengeId):
        ...
    def _request(self, callback):
        ...
    def _getMessageKey(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class RestartChallengeProcessor(_ChallengesProcessor):
    __ACTION_TYPE = 'restart'
    __challengeId: Any
    __isFree: Any
    def __init__(self, challengeId, isFree):
        ...
    def _request(self, callback):
        ...
    def _getMessageKey(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class SurrenderChallengeProcessor(_ChallengesProcessor):
    __ACTION_TYPE = 'surrender'
    __challengeId: Any
    def __init__(self, challengeId):
        ...
    def _request(self, callback):
        ...
    def _getMessageKey(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
