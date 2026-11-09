# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgnc/image_notification_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.image_helper import getTextureLinkByID as getTextureLinkByID
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from WebBrowser import getWebCache as getWebCache
_logger: Any

class WebImageHelper(object):
    __slots__: tuple
    __DEFAULT_TIMEOUT = 10.0
    __callbackMethod: Any
    __imageUrl: Any
    __callbackDelayer: Any
    __webCache: Any
    __defLocalDirPath: Any
    def __init__(self, defLocalDirPath='notifications'):
        ...
    # decorador original: @adisp_async
    def getLocalPath(self, imageUrl, callback=...):
        ...
    def __stop(self):
        ...
    def __onTimer(self):
        ...
    def __callMethod(self, localPath):
        ...

# decorador original: @adisp_process
def showPaymentMethodLinkNotification(method, imageUrl):
    ...
# decorador original: @adisp_process
def showPaymentMethodUnlinkNotification(method, imageUrl):
    ...
def _packImageBlock(imagePath):
    ...
