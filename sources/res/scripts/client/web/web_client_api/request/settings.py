# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/request/settings.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/settings.py
from __future__ import absolute_import
import helpers
from gui.limited_ui.lui_rules_storage import LUI_RULES
from helpers import dependency
from skeletons.gui.game_control import ILimitedUIController
from web.web_client_api import W2CSchema, w2c

class SettingsWebApiMixin(object):
    __limitedUIController = dependency.descriptor(ILimitedUIController)
    _MODE_HIDE_COUNTERS = 'hide_counters'

    @w2c(W2CSchema, 'settings')
    def getSettings(self, _):
        return {'client_version': (helpers.getClientVersion()), 
           'ui_spam_mode': ('' if self.__limitedUIController.isRuleCompleted(LUI_RULES.store) else self._MODE_HIDE_COUNTERS)}
