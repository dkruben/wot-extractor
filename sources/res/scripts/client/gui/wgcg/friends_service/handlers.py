# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/friends_service/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/friends_service/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class FriendServiceRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.FRIEND_STATE): (self.__getFriendBalance), 
           (WebRequestDataType.FRIEND_LIST): (self.__getFriendList), 
           (WebRequestDataType.PUT_BEST_FRIEND): (self.__putBestFriend), 
           (WebRequestDataType.DELETE_BEST_FRIEND): (self.__deleteBestFriend), 
           (WebRequestDataType.POST_GATHER_FRIEND_NY_RESOURCES): (self.__gatherFriendResources)}
        return handlers

    def __getFriendBalance(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('friends', 'get_friend_balance'), ctx.getSpaId())

    def __getFriendList(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('friends', 'get_friend_list'))

    def __putBestFriend(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('friends', 'put_best_friend'), ctx.getSpaId())

    def __deleteBestFriend(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('friends', 'delete_best_friend'), ctx.getSpaId())

    def __gatherFriendResources(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('friends', 'post_gather_friend_ny_resources'), ctx.getSpaId())
