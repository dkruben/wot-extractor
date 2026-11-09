# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/promo/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/promo/__init__.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.game_control import IPromoController
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _PromoCountSchema(W2CSchema):
    count = Field(required=True, type=int)


@w2capi(name='promo', key='action')
class PromoWebApi(object):
    _promoCtrl = dependency.descriptor(IPromoController)

    @w2c(_PromoCountSchema, 'unread_count')
    def promoCount(self, cmd):
        self._promoCtrl.setUnreadPromoCount(cmd.count)
