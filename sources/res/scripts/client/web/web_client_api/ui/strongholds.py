# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/strongholds.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/strongholds.py
from __future__ import absolute_import
from gui.clans.clan_helpers import getStrongholdUrl
from gui.impl.lobby.clan_supply.clan_supply_helpers import showClanSupplyView
from gui.shared import event_dispatcher as shared_events
from uilogging.clan_supply.constants import ClanSupplyLogKeys
from web.web_client_api import w2c, W2CSchema

class StrongholdsWebApiMixin(object):

    @w2c(W2CSchema, 'strongholds')
    def openStrongholds(self, cmd):
        url = getStrongholdUrl() + cmd.custom_parameters.get('url', '')
        shared_events.showStrongholds(url)

    @w2c(W2CSchema, 'clan_supply')
    def openClanSupply(self, cmd):
        tabID = cmd.custom_parameters.get('page')
        showClanSupplyView(tabId=tabID, parentScreenLog=ClanSupplyLogKeys.CLAN_LANDING)
