# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/uilogging/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/uilogging/__init__.py
from __future__ import absolute_import
from past.builtins import basestring
from helpers import dependency
from skeletons.ui_logging import IUILoggingCore
from uilogging.constants import LogLevels
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _UILoggingLogSchema(W2CSchema):
    feature = Field(required=True, type=basestring)
    group = Field(required=True, type=basestring)
    log_action = Field(required=True, type=basestring)
    log_level = Field(required=False, type=int, default=LogLevels.INFO)
    params = Field(required=False, type=dict, default={})


@w2capi(name='ui_logging', key='action')
class UILoggingWebApi(object):
    _logger = dependency.descriptor(IUILoggingCore)

    @w2c(_UILoggingLogSchema, 'log')
    def log(self, cmd):
        self._logger.log(feature=cmd.feature, group=cmd.group, action=cmd.log_action, loglevel=cmd.log_level, **cmd.params)
