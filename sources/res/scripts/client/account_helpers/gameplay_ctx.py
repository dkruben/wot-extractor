# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/gameplay_ctx.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/gameplay_ctx.py
from __future__ import absolute_import
import ArenaType, constants
from debug_utils import LOG_DEBUG, LOG_ERROR, LOG_WARNING
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
_ASSAULT2_GP_NAME = constants.ARENA_GAMEPLAY_NAMES[6]
ENABLED_ARENA_GAMEPLAY_NAMES = constants.ARENA_GAMEPLAY_NAMES[:3] + (_ASSAULT2_GP_NAME,)
ENABLED_ARENA_EPIC_NAMES = (
 constants.ARENA_GAMEPLAY_NAMES[15],)

def getDefaultMask():
    return ArenaType.getGameplaysMask(ENABLED_ARENA_GAMEPLAY_NAMES)


def getMask():
    from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
    settingsCore = dependency.instance(ISettingsCore)
    settingsMask = userMask = settingsCore.serverSettings.getSectionSettings(SETTINGS_SECTIONS.GAMEPLAY, 'gameplayMask', getDefaultMask())
    ctfMask = ArenaType.getGameplaysMask(('ctf', ))
    nationsMask = ArenaType.getGameplaysMask(('nations', ))
    if not userMask:
        LOG_WARNING('Gameplay is not defined', userMask)
    elif userMask & ctfMask == 0:
        LOG_WARNING('Gameplay "ctf" is not defined', userMask)
    if userMask & nationsMask:
        userMask ^= nationsMask
        LOG_DEBUG('Nations battle mode currently unavailable')
    userMask |= ctfMask
    if settingsMask != userMask:
        _setMask(userMask)
    return userMask


def setMaskByNames(names):
    gameplayNames = {
     'ctf'}
    for name in names:
        if name in ArenaType.g_gameplayNames:
            gameplayNames.add(name)
        else:
            LOG_ERROR('Gameplay is not available', name)

    gameplayMask = ArenaType.getGameplaysMask(gameplayNames)
    LOG_DEBUG('Set gameplay (names, mask)', gameplayNames, gameplayMask)
    _setMask(gameplayMask)


def isCreationEnabled(gameplayName, isEpic):
    if isEpic:
        return gameplayName in ENABLED_ARENA_EPIC_NAMES
    return gameplayName in ENABLED_ARENA_GAMEPLAY_NAMES


def _setMask(gameplayMask):
    from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
    settingsCore = dependency.instance(ISettingsCore)
    settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.GAMEPLAY, {'gameplayMask': gameplayMask})
