# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/clan_cm_handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/clan_cm_handlers.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.clans import formatters as clans_fmts
from gui.shared import event_dispatcher, utils
from shared_utils import CONST_CONTAINER

class CLAN_CM_OPTIONS(CONST_CONTAINER):
    CLAN_PROFILE = 'clanProfile'
    COPY_TO_CB = 'copyToClipboard'


class BaseClanCMHandler(AbstractContextMenuHandler, EventSystemEntity):

    def __init__(self, cmProxy, ctx=None):
        super(BaseClanCMHandler, self).__init__(cmProxy, ctx, {(CLAN_CM_OPTIONS.CLAN_PROFILE): 'showClanProfile', 
           (CLAN_CM_OPTIONS.COPY_TO_CB): 'copyToClipboard'})
        self.__clanDbID = int(ctx.dbID)
        self.__clanName = ctx.clanName
        self.__clanAbbrev = ctx.clanAbbrev

    def showClanProfile(self):
        event_dispatcher.showClanProfileWindow(self.__clanDbID, self.__clanAbbrev)

    def copyToClipboard(self):
        utils.copyToClipboard(clans_fmts.getClanFullName(self.__clanName, self.__clanAbbrev))

    def _generateOptions(self, ctx=None):
        return [
         self._makeItem(CLAN_CM_OPTIONS.CLAN_PROFILE, MENU.contextmenu('viewClanProfile')),
         self._makeItem(CLAN_CM_OPTIONS.COPY_TO_CB, MENU.contextmenu('copyClanName'))]
