# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/shop.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/shop.py
from __future__ import absolute_import
from adisp import adisp_process
from gui.Scaleform.daapi.view.lobby.store.browser import shop_helpers as helpers
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.game_control.links import URLMacros
from gui.shared import events, g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shop import Source
from last_stand.gui import ls_gui_constants
BUNDLE = 'bundle'

def _getParams(reason, price, itemId=None):
    params = {'reason': reason, 
       'goldPrice': price, 
       'source': (Source.EXTERNAL)}
    if itemId is not None:
        params['itemId'] = itemId
    return params


def showBuyGoldForBundle(fullPrice, params=None):
    params = params or {}
    params.update(_getParams(BUNDLE, fullPrice))
    showBuyGoldWebOverlay(params)


@adisp_process
def showBuyGoldWebOverlay(params=None, parent=None):
    url = helpers.getBuyMoreGoldUrl()
    if url:
        url = yield URLMacros().parse(url, params=params)
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(ls_gui_constants.VIEW_ALIAS.LS_OVERLAY_WEB_STORE, parent=parent), ctx={'url': url}), EVENT_BUS_SCOPE.LOBBY)
