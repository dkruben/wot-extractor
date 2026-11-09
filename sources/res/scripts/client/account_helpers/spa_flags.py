# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/spa_flags.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/spa_flags.py
from __future__ import absolute_import
from external_strings_utils import strtobool, InvalidStringValueException
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from constants import SPA_ATTRS

class SPAFlags(object):

    def __init__(self, syncData):
        super(SPAFlags, self).__init__()
        self.__account = None
        self.__syncData = syncData
        self.__cache = {}
        self.__country = ''
        self.__ignore = True
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True

    def setAccount(self, account):
        self.__account = account

    def synchronize(self, diff):
        cacheDiff = diff.get('cache', None)
        spaCache = cacheDiff.get('SPA', None) if cacheDiff else None
        itemDiff = {}
        if spaCache:
            for key in SPA_ATTRS.toClientAttrs():
                value = spaCache.get(key, None)
                if value:
                    if key == SPA_ATTRS.USER_COUNTRY:
                        self.__country = value
                    try:
                        itemDiff[key] = strtobool(value)
                    except InvalidStringValueException:
                        itemDiff[key] = value

        synchronizeDicts(itemDiff, self.__cache.setdefault('spaFlags', {}))
        return

    def getFlag(self, flagName):
        if self.__cache and 'spaFlags' in self.__cache:
            return self.__cache['spaFlags'].get(flagName, None)
        else:
            return

    def getCountry(self):
        return self.__country
