# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/lobby_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/lobby_constants.py
from __future__ import absolute_import
import typing
from constants import ARENA_BONUS_TYPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController
if typing.TYPE_CHECKING:
    from typing import Dict

class USER(object):
    INFO = 'userInfo'
    CLAN_INFO = 'clanInfo'
    SEND_CLAN_INVITE = 'sendClanInvite'
    CREATE_PRIVATE_CHANNEL = 'createPrivateChannel'
    ADD_TO_FRIENDS = 'addToFriends'
    REQUEST_FRIENDSHIP = 'requestFriendship'
    REMOVE_FROM_FRIENDS = 'removeFromFriends'
    ADD_TO_IGNORED = 'addToIgnored'
    REMOVE_FROM_IGNORED = 'removeFromIgnored'
    COPY_TO_CLIPBOARD = 'copyToClipBoard'
    SET_MUTED = 'setMuted'
    UNSET_MUTED = 'unsetMuted'
    CREATE_SQUAD = 'createSquad'
    CREATE_EVENT_SQUAD = 'createEventSquad'
    CREATE_BATTLE_ROYALE_SQUAD = 'createBattleRoyaleSquad'
    INVITE = 'invite'
    VEHICLE_INFO = 'vehicleInfoEx'
    END_REFERRAL_COMPANY = 'endReferralCompany'
    CREATE_MAPBOX_SQUAD = 'createMapboxSquad'


SETTINGS_WINDOWS_MAP = {}
DEFAULT_SETTINGS_ALIAS = VIEW_ALIAS.SETTINGS_WINDOW

def registerSettingsWindow(arenaBonusType, viewAlias):
    SETTINGS_WINDOWS_MAP[arenaBonusType] = viewAlias


def getSettingsWindowAlias():
    platoonController = dependency.instance(IPlatoonController)
    arenaBonusCaps = platoonController.getPrbEntityType()
    return SETTINGS_WINDOWS_MAP.get(arenaBonusCaps, DEFAULT_SETTINGS_ALIAS)
