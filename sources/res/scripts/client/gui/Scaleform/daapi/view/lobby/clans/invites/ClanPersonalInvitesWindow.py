# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanPersonalInvitesWindow.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanPersonalInvitesWindow.py
from __future__ import absolute_import
from gui.clans.clan_helpers import ClanListener
from gui.clans import formatters
from gui.Scaleform.daapi.view.meta.ClanPersonalInvitesWindowMeta import ClanPersonalInvitesWindowMeta
from gui.Scaleform.locale.CLANS import CLANS
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as _ms

class ClanPersonalInvitesWindow(ClanPersonalInvitesWindowMeta, ClanListener):

    def __init__(self, *args, **kwargs):
        super(ClanPersonalInvitesWindow, self).__init__()

    def onClanEnableChanged(self, enabled):
        if not enabled:
            self.onWindowClose()

    def onAccountClanProfileChanged(self, profile):
        if profile.isInClan():
            self.destroy()

    def onAccountInvitesReceived(self, invites):
        self._updateActualInvites()

    def _populate(self):
        super(ClanPersonalInvitesWindow, self)._populate()
        self.startClanListening()
        self._updateActualInvites()

    def _dispose(self):
        super(ClanPersonalInvitesWindow, self)._dispose()
        self.stopClanListening()

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(ClanPersonalInvitesWindow, self)._onRegisterFlashComponent(viewPy, alias)
        viewPy.setParentWindow(self)

    def onWindowClose(self):
        self.destroy()

    def _updateActualInvites(self):
        self.as_setActualInvitesTextS(_ms(CLANS.CLANPERSONALINVITESWINDOW_ACTUALINVITES, count=text_styles.stats(formatters.formatInvitesCount(self.webCtrl.getAccountProfile().getInvitesCount()))))
