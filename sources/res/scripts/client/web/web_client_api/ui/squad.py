# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/squad.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/squad.py
from __future__ import absolute_import
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import PrbAction
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from web.web_client_api import w2c, W2CSchema, Field
from web.web_client_api.common import SPA_ID_TYPES

class _CreateSquadSchema(W2CSchema):
    spa_id = Field(required=True, type=SPA_ID_TYPES)


class SquadWebApiMixin(object):

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @w2c(_CreateSquadSchema, 'squad_window')
    def createSquad(self, usersIds):
        yield self.prbDispatcher.doSelectAction(PrbAction(PREBATTLE_ACTION_NAME.SQUAD, accountsToInvite=(usersIds.spa_id,)))
