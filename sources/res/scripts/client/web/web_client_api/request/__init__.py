# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/request/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/__init__.py
from __future__ import absolute_import
from web.web_client_api import w2capi
from web.web_client_api.request.access_token import AccessTokenWebApiMixin
from web.web_client_api.request.graphics_settings import GraphicsSettingsWebApiMixin
from web.web_client_api.request.reactive_communication import ReactiveCommunicationConfigWebApiMixin
from web.web_client_api.request.settings import SettingsWebApiMixin
from web.web_client_api.request.spa_id import SpaIdWebApiMixin
from web.web_client_api.request.wgni_token import WgniTokenWebApiMixin

@w2capi('request', 'request_id')
class RequestWebApi(AccessTokenWebApiMixin, GraphicsSettingsWebApiMixin, ReactiveCommunicationConfigWebApiMixin, SettingsWebApiMixin, SpaIdWebApiMixin, WgniTokenWebApiMixin):
    pass
