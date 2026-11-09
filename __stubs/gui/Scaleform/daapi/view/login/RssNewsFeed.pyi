# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/RssNewsFeed.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import uuid as uuid
import BigWorld as BigWorld
import ResMgr as ResMgr
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.view.meta.RssNewsFeedMeta import RssNewsFeedMeta as RssNewsFeedMeta
from gui.game_control.links import URLMacros as URLMacros
from helpers import dependency as dependency
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController, IBrowserController as IBrowserController
_logger: Any

class RssNewsFeed(RssNewsFeedMeta):
    UPDATE_INTERVAL = 60
    DESCRIPTION_MAX_LENGTH = 250
    DESCRIPTION_TAIL = '...'
    DESCRIPTION_CUT_LENGTH: Any
    SHOW_NEWS_COUNT = 3
    externalBrowser: Any
    internalBrowser: Any
    __requestCbID: Any
    __feed: Any
    __urlMacros: Any
    def __init__(self):
        ...
    def getFeed(self):
        ...
    def openBrowser(self, linkToOpen):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    # decorador original: @adisp_process
    def __requestFeed(self):
        ...
    def __onRssFeedReceived(self, data):
        ...
    def __clearCallback(self):
        ...
    def __updateCallback(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __getRssUrl(self, callback):
        ...
    def __prepareData(self, entryData):
        ...
