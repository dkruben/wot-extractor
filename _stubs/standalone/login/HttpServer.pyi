# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/standalone/login/HttpServer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
from future.moves.http.server import HTTPServer as HTTPServer
from socket import error as SocketError
from threading import Thread as Thread

class HttpServer(HTTPServer):
    allow_reuse_address = False
    __BIND_ADDRESS = '127.0.0.1'
    __PORTS_POOL: tuple
    __name: Any
    __serverThread: Any
    _currentStatus: Any
    def __init__(self, name, requestHandlerClass):
        ...
    def start_listening(self):
        ...
    def stop_listening(self):
        ...
    def __setStatus(self, status):
        ...
    def _logStatus(self):
        ...
    @property
    def name(self):
        ...
