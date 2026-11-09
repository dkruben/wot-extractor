# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/request/access_token.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/access_token.py
from __future__ import absolute_import
from helpers import dependency, time_utils
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.web import IWebController
from web.web_client_api import w2c, W2CSchema, Field

class _RequestAccessTokenSchema(W2CSchema):
    force = Field(required=False, type=bool)


class AccessTokenWebApiMixin(object):
    _connectionMgr = dependency.descriptor(IConnectionManager)
    _webCtrl = dependency.descriptor(IWebController)

    @w2c(_RequestAccessTokenSchema, 'access_token')
    def accessToken(self, cmd):
        accessTokenData = yield self._webCtrl.getAccessTokenData(force=cmd.force)
        if accessTokenData is not None:
            yield {'spa_id': (str(self._connectionMgr.databaseID)), 'access_token': (str(accessTokenData.accessToken)), 
               'expires_in': (accessTokenData.expiresAt - time_utils.getCurrentTimestamp()), 
               'periphery_id': (str(self._connectionMgr.peripheryID))}
        else:
            yield {'error': 'Unable to obtain access token.'}
        return
