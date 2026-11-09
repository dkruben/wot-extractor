# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/base/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/base/handlers.py
from gui.wgcg.settings import WebRequestDataType

class RequestHandlers(object):

    def __init__(self, requester):
        self._requester = requester


class BaseRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.LOGIN): (self.__login), 
           (WebRequestDataType.LOGOUT): (self.__logout), 
           (WebRequestDataType.PING): (self.__ping)}
        return handlers

    def __login(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, 'login', ctx.getUserDatabaseID(), ctx.getTokenID(), ctx.isJwt())

    def __logout(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, 'logout')

    def __ping(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, 'get_alive_status')
