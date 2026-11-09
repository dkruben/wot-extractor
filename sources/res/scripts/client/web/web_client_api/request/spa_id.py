# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/request/spa_id.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/spa_id.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager
from web.web_client_api import w2c, W2CSchema

class SpaIdWebApiMixin(object):
    connectionMgr = dependency.descriptor(IConnectionManager)

    @w2c(W2CSchema, 'spa_id')
    def spaId(self, cmd):
        if self.connectionMgr is not None:
            yield {'spa_id': (str(self.connectionMgr.databaseID))}
        else:
            yield {'error': 'Unable to obtain spa id'}
        return
