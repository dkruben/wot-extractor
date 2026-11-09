# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/tankman.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/tankman.py
from __future__ import absolute_import
from past.builtins import basestring
from gui.server_events.recruit_helper import getRecruitInfo
from web.web_client_api import w2c, W2CSchema, Field
from gui.server_events import events_dispatcher as server_events

class _RecruitIDSchema(W2CSchema):
    recruit_id = Field(required=True, type=basestring, validator=(lambda value, _: _tankManTokenValidator(value)))


def _tankManTokenValidator(tokenID):
    return getRecruitInfo(tokenID) is not None


class OpenTankmanWebApiMixin(object):

    @w2c(_RecruitIDSchema, 'recruit')
    def openRecruitingWindow(self, cmd):
        server_events.showRecruitWindow(cmd.recruit_id.encode())
