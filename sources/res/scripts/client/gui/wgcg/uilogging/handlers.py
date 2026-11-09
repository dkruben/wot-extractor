# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/uilogging/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/uilogging/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class UILoggingRequestHandlers(RequestHandlers):

    def get(self):
        return {(WebRequestDataType.UI_LOGGING_SESSION): (self.__getSession)}

    def __getSession(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('uilogging', 'get_uilogging_session'))
