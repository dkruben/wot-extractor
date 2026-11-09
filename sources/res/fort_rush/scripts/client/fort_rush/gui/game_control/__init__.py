# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/game_control/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/game_control/__init__.py
from __future__ import absolute_import
from fort_rush_common import fort_rush_constants
from gui.shared.system_factory import registerAwardControllerHandlers
from fort_rush.gui.game_control.AwardController import FortRushPunishWindowHandler, FortRushAwardsController

def registerFortRushAwardControllers():
    registerAwardControllerHandlers((FortRushAwardsController, FortRushPunishWindowHandler))


def registerFortRushSMTypes():
    from gui import SystemMessages
    SystemMessages.SM_TYPE.inject(['FREventProgression'])


def registerControlModeOverrides():
    from aih_constants import CTRL_MODE_NAME, CTRL_TYPE
    from AvatarInputHandler import OVERWRITE_CTRLS_DESC_MAP
    from fort_rush_control_modes import FortRushPostMortemControlMode
    OVERWRITE_CTRLS_DESC_MAP[fort_rush_constants.ARENA_BONUS_TYPE.FORT_RUSH] = {(CTRL_MODE_NAME.POSTMORTEM): (
                                   FortRushPostMortemControlMode,
                                   'postMortemMode',
                                   CTRL_TYPE.USUAL)}
