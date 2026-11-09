# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/hof/contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/hof/contexts.py
from gui.clans import items
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType
from shared_utils import makeTupleByDict

class _BaseHofRequestCtx(CommonWebRequestCtx):

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def getDataObj(self, incomeData):
        incomeData = incomeData or {}
        return makeTupleByDict(items.HofAttrs, incomeData)

    def isCaching(self):
        return False


class HofUserInfoCtx(_BaseHofRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.HOF_USER_INFO


class HofUserExcludeCtx(_BaseHofRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.HOF_USER_EXCLUDE


class HofUserRestoreCtx(_BaseHofRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.HOF_USER_RESTORE
