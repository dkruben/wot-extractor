# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/login/social_networks/DataServer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import hashlib as hashlib
from SocketServer import ThreadingMixIn as ThreadingMixIn
from Event import Event as Event
from Crypto.Cipher import AES as AES
from Crypto.Util import Counter as Counter
from debug_utils import LOG_DEBUG as LOG_DEBUG
from py2to3.compat import base64compat as base64compat
from .RequestHandler import RequestHandler as RequestHandler
from standalone.login import HttpServer as HttpServer

class DataServer(HttpServer):
    dataReceived: Any
    def __init__(self, name):
        ...
    def keepData(self, token, spaID, socialNetwork):
        ...
    def _logStatus(self):
        ...

class EncryptingDataServer(DataServer):
    _tokenSecret: Any
    def __init__(self, name):
        ...
    def keepData(self, token, spaID, socialNetwork):
        ...
    @property
    def tokenSecret(self):
        ...

class ThreadedDataServer(ThreadingMixIn, DataServer):
    def __init__(self, name):
        ...

class EncryptingThreadedDataServer(ThreadingMixIn, EncryptingDataServer):
    def __init__(self, name):
        ...
