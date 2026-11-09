# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/base/response.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import httplib as httplib
import typing as typing
import enum as enum
from gui.shared.utils.requesters.abstract import Response as Response

# decorador original: @enum.unique
class Codes(enum.IntEnum):
    SUCCESS = 0
    AUTHORIZATION_ERROR = 1
    POW_NOT_SOLVED = 2
    REQUEST_TIMEOUT = 3
    REQUEST_CANCELED = 4
    REQUEST_DESTROYED = 5
    HTTP_REQUEST_ERROR = 6
    UNEXPECTED_ERROR = 7
    SERVICE_NOT_STARTED = 8
    SERVICE_DISABLED = 9

class PlatformResponse(Response):
    @property
    def isCreated(self):
        ...
    @classmethod
    def createRequestCanceled(cls):
        ...
    @classmethod
    def createRequestDestroyed(cls):
        ...
    @classmethod
    def createServiceNotStarted(cls):
        ...
    @classmethod
    def createServiceDisabled(cls):
        ...
    @classmethod
    def createUnexpectedError(cls, txtStr=''):
        ...
    @classmethod
    def createAuthorizationError(cls):
        ...
    @classmethod
    def createPowNotSolved(cls):
        ...
    @classmethod
    def createRequestTimeout(cls):
        ...
    @classmethod
    def createHttpError(cls, extraCode, txtStr='', data=None, headers=None):
        ...
    @classmethod
    def createSuccess(cls, extraCode=..., txtStr='', data=None, headers=None):
        ...
    @classmethod
    def createError(cls, code, extraCode=..., txtStr='', data=None, headers=None):
        ...
    def getData(self):
        ...
    @classmethod
    def _create(cls, code, extraCode, txtStr='', data=None, headers=None):
        ...
    def _isError(self, errorType, *errorNames):
        ...
