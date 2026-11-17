# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/web/cache/web_downloader.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
from functools import partial as partial
from helpers import threads as threads
from gui.shared.RemoteDataDownloader import _HttpOpenUrlJob as _HttpOpenUrlJob
from helpers.web.downloader import IDownloader as IDownloader
from shared_utils import nextTick as nextTick

class WebDownloader(IDownloader):
    __worker: Any
    __paused: Any
    def __init__(self, workersLimit, queueLimit=...):
        ...
    @property
    def stopped(self):
        ...
    def close(self):
        ...
    def downloadLowPriority(self, url, callback):
        ...
    def download(self, url, callback):
        ...
    def setPause(self, value):
        ...
    def __onDownload(self, url, callback, data, lastModified, expires):
        ...
