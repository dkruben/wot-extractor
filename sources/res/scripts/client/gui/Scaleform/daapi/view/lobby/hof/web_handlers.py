# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hof/web_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hof/web_handlers.py
from __future__ import absolute_import
from web.web_client_api import webApiCollection, w2capi
from web.web_client_api.exchange import PersonalExchangeRatesDiscountsWebApi
from web.web_client_api.shop import ShopWebApi
from web.web_client_api.ui.browser import CloseBrowserViewWebApiMixin
from web.web_client_api.vehicles import VehiclesWebApi
from web.web_client_api.request import RequestWebApi
from web.web_client_api.sound import SoundWebApi
from web.web_client_api.ui import OpenWindowWebApi, OpenTabWebApi, ContextMenuWebApi

def createHofWebHandlers():

    @w2capi(name='close_window', key='window_id')
    class _CloseWindowWebApi(CloseBrowserViewWebApiMixin):
        pass

    return webApiCollection(_CloseWindowWebApi, OpenWindowWebApi, OpenTabWebApi, RequestWebApi, SoundWebApi, ContextMenuWebApi, ShopWebApi, VehiclesWebApi, PersonalExchangeRatesDiscountsWebApi)
