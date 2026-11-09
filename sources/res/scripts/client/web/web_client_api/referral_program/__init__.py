# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/referral_program/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/referral_program/__init__.py
from __future__ import absolute_import
from past.builtins import basestring
from helpers import dependency
from skeletons.gui.game_control import IReferralProgramController
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _CloseReferralProgramViewSchema(W2CSchema):
    pass


class _OpenContentPage(W2CSchema):
    url = Field(required=True, type=basestring)


@w2capi(name='referral_program', key='action')
class ReferralProgramWebApi(W2CSchema):
    __referralCtrl = dependency.descriptor(IReferralProgramController)

    @w2c(_CloseReferralProgramViewSchema, 'close_referral_program_view')
    def closeReferralProgramView(self, cmd):
        if self.__referralCtrl:
            self.__referralCtrl.hideWindow()
