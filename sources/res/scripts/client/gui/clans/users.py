# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/clans/users.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/clans/users.py
import weakref
from adisp import adisp_async, adisp_process
from gui.wgcg.clan.contexts import AccountClanRatingsCtx

class UserCache(object):

    def __init__(self, clanCtrl):
        super(UserCache, self).__init__()
        self.__cache = dict()
        self.__clanCtrl = weakref.proxy(clanCtrl)

    @adisp_async
    @adisp_process
    def requestUsers(self, dbIDs, callback):
        status = True
        missingUser = [usrID for usrID in dbIDs if usrID not in self.__cache]
        if missingUser:
            usrCtx = AccountClanRatingsCtx(missingUser)
            result = yield self.__clanCtrl.sendRequest(usrCtx, allowDelay=True)
            if result.isSuccess():
                ratingsData = usrCtx.getDataObj(result.data)
                for key, item in ratingsData.iteritems():
                    self.__cache[key] = item

            else:
                status = False
        users = dict((usrID, self.__cache[usrID]) for usrID in dbIDs if usrID in self.__cache)
        callback((status, users))
