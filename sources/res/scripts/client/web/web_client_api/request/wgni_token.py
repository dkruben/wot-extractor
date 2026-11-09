# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/request/wgni_token.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/wgni_token.py
from __future__ import absolute_import
from constants import TOKEN_TYPE
from gui.shared.utils.requesters import getTokenRequester
from web.web_client_api import w2c, W2CSchema

class WgniTokenWebApiMixin(object):

    @w2c(W2CSchema, 'token1')
    def wgniToken(self, cmd):
        tokenRqs = getTokenRequester(TOKEN_TYPE.WGNI)
        if not tokenRqs.isInProcess():
            response = yield tokenRqs.request(timeout=10.0)
        else:
            response = None
        if response and response.isValid():
            yield {'request_id': 'token1', 'spa_id': (str(response.getDatabaseID())), 
               'token': (response.getToken())}
        else:
            coolDownExpiration = tokenRqs.getReqCoolDown() - tokenRqs.lastResponseDelta()
            yield {'request_id': 'token1', 
               'error': 'Unable to obtain token.', 
               'cooldown': (coolDownExpiration if coolDownExpiration > 0 else tokenRqs.getReqCoolDown())}
        return
