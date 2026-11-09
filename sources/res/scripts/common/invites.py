# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/invites.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/invites.py
from __future__ import absolute_import
from enumerations import Enumeration
INVITE_TYPES = Enumeration('InviteTypes', [
 'BARTER', 
 'TEAM', 
 'CLAN', 
 'TRAINING_ROOM', 
 'PREBATTLE'])
_g_invitesConfig = {(INVITE_TYPES.BARTER.index()): {'TTL': 900, 'keepInArchive': 3600, 'checkIgnore': True}, 
   (INVITE_TYPES.TEAM.index()): {'TTL': (-1), 'keepInArchive': (-1), 'checkIgnore': True}, (INVITE_TYPES.CLAN.index()): {'TTL': (-1), 'keepInArchive': (-1), 'checkIgnore': True}, (INVITE_TYPES.TRAINING_ROOM.index()): {'TTL': 900, 'keepInArchive': 3600, 'checkIgnore': True}, 
   (INVITE_TYPES.PREBATTLE.index()): {'TTL': 900, 'keepInArchive': 3600, 'checkIgnore': True}}
_g_defaultInviteConfig = {'TTL': (-1), 'keepInArchive': (-1), 'checkIgnore': True}

def getInviteConfig(inviteTypeIdx):
    return _g_invitesConfig.get(inviteTypeIdx, _g_defaultInviteConfig)


INVITE_STATUS = Enumeration('Invite statuses', [
 'accepted',
 'rejected',
 'invalid',
 'invalidTTL'])
