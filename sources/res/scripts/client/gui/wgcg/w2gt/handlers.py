# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/w2gt/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/w2gt/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class W2gtRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.W2GT_DATA): (self.__getTips)}
        return handlers

    def __getTips(self, ctx, callback):
        descriptor = 'w2gt'
        accessorMethod = 'get_w2gt_tips'
        return self._requester.doRequestEx(ctx, callback, (descriptor, accessorMethod), ctx.getHeaders(), ctx.getParams())
