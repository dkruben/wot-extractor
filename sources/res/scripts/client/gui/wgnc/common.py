# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgnc/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/common.py
import logging, typing
if typing.TYPE_CHECKING:
    from web.web_client_api import CommandHandler
_logger = logging.getLogger(__name__)

class WebHandlersContainer(object):
    _webHandlers = {}

    @classmethod
    def addWebHandler(cls, name, handler):
        cls._webHandlers[name] = handler

    @classmethod
    def removeWebHandler(cls, name):
        if name in cls._webHandlers:
            del cls._webHandlers[name]

    @classmethod
    def getWebHandler(cls, name):
        if name is None:
            return
        else:
            if name not in cls._webHandlers:
                _logger.warning("Cannot get web client handler by name '%s'", name)
                return
            return cls._webHandlers[name]
