# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/RSSDownloader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import threading as threading
import BigWorld as BigWorld
import helpers as helpers
from helpers import feedparser as feedparser
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
g_downloader = None

class RSSDownloader(object):
    UPDATE_INTERVAL = 0.1
    lastRSS: Any
    isBusy: Any
    __thread: Any
    __lastDownloadTime: Any
    __cbID: Any
    __lastRSS: Any
    __onCompleteCallbacks: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def download(self, callback, url):
        ...
    def __update(self):
        ...

class _WorkerThread(threading.Thread):
    url: Any
    result: Any
    name: Any
    def __init__(self, url):
        ...
    def run(self):
        ...

def init():
    ...
